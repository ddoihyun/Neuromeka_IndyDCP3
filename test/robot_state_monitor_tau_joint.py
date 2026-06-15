# ***********************************************************************
#
# Indy Robot State Monitor
#
# 기능:
#   - indy.get_robot_data()['op_state'] 를 폴링하여 상태 변화 감지
#   - TELE_OP(17) 또는 TEACHING(7) 진입/이탈 시 로그 출력
#   - 상태 변화 시마다 tau_ext, q 값을 실시간 출력
#   - force_control.py 와 동일한 로그 포맷 사용
#
# 사용법:
#   python robot_state_monitor.py
#   python robot_state_monitor.py --ip 192.168.0.137 --index 0
#
# ***********************************************************************

from __future__ import annotations

import argparse
import logging
import sys
import time
from typing import Optional

from neuromeka import IndyDCP3


# ===================================================================
# 설정값
# ===================================================================

ROBOT_IP    = '192.168.0.137'
ROBOT_INDEX = 0

POLL_INTERVAL   = 0.1    # 상태 폴링 주기 (초)
STREAM_INTERVAL = 0.5    # TELE_OP / TEACHING 진행 중 tau_ext & q 출력 주기 (초)


# ===================================================================
# OpState 정의
# ===================================================================

OP_STATE_NAMES = {
    0:  'SYSTEM_OFF',
    1:  'SYSTEM_ON',
    2:  'VIOLATE',
    3:  'RECOVER_HARD',
    4:  'RECOVER_SOFT',
    5:  'IDLE',
    6:  'MOVING',
    7:  'TEACHING',       # 직접교시
    8:  'COLLISION',
    9:  'STOP_AND_OFF',
    10: 'COMPLIANCE',
    11: 'BRAKE_CONTROL',
    12: 'SYSTEM_RESET',
    13: 'SYSTEM_SWITCH',
    15: 'VIOLATE_HARD',
    16: 'MANUAL_RECOVER',
    17: 'TELE_OP',        # 텔레오퍼레이션
}

MONITORED_STATES = {7, 17}   # 집중 모니터링 대상 상태


# ===================================================================
# 로그 포맷 — force_control.py 와 동일한 스타일
# ===================================================================

class _CompactFormatter(logging.Formatter):
    LEVEL_ABBREV = {
        logging.DEBUG:    'DEBUG  ',
        logging.INFO:     'INFO   ',
        logging.WARNING:  'WARN   ',
        logging.ERROR:    'ERROR  ',
        logging.CRITICAL: 'CRIT   ',
    }

    def format(self, record):
        ts  = self.formatTime(record, '%H:%M:%S')
        ms  = int(record.msecs)
        lvl = self.LEVEL_ABBREV.get(record.levelno, record.levelname[:7])
        msg = record.getMessage()
        return f'[{ts}.{ms:03d}] [{lvl}] {msg}'


def _build_logger() -> logging.Logger:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(_CompactFormatter())
    logger  = logging.getLogger('RobotMonitor')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.propagate = False
    return logger


log = _build_logger()

DIVIDER = '─' * 62


# ===================================================================
# 유틸리티
# ===================================================================

def state_label(op_state: int) -> str:
    name = OP_STATE_NAMES.get(op_state, f'UNKNOWN({op_state})')
    return f'{name}({op_state})'


def print_tau_q(indy: IndyDCP3, prefix: str = '') -> None:
    """tau_ext 와 q 를 한 줄씩 출력한다."""
    try:
        ctrl = indy.get_control_state()
        tau  = ctrl.get('tau_ext', [])
        q    = ctrl.get('q', [])

        tau_str = '  '.join(f'{v:+8.4f}' for v in tau)
        q_str   = '  '.join(f'{v:+8.4f}' for v in q)

        log.info('%s tau_ext [Nm] : [ %s ]', prefix, tau_str)
        log.info('%s q      [deg] : [ %s ]', prefix, q_str)
    except Exception as e:
        log.warning('get_control_state 오류: %s', e)


# ===================================================================
# 메인 모니터링 루프
# ===================================================================

def monitor(indy: IndyDCP3) -> None:
    log.info(DIVIDER)
    log.info('  로봇 상태 모니터 시작')
    log.info(DIVIDER)
    log.info('로봇 IP    : %s  (index=%d)', ROBOT_IP, ROBOT_INDEX)
    log.info('폴링 주기  : %.0f ms', POLL_INTERVAL * 1000)
    log.info('스트림 주기: %.0f ms  (TELE_OP / TEACHING 진행 중)', STREAM_INTERVAL * 1000)
    log.info('감시 상태  : %s',
             ', '.join(state_label(s) for s in sorted(MONITORED_STATES)))
    log.info(DIVIDER)

    prev_op_state: Optional[int] = None
    last_stream_time: float      = 0.0

    log.info('모니터링 시작 — Ctrl+C 로 종료')

    try:
        while True:
            t_now = time.time()

            # ── 상태 읽기 ──────────────────────────────────────────
            try:
                robot_data = indy.get_robot_data()
                op_state   = int(robot_data.get('op_state', -1))
            except Exception as e:
                log.error('get_robot_data 오류: %s', e)
                time.sleep(POLL_INTERVAL)
                continue

            # ── 상태 변화 감지 ─────────────────────────────────────
            if op_state != prev_op_state:
                prev_label = state_label(prev_op_state) if prev_op_state is not None else '(시작 전)'
                curr_label = state_label(op_state)

                log.info(DIVIDER)

                # 진입 메시지
                if op_state == 17:
                    log.info('🤖 ▶ TELE_OP 모드 시작  (%s → %s)', prev_label, curr_label)
                elif op_state == 7:
                    log.info('✋ ▶ 직접교시(TEACHING) 모드 시작  (%s → %s)', prev_label, curr_label)
                elif prev_op_state in MONITORED_STATES:
                    # 특수 모드에서 빠져나온 경우
                    exited_label = state_label(prev_op_state)
                    log.info('⏹  %s 종료  → %s', exited_label, curr_label)
                else:
                    log.info('상태 변경: %s → %s', prev_label, curr_label)

                log.info(DIVIDER)

                # 상태 변화 시점의 tau_ext, q 스냅샷
                print_tau_q(indy, prefix='  [변화 시점]')

                log.info(DIVIDER)

                prev_op_state   = op_state
                last_stream_time = t_now

            # ── 활성 모드 중 주기적 스트리밍 ──────────────────────
            if op_state in MONITORED_STATES:
                if t_now - last_stream_time >= STREAM_INTERVAL:
                    mode_tag = 'TELE_OP' if op_state == 17 else 'TEACHING'
                    print_tau_q(indy, prefix=f'  [{mode_tag}]')
                    last_stream_time = t_now

            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        log.info(DIVIDER)
        log.info('⏹  사용자 종료 (Ctrl+C)')
        log.info(DIVIDER)


# ===================================================================
# 진입점
# ===================================================================

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Indy 로봇 상태 모니터 (TELE_OP / TEACHING 감지)'
    )
    parser.add_argument('--ip',    default=ROBOT_IP,    help=f'로봇 IP (기본값: {ROBOT_IP})')
    parser.add_argument('--index', default=ROBOT_INDEX, type=int,
                        help=f'로봇 인덱스 (기본값: {ROBOT_INDEX})')
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # 전역 설정을 CLI 인수로 덮어쓰기
    global ROBOT_IP, ROBOT_INDEX
    ROBOT_IP    = args.ip
    ROBOT_INDEX = args.index

    log.info(DIVIDER)
    log.info('  Indy 로봇 연결 중...')
    log.info(DIVIDER)
    log.info('로봇 IP : %s', ROBOT_IP)
    log.info('인덱스  : %d', ROBOT_INDEX)

    try:
        indy = IndyDCP3(robot_ip=ROBOT_IP, index=ROBOT_INDEX)
        log.info('✓ 로봇 연결 성공')
    except Exception as e:
        log.error('✗ 로봇 연결 실패: %s', e)
        sys.exit(1)

    monitor(indy)


if __name__ == '__main__':
    main()