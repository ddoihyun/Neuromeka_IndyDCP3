# Neuromeka IndyDCP3 Python 정리

원본 HTML: `C:\Users\neuromeka\Documents\Dohyun.kwak\Neuromeka_IndyDCP_Study\Python - Neuromeka Docs - 한국어.html`

이 README는 Neuromeka Docs 한국어 페이지의 IndyDCP3 Python 클라이언트 내용을 Markdown으로 정리한 문서입니다. 원본 본문에 있는 설치 명령어, 예제 코드, 출력 예시, 함수 표를 보존했고, HTML 주석 안에 들어 있던 로봇 설정 함수 섹션도 부록에 포함했습니다.

## 함수 빠른 색인

아래 색인은 원본 HTML의 본문 제목과 주석 처리된 함수 표에서 추출했습니다. 상세 설명과 예제는 아래 본문 정리에 그대로 보존되어 있습니다.

### 실시간 데이터 획득 함수
| 함수/항목 |
| --- |
| **`get_robot_data()`** |
| **`get_control_state()`** |
| **`get_motion_data()`** |
| **`get_servo_data()`** |
| **`get_violation_data()`** |
| **`get_program_data()`** |

### 입출력 디바이스 관련 함수
| 함수/항목 |
| --- |
| **`get_di()`** |
| **`get_do()`, `set_do()`** |
| **`get_ai()`** |
| **`get_ao()`, `set_ao()`** |
| **`get_endtool_di()`** |
| **`set_endtool_do()`**, **`get_endtool_do()`** |
| **`get_endtool_ai()`** |
| **`set_endtool_ao()`**, **`get_endtool_ao()`** |
| **`get_device_info()`** |
| **`get_ft_sensor_data()`** |

### 모션 명령 함수
| 함수/항목 |
| --- |
| **`stop_motion(stop_category)`** |
| **`move_home()`** |
| **`movej(...)`** |
| **`movel(...)`** |
| **`movec(...)`** |
| **`move_gcode(...)`** |

### 텔레오퍼레이션 관련 함수
| 함수/항목 |
| --- |
| **`start_teleop(method)`, `stop_teleop()`** |
| **`movetelej_rel(jpos, vel_ratio, acc_ratio)`** |
| **`movetelel_rel(tpos, vel_ratio, acc_ratio)`** |
| **`get_teleop_device()`** |
| **`get_teleop_state()`** |
| **`connect_teleop_device(name, type, ip, port)`** |
| **`disconnect_teleop_device()`** |
| **`read_teleop_input()`** |
| **`get_tele_file_list()`** |
| **`save_tele_motion(name)`** |
| **`load_tele_motion(name)`** |
| **`delete_tele_motion(name)`** |
| **`enable_tele_key(enable)`** |
| **`set_play_rate(rate)`** |
| **`get_play_rate()`** |

### 변수 (Variable)
| 함수/항목 |
| --- |
| **`get_bool_variable()`** |
| **`set_bool_variable(bool_variables)`** |
| **`get_int_variable()`** |
| **`set_int_variable(int_variables)`** |
| **`get_float_variable()`** |
| **`get_jpos_variable()`** |
| **`get_tpos_variable()`** |
| **`set_tpos_variable(tpos_variables)`** |

### 역기구학과 시뮬레이션 모드 관련 함수
| 함수/항목 |
| --- |
| **`inverse_kin(tpos, init_jpos)`** |
| **`set_direct_teaching(enable)`** |
| **`set_simulation_mode(enable)`** |
| **`recover()`** |

### 프로그램 제어 관련 함수
| 함수/항목 |
| --- |
| **`play_program(prog_name, prog_idx)`** |
| **`pause_program()`** |
| **`resume_program()`** |
| **`stop_program()`** |

### IndySDK 사용
| 함수/항목 |
| --- |
| **`activate_sdk()`** |
| **`set_custom_control_mode()`** |
| **`get_custom_control_mode()`** |
| **`set_custom_control_gain()`** |
| **`get_custom_control_gain()`** |
| **`set_joint_control_gain(kp, kv, kl2)`** |
| **`get_joint_control_gain()`** |
| **`set_task_control_gain(kp, kv, kl2)`** |
| **`get_task_control_gain()`** |
| **`set_impedance_control_gain(mass, damping, stiffness, kl2)`** |
| **`get_impedance_control_gain()`** |
| **`set_force_control_gain(kp, kv, kl2, mass, damping, stiffness, kpf, kif)`** |
| **`get_force_control_gain()`** |

### 유틸리티 함수
| 함수/항목 |
| --- |
| **`start_log()`**, **`end_log()`** |
| **`wait_for_operation_state(op_state)`** |
| **`wait_for_motion_state(motion_state)`** |
| **`set_friction_comp_state(enable)`** |
| **`get_friction_comp_state()`** |
| **`set_mount_pos(rot_y, rot_z)`** |
| **`get_mount_pos()`** |
| **`set_brakes(brake_state_list)`** |
| **`set_servo_all(enable)`** |
| **`set_servo(index, enable)`** |
| **`set_endtool_led_dim(led_dim)`** |
| **`execute_tool(name)`** |
| **`get_el5001()`** |
| **`get_el5101()`** |
| **`get_brake_control_style()`** |
| **`set_conveyor_name(name)`** |
| **`set_conveyor_encoder(encoder_type, channel1, channel2, sample_num, mm_per_tick, vel_const_mmps, reversed)`** |
| **`set_conveyor_trigger(trigger_type, channel, detect_rise)`** |
| **`set_conveyor_offset(offset_mm)`** |
| **`set_conveyor_starting_pose(jpos, tpos)`** |
| **`set_conveyor_terminal_pose(jpos, tpos)`** |

### HTML 주석 내 로봇 설정 함수
| 함수/항목 |
| --- |
| `get_home_pos()` |
| `set_home_pos(home_jpos)` |
| `get_ref_frame()` |
| `set_ref_frame()` |
| `set_ref_frame_planar()` |
| `set_tool_frame()` |
| `set_speed_ratio()` |
| `set_auto_servo_Off()` |
| `set_coll_sens_level()` |
| `get_coll_sens_level()` |
| `set_safety_limits()` |
| `get_auto_servo_off()` |
| `get_safety_limits()` |
| `set_di_config_list()` |
| `get_di_config_list()` |
| `set_do_config_list()` |
| `get_do_config_list()` |
| `set_friction_comp()` |
| `get_friction_comp()` |
| `set_tool_property()` |
| `get_tool_property()` |
| `set_coll_sens_param()` |
| `get_coll_sens_param()` |
| `set_safety_stop_config()` |
| `get_safety_stop_config()` |
| `set_home_pos(), get_home_pos()` |
| `set_ref_frame(), set_ref_frame_planar(), set_tool_frame()` |
| `set_auto_servo_Off(), get_auto_servo_off()` |
| `set_coll_sens_level(), get_coll_sens_level()` |
| `set_safety_limits(), get_safety_limits()` |
| `set_di_config_list(), set_do_config_list()` |
| `set_coll_tuning()` |

## 원문 기반 상세 정리

# Python IndyDCP3 클라이언트

Python을 사용하여 IndyDCP3 클라이언트를 사용하기 위해 먼저 **`neuromeka`** 패키지를 설치해야 합니다.

- [Github](https://github.com/neuromeka-robotics/neuromeka-package)
- [PyPI](https://pypi.org/project/neuromeka/)

특히 Github 저장소에서 `Jupyter notebook` 예제를 확인하실 수 있습니다.

## 설치 요구 사항

- Python 3.6 이상의 버전이 필요하지만, 3.9 이상의 버전에서는 동작하지 않을 수 있습니다.
- `pip3` (또는 `pip`)를 사용하여 설치합니다.

## 설치 방법

터미널이나 명령 프롬프트에서 다음 명령어를 사용하여 패키지를 설치할 수 있습니다.

```text
pip3 install neuromeka
```

아래 터미널 명령을 통해 패키지 버전 업데이트가 가능합니다.

```text
pip3 install --upgrade neuromeka
```

현재 설치된 패키지의 버전은 아래 터미널 명령을 통해 확인이 가능합니다 ([릴리즈 버전 이력](https://pypi.org/project/neuromeka/#history)).

```text
pip3 show neuromeka
```

## IndyDCP3 사용방법

클라이언트 객체를 생성하기 위해서는 `neuromeka` 패키지에서 `IndyDCP3` 클래스를 임포트해야 합니다.

```python
from neuromeka import IndyDCP3
```

IndyDCP3

클래스 객체를 생성한 후, 로봇과의 통신을 위해 다음과 같이 로봇의 IP 주소를 지정해야 합니다.

```python
indy = IndyDCP3(robot_ip='192.168.0.10', index=0)
```

- **`robot_ip`**: 로봇 컨트롤러의 IP 주소
- **`index`**: 양팔로봇과 같이 로봇 컨트롤러에 여러대의 로봇이 연결된 경우 로봇 인덱스

## 사용방법 및 함수

아래부터는 IndyDCP3의 객체를 이용하여 호출 가능한 프로토콜 함수들의 리스트를 나타냅니다. 각각의 함수들에 대한 사용방법과 입출력 예제들을 참고하여 사용해주시기 바랍니다.

Note

모든 함수의 출력은 Python dict 타입으로 반환됩니다.

---

## 실시간 데이터 획득 함수

로봇의 현재 모션 상태, 제어 데이터 및 상태, 서보 모터의 상태, 에러 사항, 그리고 프로그램의 상태 등을 반환 받을 수 있습니다.

| Function | Description |
| --- | --- |
| `get_robot_data()` | 로봇 상태 데이터 |
| `get_control_state()` | 제어 상태 |
| `get_motion_data()` | 모션 데이터 |
| `get_servo_data()` | 서보 데이터 |
| `get_violation_data()` | 에러 데이터 |
| `get_program_data()` | 로봇 프로그램 데이터 |

### **`get_robot_data()`**

```python
indy.get_robot_data()
```

```yaml
{
  'running_mins': 6,
  'running_secs': 11,
  'op_state': 5,
  'sim_mode': True,
  'ref_frame': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'tool_frame': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'running_hours': 0
}
```

- `running_hours`: 로봇 운영 시간 (시간)
- `running_mins`: 로봇 운영 시간 (분)
- `running_secs`: 로봇 운영 시간 (초)
- `op_state`: 로봇 상태를 나타내며 `OpState` 클래스에 정의
  - **`OpState`**: `SYSTEM_OFF(0)`, `SYSTEM_ON(1)`, `VIOLATE(2)`, `RECOVER_HARD(3)`, `RECOVER_SOFT(4)`, `IDLE(5)`, `MOVING(6)`, `TEACHING(7)`, `COLLISION(8)`, `STOP_AND_OFF(9)`, `COMPLIANCE(10)`, `BRAKE_CONTROL(11)`, `SYSTEM_RESET(12)`, `SYSTEM_SWITCH(13)`, `VIOLATE_HARD(15)`, `MANUAL_RECOVER(16)`, `TELE_OP(17)`
    ```python
    from neuromeka import OpState
    OpState.IDLE
    ```
    ```yaml
    5
    ```
- `sim_mode`: 시뮬레이션 모드 활성화 (True)
- `ref_frame`: 참조 프레임 ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
- `tool_frame`: 툴 프레임 ([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

### **`get_control_state()`**

```python
indy.get_control_state()
```

```yaml
{
  'q': [...],
  'qdot': [...],
  'qddot': [...],
  'qdes': [...],
  'qdotdes': [...],
  'qddotdes': [...],
  'p': [...],
  'pdot': [...],
  'pddot': [...],
  'pdes': [...],
  'pdotdes': [...],
  'pddotdes': [...],
  'tau': [...],
  'tau_act': [...],
  'tau_ext': [...],
  'tau_jts': [...],
  'tau_jts_raw1': [...],
  'tau_jts_raw2': [...],
}
```

- `q`, `qdot`, `qddot`: 현재 각 관절의 위치 (deg), 속도 (deg/s), 가속도 (deg/s²)
- `qdes`, `qdotdes`, `qddotdes`: 현재 각 관절의 목표 위치 (deg), 속도 (deg/s), 가속도 (deg/s²)
- `p`, `pdot`, `pddot`: 현재 작업공간 포즈 위치 (mm), 속도 (mm/s), 가속도 (mm/s²)
- `pdes`, `pdotdes`, `pddotdes`: 현재 작업공간 포즈 목표 위치 (mm), 속도 (mm/s), 가속도 (mm/s²)
- `tau`, `tau_act`, `tau_ext`: 현재 각 관절의 입력 토크, 실제 토크, 외력 토크 (Nm)
- `tau_jts`, `tau_jts_raw1`, `tau_jts_raw2`: 조인트 토크 센서 값.

예시로서 아래와 같이 사용하여 각 관절의 현재 각도를 `list` 타입으로 반환 받을 수 있습니다.

```python
indy.get_control_state()['q']
```

```yaml
[6.069774e-07, -22.08, 103.85, -7.2715176e-07, 98.23, -1.6545988e-10]
```

### **`get_motion_data()`**

```python
indy.get_motion_data()
```

```yaml
{
 'traj_progress': 100,
 'cur_traj_progress': 100,
 'is_target_reached': True,
 'is_in_motion': False,
 'is_pausing': False,
 'is_stopping': False,
 'traj_state': 0,
 'speed_ratio': 100,
 'has_motion': False,
 'motion_id': 0,
 'remain_distance': 0.0,
 'motion_queue_size': 0
}
```

- `traj_progress`: 전체 모션의 진행률 (%)
- `cur_traj_progress`: 현재 실행 중인 모션의 진행률 (%)
- `is_target_reached`: 타겟 위치 도달 여부 (True/False)
- `is_in_motion`: 모션 진행 중 여부 (True/False)
- `is_pausing`: 모션 일시정지 상태 (True/False)
- `is_stopping`: 모션 중단 상태 (True/False)
- `traj_state`: 모션 진행 상태를 나타내며 `TrajState` 클래스에 상태 정의
  - **`TrajState`**: `NONE(0)`, `INIT(1)`, `CALC(2)`, `STAND_BY(3)`, `ACC(4)`, `CRUISE(5)`, `DEC(6)`, `CANCELLING(7)`, `FINISHED(8)`, `ERROR(9)`
    ```python
    from neuromeka import TrajState
    TrajState.CALC
    ```
    ```yaml
    2
    ```
- `speed_ratio`: 모션 속도 비율, `set_speed_ratio()`로 설정
- `has_motion`: 모션 존재 여부 (True/False)
- `remain_distance`: 남은 거리 (mm)
- `motion_id`: 현재 모션 ID
- `motion_queue_size`: 모션 큐 크기

### **`get_servo_data()`**

```python
indy.get_servo_data()
```

```yaml
{
  'status_codes': ['0x1237', '0x1237', '0x1237', '0x1237', '0x1237', '0x1237'],
  'temperatures': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'voltages': [48.0, 48.0, 48.0, 48.0, 48.0, 48.0],
  'currents': [3.4812942e-18,
              26.195215,
              26.963966,
              0.12320003,
              0.55777645,
              4.536144e-05],
  'servo_actives': [True, True, True, True, True, True],
  'brake_actives': [False, False, False, False, False, False]
 }
```

- `status_codes`: 각 관절 서보의 상태 (CiA402)
- `temperatures`: 각 관절 서보의 온도
- `voltages`: 각 관절 서보의 전압
- `currents`: 각 관절 서보의 전류
- `servo_actives`: 각 관절 서보의 활성화 상태 (True/False)
- `brake_actives`: 각 관절 서보 브레이크의 활성화 상태 (True/False)

### **`get_violation_data()`**

```python
indy.get_violation_data()
```

```yaml
{
  'violation_code': '262144',
  'j_index': 4,
  'i_args': [2],
  'f_args': [0.0012204262],
  'violation_str': 'EMG Button Activated'
}
```

- `j_index`: violation 발생한 관절 인덱스
- `i_args`: violation 발생 사항에 대한 int 정보
- `f_args`: violation 발생 사항에 대한 float 정보
- `violation_str`: 에러 메시지
- `violation_code`: 에러 코드

| violation_code (Binary) | violation_str |
| --- | --- |
| 0b00 | None |
| 0b01 << 0 | Joint [axisIdx/DOF] Position Error Over Limit (Current: X deg, Desired: Y, Limit: Z) |
| 0b01 << 1 | Joint [axisIdx/DOF] Position Close To Limit (Current: X deg, Allowed: A ~ B) |
| 0b01 << 2 | Joint [axisIdx/DOF] Velocity Close To Limit (Current: X deg/s, Allowed: A ~ B) |
| 0b01 << 6 | TCP Singular Closed |
| 0b01 << 7 | Joint [axisIdx/DOF] Position Exceeded Limit (Current: X, Allowed: A ~ B) |
| 0b01 << 8 | Joint [axisIdx/DOF] Velocity Exceeded Limit (Current: X, Allowed: A ~ B) |
| 0b01 << 9 | Joint [axisIdx/DOF] Torque Exceeded Limit (Current: X, Allowed: A ~ B) |
| 0b01 << 10 | TCP Speed Limit: X m/s |
| 0b01 << 11 | TCP Force Limit: X N |
| 0b01 << 12 | Power Over Limit (Current: X, Allowed: Y) |
| 0b01 << 13 | Standstill Failed |
| 0b01 << 14 | Loss of Conty Communication |
| 0b01 << 15 | Loss of IndyKey Communication |
| 0b01 << 16 | Safety Guard Input 1 |
| 0b01 << 17 | Safety Guard Input 2 |
| 0b01 << 18 | EMG Button Activated |
| 0b01 << 19 | Robot Specs Reading Failed |
| 0b01 << 20 | Connection Lost - Master: masterState, Detected Joints Num: numSlavesDetected / DOF+2 |
| 0b01 << 21 | Motor Status Error: joint [axisIdx/DOF], Code = errorCode |
| 0b01 << 22 | Motor Over Current: joint [axisIdx/DOF], Code errorCode |
| 0b01 << 23 | Motor Over Heated: joint [axisIdx/DOF], Temperature X celsius |
| 0b01 << 24 | Motor Error Bit: joint [axisIdx/DOF], Code = errorCode |
| 0b01 << 25 | Motor Low Battery: joint [axisIdx/DOF], Code = errorCode |
| 0b01 << 26 | Motor Firmware Error |
| 0b01 << 27 | Task Time Over Limit (Current: X us, Allowed: Y us) |
| 0b01 << 28 | Soft Reset Failed |
| 0b01 << 29 | Auto Servo-Off Activated |
| 0b01 << 30 | TeleOp Starting Point Too Far |

### **`get_program_data()`**

```python
indy.get_program_data()
```

```yaml
{
  'program_name': 'ProgramScripts/',
  'program_state': 0,
  'cmd_id': 0,
  'sub_cmd_id': 0,
  'running_hours': 0,
  'running_mins': 0,
  'running_secs': 0,
  'program_alarm': '',
  'program_annotation': ''
}
```

- `program_name`: 현재 실행 중인 프로그램 파일 이름
- `program_state`: 프로그램 실행 상태
  - `ProgramState`: `IDLE(0)`, `RUNNING(1)`, `PAUSING(2)`, `STOPPING(3)`
    ```python
    from neuromeka import ProgramState
    ProgramState.STOPPING
    ```
    ```yaml
    3
    ```
- `running_hours`: 현재 실행중인 프로그램 재생 시간(시간)
- `running_mins`: 현재 실행중인 프로그램 재생 시간(분)
- `running_secs`: 현재 실행중인 프로그램 재생 시간(초)
- `program_alarm`: 콘티 흐름제어의 Alarm
- `program_annotation`: 콘티 흐름제어의 Annotation

## 입출력 디바이스 관련 함수

로봇의 다양한 하드웨어 상태를 설정하고 조회할 수 있는 함수를 제공합니다. 각 함수는 디지털 입/출력, 아날로그 입/출력, 엔드툴 입/출력, 특정 장치의 상태, 그리고 장치의 기본 정보 등을 관리하고 조회하는 데 사용됩니다.

Note

일부 endtool 기능은 구매하신 로봇 사양에 따라 지원하지 않을 수 있습니다.

| Function | Description |
| --- | --- |
| `get_di()` | IO보드 DI 데이터 |
| `get_do()` | IO보드 DO 데이터 |
| `set_do(do_signal_list)` | IO보드 DO 데이터 |
| `get_ai()` | IO보드 AI 데이터 |
| `get_ao()` | IO보드 AO 데이터 |
| `set_ao(ao_signal_list)` | IO보드 AO 데이터 |
| `get_endtool_di()` | 엔드툴 DI 데이터 |
| `get_endtool_do()` | 엔드툴 DO 데이터 |
| `set_endtool_do(end_do_signal_list)` | 엔드툴 DO 데이터 |
| `get_endtool_ai()` | 엔드툴 AI 데이터 |
| `get_endtool_ao()` | 엔드툴 AO 데이터 |
| `set_endtool_ao(end_ao_signal_list)` | 엔드툴 AO 데이터 |
| `get_device_info()` | 장치 정보 |
| `get_ft_sensor_data()` | 엔드툴 F/T 센서 데이터 |

### **`get_di()`**

디지털 입출력의 `DigitalState` 값은 `OFF(0)`, `ON(1)`, `UNUSED(2)` 세 가지의 상태를 나타냅니다.

```python
from neuromeka import DigitalState
DigitalState.ON
```

```yaml
1
```

입출력 데이터는 모두 `dict` 타입으로 반환되며 `address`는 IO 채널의 주소, `state`는 `DigitalState` 상태를 나타냅니다.

```python
indy.get_di()
```

```yaml
{
  'signals': [
    ...
    {'address': 7, 'state': 2},
    {'address': 8, 'state': 2},
    {'address': 9, 'state': 2},
    {'address': 10, 'state': 2},
    {'address': 11, 'state': 2},
    ...
  ]
}
```

### **`get_do()`, `set_do()`**

`set_do`와 같이 출력값을 인가하기 위해서는 아래 예제 코드와 같이 `dict` 타입을 인수로 주어야 합니다.

```python
from neuromeka import DigitalState

# address 1의 상태를 ON으로 변경
signal = [{'address': 1, 'state': DigitalState.ON}]
indy.set_do(signal)

# 변경 후 DO 상태 확인
indy.get_do()
```

```yaml
{
 'signals': [
  ...,
  {'address': 1, 'state': 1},
  ...
 ]
}
```

```python
# address 1을 OFF 상태로,
# address 5을 ON 상태로,
# address 9을 ON 상태로 동시 변경
signal = [{'address': 1, 'state': DigitalState.OFF},
         {'address': 5, 'state': DigitalState.ON},
         {'address': 9, 'state': DigitalState.ON}]
indy.set_do(signal)

# 변경 후 DO 상태 확인
indy.get_do()
```

```yaml
{
 'signals': [
  ...,
  {'address': 1, 'state': 0},
  ...
  {'address': 5, 'state': 1},
  ...
  {'address': 9, 'state': 1},
  ...
 ]
}
```

### **`get_ai()`**

```python
indy.get_ai()
```

```yaml
{
  'signals': [
    {'address': 0, 'voltage': 0},
    {'address': 1, 'voltage': 0},
    {'address': 2, 'voltage': 0},
    {'address': 3, 'voltage': 0},
    {'address': 4, 'voltage': 0},
    {'address': 5, 'voltage': 0},
    {'address': 6, 'voltage': 0},
    {'address': 7, 'voltage': 0}
  ]
}
```

- 컨트롤박스의 IO보드에는 2새의 AI 채널이 있으며 이는 각각 `address` 0과 1에 할당됩니다. 나머지 채널은 예비입니다.

### **`get_ao()`, `set_ao()`**

```python
# address 0의 아날로그 출력을 7로, address 1의 출력을 2로 변경
signal = [{'address': 0, 'voltage': 7},
         {'address': 1, 'voltage': 2}]
indy.set_ao(signal)

# 변경 후 AO 상태 확인
indy.get_ao()
```

```yaml
{
 'signals': [{'voltage': 7, 'address': 0},
  {'address': 1, 'voltage': 2},
  {'address': 2, 'voltage': 0},
  {'address': 3, 'voltage': 0},
  {'address': 4, 'voltage': 0},
  {'address': 5, 'voltage': 0},
  {'address': 6, 'voltage': 0},
  {'address': 7, 'voltage': 0}]
}
```

### **`get_endtool_di()`**

엔드툴포트의 디지털출력은 **`EndtoolState`** 클래스의 아래 상태로 정의가 됩니다. `UNUSED(0)`, `HIGH_PNP(2)`, `HIGH_NPN(1)`, `LOW_NPN(-1)`, `LOW_PNP(-2)`

```python
from neuromeka import EndtoolState
EndtoolState.HIGH_PNP
```

```yaml
2
```

```python
indy.get_endtool_di()
```

```yaml
{'signals': [{'port': 'A', 'states': [0, 0]},
  {'port': 'B', 'states': [0, 0]}]}
```

### **`set_endtool_do()`**, **`get_endtool_do()`**

RevC 엔드툴보드의 경우 하나의 C포트만 존재하며 아래와 같이 사용할 수 있습니다.

```python
from neuromeka import EndtoolState

signal = [{'port': 'C', 'states': [EndtoolState.HIGH_PNP]}]
indy.set_endtool_do(signal)

indy.get_endtool_do()
```

```yaml
{ 'signals': [{'port': 'C', 'states': [2]}] }
```

RevE 엔드툴보드의 경우 A포트, B포트 두 가지 엔드툴포트가 존재하며, 아래와 같이 사용할 수 있습니다.

```python
from neuromeka import EndtoolState

signal = [{'port': 'A', 'states': [EndtoolState.HIGH_PNP, EndtoolState.HIGH_PNP]},
         {'port': 'B', 'states': [EndtoolState.HIGH_NPN, EndtoolState.HIGH_NPN]}]
indy.set_endtool_do(signal)

indy.get_endtool_do()
```

```yaml
{'signals': [{'port': 'A', 'states': [2, 2]},
  {'port': 'B', 'states': [1, 1]}]}
```

### **`get_endtool_ai()`**

RevE 엔드툴보드에서만 사용 가능합니다.<br> RevE 엔드툴보드에는 2개의 AI 채널이 있으며 이는 각각 `address` 0과 1에 할당됩니다. 나머지 채널은 예비입니다.

```python
indy.get_endtool_ai()
```

```yaml
{'signals': [{'address': 0, 'voltage': 0},
  {'address': 1, 'voltage': 0},
  {'address': 2, 'voltage': 0},
  {'address': 3, 'voltage': 0},
  {'address': 4, 'voltage': 0},
  {'address': 5, 'voltage': 0},
  {'address': 6, 'voltage': 0},
  {'address': 7, 'voltage': 0}]}
```

### **`set_endtool_ao()`**, **`get_endtool_ao()`**

RevE 엔드툴보드에서만 사용 가능합니다.<br> RevE 엔드툴보드에는 2개의 AO 채널이 있으며 이는 각각 `address` 0과 1에 할당됩니다. 나머지 채널은 예비입니다.

```python
signal = [{'address': 0, 'voltage': 10},{'address': 1, 'voltage': 5}]
indy.set_endtool_ao(signal)

indy.get_endtool_ao()
```

```yaml
{'signals': [{'address': 0, 'voltage': 10},{'address': 1, 'voltage': 5}]}
```

### **`get_device_info()`**

```python
indy.get_device_info()
```

```yaml
{
 'num_joints': 6,
 'robot_serial': 'Robot-151',
 ...
 'controller_detail': ''
}
```

### **`get_ft_sensor_data()`**

```python
indy.get_ft_sensor_data()
```

```yaml
{'ft_Fx': 0.0,
 'ft_Fy': 0.0,
 'ft_Fz': 0.0,
 'ft_Tx': 0.0,
 'ft_Ty': 0.0,
 'ft_Tz': 0.0}
```

## 모션 명령 함수

모션 명령 함수는 로봇의 모션 제어에 관련된 다양한 작업을 수행합니다. 예를 들어, `stop_motion` 함수는 로봇의 모션을 정지 카테고리에 따라 멈추도록 합니다. `movej`, `movel`, `movec` 함수는 관절 이동, 선형 이동, 원호 이동을 수행할 때 사용되며, 각각의 함수는 이동할 위치, 속도 비율, 가속도 비율, 이동 시간, 그리고 다양한 이동 조건을 설정할 수 있습니다.

| Function | Description |
| --- | --- |
| `stop_motion(stop_category)` | 지정된 방식의 정지 카테고리에 따라 모션을 정지 |
| `move_home()` | 지정된 홈 위치로 로봇을 관절이동 |
| `movej(jtarget, blending_type, base_type, blending_radius, vel_ratio, acc_ratio, post_condition, teaching_mode)` | 지정된 관절 목표위치로 로봇을 이동 |
| `movej_time(jtarget, blending_type, base_type, blending_radius, move_time, post_condition)` | 지정된 시간 동안 관절 목표위치로 로봇을 이동 |
| `movel(ttarget, blending_type, base_type, blending_radius, vel_ratio, acc_ratio, post_condition, teaching_mode)` | 지정된 작업공간 목표 위치로 로봇을 선형 이동 |
| `movel_time(ttarget, blending_type, base_type, blending_radius, move_time, post_condition)` | 지정된 시간 동안 작업공간 목표 위치로 로봇을 선형 이동 |
| `movec(tpos0, tpos1, blending_type, base_type, angle, setting_type, move_type, blending_radius, vel_ratio, acc_ratio, post_condition, teaching_mode)` | 로봇의 현재 위치가 입력된 두 작업공간 위치 tpos0, tpos1를 지나는 원호를 따라 로봇을 이동 |
| `movec_time(tpos0, tpos1, blending_type, base_type, angle , setting_type, move_type, blending_radius, move_time, post_condition)` | 지정된 시간동안 로봇의 현재 위치가 입력된 두 작업공간 위치 tpos0, tpos1를 지나는 원호를 따라 로봇을 이동 |
| `move_gcode(gcode_file, is_smooth_mode, smooth_radius, vel_ratio, acc_ratio)` | 입력된 gcode 파일을 따라 로봇을 이동 |
| `add_joint_waypoint(jpos)` `get_joint_waypoint()` `clear_joint_waypoint()` `move_joint_waypoint(move_time)` | joint waypoints의 집합을 따라 로봇을 이동 |
| `add_task_waypoint(tpos)` `get_task_waypoint()` `clear_task_waypoint()` `move_task_waypoint(move_time)` | task waypoints의 집합을 따라 로봇을 이동 |
| `move_joint_traj(q_list, qdot_list, qddot_list)` | 로봇의 제어 주기에 대한 관절공간의 위치-속도-가속도를 한번에 입력받고 입력된 궤적을 따라 로봇을 이동 |
| `move_task_traj(p_list, pdot_list, pddot_list)` | 로봇의 제어 주기에 대한 작업공간의 위치-속도-가속도를 한번에 입력받고 입력된 궤적을 따라 로봇을 이동 |

Warning

모션 명령을 경우 명령이 성공적으로 인가되면 로봇이 즉각적으로 움직이기 됩니다. 콘티를 이용하여 로봇을 움직일 때에는 사용자가 터치를 누르는 동안만 로봇이 움직이지만 API 사용시에는 프로그램 명령을 통해 움직이기 때문에 항상 주변에 충돌이 발생할 만한 물건들을 치운 후 조심해서 사용해주시기 바랍니다. 특히 속도, 가속도 설정을 높게 할 경우 예상보다 로봇이 빠르게 움직일 수 있으므로 항상 안전에 유의하시기 바랍니다.

### **`stop_motion(stop_category)`**

`stop_category`의 값에 따라서 카테고리 0 정지, 카테고리 1 정지, 카테고리 2 정지를 선택할 수 있습니다. **`StopCategory`** 클래스에 정지 카테고리 `CAT0(0)`, `CAT1(1)`, `CAT2(2)`가 정의되어 있습니다.

```python
from neuromeka import StopCategory
indy.stop_motion(StopCategory.CAT2)
```

- **`StopCategory`**
  - `CAT0`: 정지카테고리 0 (즉시 전원 차단)으로 로봇 정지
  - `CAT1`: 정지카테고리 1 (모션 정지 후 전원 차단)로 로봇 정지
  - `CAT2`: 정지카테고리 2 (모션 정지)로 로봇 정지

### **`move_home()`**

`move_home`은 지정된 홈 위치로 관절 이동을 수행하는 명령입니다.

```python
indy.move_home()
```

### **`movej(...)`**

`movej`는 관절 이동 명령입니다. 아래 예제에서 `target_pos`는 `list` 값으로 단위는 degree 단위이며 입력된 목표 관절 위치로 로봇이 이동합니다.

```python
target_pos = [0, 0, -90, 0, -90, 0]
indy.movej(jtarget=target_pos)
```

**속도/가속도 설정**

`vel_ratio`와 `acc_ratio`를 통해 로봇의 속도, 가속도를 조절할 수 있습니다.

```python
target_pos = [50, 0, -90, 0, -90, 0]
indy.movej(jtarget=target_pos, vel_ratio=100, acc_ratio=300)
```

- `vel_ratio`: 로봇 이동 시 등속모드에서의 속도를 나타냅니다. 0-100 (%)의 값을 입력할 수 있으며, 100%는 로봇의 최대 관절속도를 나타냅니다 (예. 인디7의 경우 180deg/s).
- `acc_ratio`: 로봇 이동 시 가속도를 나타내며 `vel_ratio`의 배수로 나타냅니다. 0-900 (%)의 값을 입력할 수 있으며 300%를 입력할 경우 설정된 `vel_ratio`의 3배의 가속도로 이동하게 됩니다.

**절대위치/상대위치 관절이동**

`base_type`은 입력되는 목표 관절위치 `jtarget`에 대해 절대좌표 기준 또는 상대좌표 기준 중 하나로 설정하기 위한 값입니다.

```python
from neuromeka import JointBaseType

target_pos = [50, 0, -90, 0, -90, 0]
indy.movej(jtarget=target_pos, base_type=JointBaseType.ABSOLUTE)
```

```python
target_pos = [50, 0, 0, 0, 0, 0]
indy.movej(jtarget=target_pos, base_type=JointBaseType.RELATIVE)
```

- `JointBaseType`
  - `ABSOLUTE(0)`: 절대위치 `jtarget`으로 이동
  - `RELATIVE(1)`: 현재 로봇 위치 기준 상대위치 `jtarget`으로 이동

**조그모드 관절이동**

`teaching_mode`를 `True`로 설정하면 조그모드로 로봇을 움직이게 할 수 있습니다.

```python
target_pos = [100, 0, -90, 0, -90, 0]

for i in range(0,20):
    time.sleep(0.1)
    indy.movej(jtarget=target_pos, vel_ratio=50, acc_ratio=100, teaching_mode=True)
```

조그모션 이동을 실행할 때에는 `movej` 커맨드를 주기적으로 인가해주어야 로봇이 움직입니다.

**시간기반 이동**

`movej_time`은 지정된 `move_time`에 설정된 시간 (단위: sec)에 맞추어 관절이동을 수행하는 명령입니다.

```python
target_pos = [0, 0, -90, 0, -90, 0]
indy.movej_time(jtarget=target_pos, move_time=5)
```

### **`movel(...)`**

`movel`은 작업공간에서의 선형 위치이동 명령입니다. 아래 `target_pos`는 `list` 값으로 단위는 [mm, mm, mm, deg, deg, deg] 입니다.

```python
# 현재 작업공간 위치를 가져온 후 x 방향으로 100m 증가한 위치 계산
pos = indy.get_control_state()['p']
pos[0] += 100

indy.movel(pos)
```

`base_type`, `vel_ratio`, `acc_ratio`, `teaching_mode`은 앞서 `movej`에서 사용되는 인자와 동일하게 적용이 됩니다.

**절대위치/상대위치(참조좌표계, 툴좌표계) 관절이동**

`base_type`은 입력되는 목표 작업공간 위치 `ttarget`에 대해 절대좌표 기준 또는 상대좌표 기준 중 참조좌표계 또는 툴좌표계 기준을 설정하기 위한 값입니다.

```python
indy.movej(ttarget=target_pos, base_type=TaskBaseType.ABSOLUTE)
```

```python
from neuromeka import TaskBaseType

target_pos = [100, 0, 0, 0, 0, 0]

# 참조좌표계 기준으로 x 방향 100mm 만큼 상대위치 이동
indy.movel(ttarget=target_pos, base_type=TaskBaseType.RELATIVE)

# 툴좌표계 기준으로 x 방향 100mm 만큼 상대위치 이동
indy.movel(ttarget=target_pos, base_type=TaskBaseType.TCP)
```

- `TaskBaseType`
  - `ABSOLUTE(0)`: 절대위치 `ttarget`으로 이동
  - `RELATIVE(1)`: 현재 로봇 위치 기준 상대위치 `ttarget`만큼 참조좌표계 기준으로 로봇을 선형 이동
  - `TCP(2)`: 현재 로봇 위치 기준 상대위치 `ttarget`만큼 툴좌표계 기준으로 로봇을 선형 이동

**시간 기반 이동**

`movel_time`은 지정된 `move_time` 시간에 맞추어 작업공간에서의 선형 위치이동을 수행하는 명령입니다.

```python
pos = indy.get_control_state()['p']
pos[0] += 100

indy.movel_time(ttarget=pos, move_time=3)
```

### **`movec(...)`**

`movec`는 작업공간에서 원호 모션으로의 위치이동 명령입니다. 여기서 `tpos0`와 `tpos1`는 `list` 값으로 각각 via point와 end point를 나타냅니다.

```python
start_pos = [400.83, -61.27, 647.45, 0.07, 179.96, 8.78]
indy.movel(ttarget=start_pos)

via_point = [241.66, -51.11, 644.20, 0.0, 180.0, 23.36]
end_point = [401.53, -47.74, 647.50, 0.0, 180.0, 23.37]
indy.movec(tpos0=via_point, tpos1=end_point, angle=360)
```

- `angle`: 원호의 각도 설정 (단위 degree), 360으로 설정하면 원을 그리며 180으로 설정하면 반원을 그리며 720을 설정하면 원을 두 바퀴 그리게 됩니다.

**시간 기반 이동**

`movec_time`은 지정된 `move_time` 시간에 맞추어 작업공간에서의 원호 이동을 수행하는 명령입니다.

```python
indy.movec_time(tpos0=via_point, tpos1=end_point, angle=360, move_time=15.0)
```

### **`move_gcode(...)`**

`move_gcode` 함수는 G-code 파일을 기반으로 모션을 읽고 실행합니다. G-code는 CNC 및 로봇 어플리케이션에서 경로를 정의하는 데 널리 사용됩니다.

```text
gcode_path = "/path/to/gcode/<gcode file>"

indy.move_gcode(
    gcode_file=gcode_path,
    is_smooth_mode=False,
    smooth_radius=0.0,
    vel_ratio=15,
    acc_ratio=100
)
```

- **`gcode_file`**: G-code 파일의 경로를 설정합니다.
- **`is_smooth_mode`**: `True`일 경우, 경로 간의 부드러운 전환이 이루어집니다. (기본값: `False`)
- **`smooth_radius`**: 부드로운 모션을 만들기 위한 블랜딩 모션의 밀리미터 단위 반지름을 의미합니다.
- **`vel_ratio`**: 속도 비율로, 로봇의 최대 속도의 퍼센트로 나타냅니다. (기본값: `JogVelRatioDefault`)
  **`acc_ratio`**: 가속도 비율로, 속도 비율의 퍼센트로 나타냅니다. (기본값: `JogAccRatioDefault`)
  각 G-code 경로 간의 부드러운 모션을 지원합니다.
- `smooth_radius`을 사용해 블렌딩 반지름을 설정합니다.

### **관절 경유점, 작업 경유점을 이용한 Move**

#### Joint Waypoints

관절 경유점은 로봇의 각 관절 각도를 나타내며 여러 관절 경유점을 순차적으로 이동하도록 모션을 만들 수 있게 합니다.

`add_joint_waypoint(jpos)`는 관절 경유점을 경유점 리스트에 추가합니다. 경유점은 타겟 관절 위치를 벡터로 표현합니다. `jpos`: float으로 표현된 벡터이며 1번부터 6번 까지의 관절 각도를 deg 단위로 나타냅니다.

```python
jtarget_0 = [0,0,0,0,0,0]
jtarget_1 = [-44,25,-63,48,-7,-105]
jtarget_2 = [0,0,90,0,90,0]
jtarget_3 = [-145,31,-33,117,-7,-133]
jtarget_4 = [-90,-15,-90,0,-75,0]

indy.add_joint_waypoint(jtarget_0)
indy.add_joint_waypoint(jtarget_1)
indy.add_joint_waypoint(jtarget_2)
indy.add_joint_waypoint(jtarget_3)
indy.add_joint_waypoint(jtarget_4)
```

`get_joint_waypoint()` 현재 경유점 리스트에 저장된 관절 경유점 값을 반환 받을 수 있습니다.

```python
indy.get_joint_waypoint()
```

`clear_joint_waypoint()` 저장된 경유점 리스트를 리셋합니다.

```python
indy.clear_joint_waypoint()
```

`move_joint_waypoint(move_time)` 경유점 리스트에 저장된 관절 경유점을 따라 순차적으로 로봇이 이동합니다. `move_time`: (옵션) 각 경유점 간의 이동시간을 설정할 수 있습니다.

```python
indy.move_joint_waypoint()
```

```python
indy.move_joint_waypoint(move_time=3)
```

#### Task Waypoints

작업 경유점은 로봇의 작업공간 상의 위치와 자세를 나타내며 여러 작업 경유점을 순차적으로 이동하도록 모션을 만들 수 있게 합니다.

`add_task_waypoint(tpos)`는 작업 경유점을 경유점 리스트에 추가합니다. 경유점은 타겟 작업 위치를 벡터로 표현합니다. `tpos`: float으로 표현된 벡터이며 x, y, z 위치와 말단의 u, v, w 방향 각도를 나타냅니다.

```python
ttarget_0 = [400, -50, 650, 0, 180, 23]
ttarget_1 = [300, -50, 650, 0, 180, 23]
ttarget_2 = [300, -50, 550, 0, 180, 23]
ttarget_3 = [400, -50, 550, 0, 180, 23]
ttarget_4 = [400, -50, 650, 0, 180, 23]

indy.add_task_waypoint(ttarget_0)
indy.add_task_waypoint(ttarget_1)
indy.add_task_waypoint(ttarget_2)
indy.add_task_waypoint(ttarget_3)
indy.add_task_waypoint(ttarget_4)
```

`get_task_waypoint()` 현재 경유점 리스트에 저장된 작업 경유점 값을 반환 받을 수 있습니다.

```python
indy.get_task_waypoint()
```

`clear_task_waypoint()` 저장된 작업 경유점 리스트를 리셋합니다.

```python
indy.clear_task_waypoint()
```

`move_task_waypoint(move_time)` 경유점 리스트에 저장된 경유점을 따라 순차적으로 로봇이 이동합니다. `move_time`: (옵션) 각 경유점 간의 이동시간을 설정할 수 있습니다.

```python
indy.move_task_waypoint()
```

```python
indy.move_task_waypoint(move_time=1.5)
```

### 비동기 모션

로봇 모션 명령 수행 시 `blending_type` 설정을 통해 비동기 모션을 수행할 수 있습니다. 모션을 다음 모션으로 갈아타기 (Override)하거나, 중첩하기 (Duplicate)할 수 있습니다.

```python
# 일반적인 동기모션
import time

target_pos1 = [400, -50, 650, 0, 180, 23]
target_pos2 = [300, -50, 650, 0, 180, 23]
target_pos3 = [300, -50, 550, 0, 180, 23]

indy.movel(target_pos1)
time.sleep(1)

indy.movel(target_pos2)
indy.movel(target_pos3)
```

```python
from neuromeka import BlendingType

# Duplicate 예제
indy.movel(target_pos1)
time.sleep(1)

indy.movel(target_pos2, blending_type=BlendingType.DUPLICATE)
time.sleep(0.5)
indy.movel(target_pos3)
```

```python
# Override 예제
indy.movel(target_pos1)
time.sleep(1)

indy.movel(target_pos2, blending_type=BlendingType.OVERRIDE)
time.sleep(0.5)
indy.movel(target_pos3)
```

- **`BlendingType`**
  - `NONE(0)`: 비동기모션을 지정하지 않음 (동기모션 수행)
  - `OVERRIDE(1)`: 갈아타기 비동기모션 수행
  - `DUPLICATE(2)`: 중첩하기 비동기모션 수행

### **Waiting 함수**

**Wait IO**: 특정 디지털 또는 아날로그 I/O 신호가 주어진 조건과 일치할 때까지 대기합니다.<br> **Wait Time**: 첫 모션 명령이 입력된 후 특정 시간 동안 대기합니다.<br> **Wait Progress**: 특정 진행 상태에 도달할 때까지 대기합니다.<br> **Wait Radius**: 지정된 반경 내에서 움직임이 완료될 때까지 대기합니다.<br> **Wait Traj**: 경로 이동이 완료될 때까지 대기합니다.<br> - **`WaitTraj 조건`**<br> - `TRAJ_STARTED(0)`: 경로 이동이 막 시작되었음<br> - `TRAJ_ACC_DONE(1)`: 경로의 가속 구간이 완료되었음<br> - `TRAJ_CRZ_DONE(2)`: 경로의 순항 구간(일정 속도 구간)이 완료되었음<br> - `TRAJ_DEC_DONE(3)`: 경로의 감속 구간이 완료되었음

```python
jtarget_0 = [0,0,0,0,0,0]
indy.movej(jtarget = jtarget_0, blending_type=1)

# indy.wait_time(1)
# indy.wait_radius(10)
# indy.wait_traj(1)
indy.wait_progress(15)

jtarget_1 = [0,0,-90,0,-90,0]
indy.movej(jtarget = jtarget_1, blending_type=1)
```

**Wait IO 사용 예제**

```python
di_signals = [{'address': 1, 'state': True}]

indy.wait_io(
    di_signal_list=di_signals,
    do_signal_list=[],
    end_di_signal_list=[],
    end_do_signal_list=[],
    conjunction=0
)
```

### 궤적 운동

`move_joint_traj`는 관절 공간 궤적 이동 명령입니다. 아래에서 `q_list`, `qdot_list`, `qddot_list`는 라디안 단위의 관절 위치, 속도 및 가속도의 `list` 값입니다. 궤적 사이의 시간 간격은 제어 주기이며 기본적으로 250us입니다.

```python
# Get current Q
q_cur_deg = indydcp3.get_control_data()['q']

# Convert to rad
q_cur_rad = np.deg2rad(q_cur_deg)

# sin path
magitude = np.pi/18
traj_time=5

traj_num =traj_time*freq
q_list = magitude * (0.5-0.5*np.cos(np.arange(traj_num) / (traj_num) * 2 * np.pi)).reshape((traj_num, -1)) + [q_cur_rad]*traj_num
qdot_list = np.pad((q_list[1:]-q_list[:-1])/dt, ((0,1),(0,0)))
qddot_list = np.pad((qdot_list[1:]-qdot_list[:-1])/dt, ((0,1),(0,0)))

# Move
indydcp3.move_joint_traj(q_list, qdot_list, qddot_list)
```

`move_task_traj`는 작업 공간 궤적 이동 명령입니다. 아래에서 `p_list`, `pdot_list`, `pddot_list`는 엔드툴 위치, 속도 및 가속도의 미터 및 라디안 단위의 `list` 값입니다. 궤적 사이의 시간 단계는 제어 기간이며 기본적으로 250us입니다.

```python
# Get current P
p_cur_mm_deg = indydcp3.get_control_data()['p']

# Convert to m, rad
p_cur_m_rad = p_cur_mm_deg
p_cur_m_rad[:3] = np.multiply(p_cur_mm_deg[:3], 1e-3)
p_cur_m_rad[3:] = np.deg2rad(p_cur_mm_deg[3:])

# sin path
magitude_disp = 0.1
magitude_rot = np.pi/18
traj_time=5

traj_num =traj_time*freq
p_list = np.array([p_cur_m_rad]*traj_num)
pdot_list = np.zeros_like(p_list)
pddot_list = np.zeros_like(p_list)
p_list[:,0] = magitude_disp * (0.5-0.5*np.cos(np.arange(traj_num) / (traj_num) * 2 * np.pi)) + p_list[:,0]
pdot_list[:,0] = np.pad((p_list[1:,0]-p_list[:-1,0])/dt, (0,1))
pddot_list[:,0] = np.pad((pdot_list[1:,0]-pdot_list[:-1,0])/dt, (0,1))

# Move
indydcp3.move_task_traj(p_list, pdot_list, pddot_list)
```

## 텔레오퍼레이션 관련 함수

텔레오퍼레이션 관련 함수는 사용자가 로봇을 원격 제어할 수 있도록 하는 기능을 제공합니다. 이 함수들을 통해 로봇의 모션을 실시간으로 조정하고, 다양한 조작 모드에서 로봇을 제어할 수 있습니다. `start_teleop` 함수를 사용하여 텔레오퍼레이션 모드를 시작하고, `stop_teleop` 함수로 모드를 종료할 수 있습니다. 또한, `movetelej_abs`/`movetelej_rel`와 `movetelel_abs`/`movetelel_rel` 함수를 사용하여 각각 관절 공간과 작업 공간에서의 로봇 움직임을 업데이트할 수 있습니다.

Note

텔레오퍼레이션 모션 이용 시 IndyDCP3를 통해 실시간으로 지속적 목표 위치를 업데이트하게 되면 로봇은 이를 스트리밍하여 즉각적이면서 스무스한 모션을 생성합니다. 기존 Motion 명령들 (`movej`, `movel`)은 목표 위치로의 경로 생성을 부드럽게 수행하지만 원격제어와 같은 즉각적인 반응을 할 수는 없습니다. 이 점이 텔레오퍼레이션 모션의 특징입니다.

| Function | Description |
| --- | --- |
| `start_teleop(method)` | 텔레오퍼레이션 모드 시작 |
| `stop_teleop()` | 현재 실행 중인 텔레오퍼레이션 모드 종료 |
| `movetelej_abs(jpos, vel_ratio, acc_ratio)` | 지정된 관절 위치로 로봇을 원격 제어 (절대좌표) |
| `movetelej_rel(jpos, vel_ratio, acc_ratio)` | 지정된 관절 위치로 로봇을 원격 제어 (상대좌표) |
| `movetelel_abs(tpos, vel_ratio, acc_ratio)` | 지정된 작업 공간 위치로 로봇을 원격 제어 (절대좌표) |
| `movetelel_rel(tpos, vel_ratio, acc_ratio)` | 지정된 작업 공간 위치로 로봇을 원격 제어 (상대좌표) |
| `get_teleop_device()` | 현재 연결된 텔레오퍼레이션 장치에 대한 정보를 가져옵니다. |
| `get_teleop_state()` | 현재 텔레오퍼레이션 상태를 가져옵니다. |
| `connect_teleop_device(name, type, ip, port)` | 지정된 매개변수로 텔레오퍼레이션 장치에 연결합니다. |
| `disconnect_teleop_device()` | 현재 연결된 텔레오퍼레이션 장치의 연결을 해제합니다. |
| `read_teleop_input()` | 텔레오퍼레이션 장치에서 현재 입력 값을 읽어옵니다. |
| `get_tele_file_list()` | 저장된 텔레오퍼레이션 모션 파일 목록을 가져옵니다. |
| `save_tele_motion(name)` | 현재 텔레오퍼레이션 모션을 지정된 이름으로 저장합니다. |
| `load_tele_motion(name)` | 저장된 텔레오퍼레이션 모션을 이름으로 불러옵니다. |
| `delete_tele_motion(name)` | 저장된 텔레오퍼레이션 모션을 이름으로 삭제합니다. |
| `enable_tele_key(enable)` | 텔레오퍼레이션 키 입력을 활성화하거나 비활성화합니다. |
| `set_play_rate(rate)` | 텔레오퍼레이션 모션 재생 속도를 설정합니다. |
| `get_play_rate()` | 텔레오퍼레이션 모션 재생의 현재 재생 속도를 가져옵니다. |

### **`start_teleop(method)`, `stop_teleop()`**

```python
from neuromeka import JointTeleopType, TaskTeleopType

indy.start_teleop(method=JointTeleopType.RELATIVE)

(...)

indy.stop_teleop()
```

**`JointTeleopType`**
  - `ABSOLUTE`: 관절 절대위치를 타겟으로 움직이도록 설정. 이 설정에서는 `movetelej_abs` 함수만 호출 할 수 있음.
  - `RELATIVE`: 관절 상대위치 (`start_teleop`을 실행한 시점에서의 로봇 위치가 기준)를 타겟으로 움직이도록 설정. 이 설정에서는 `movetelej_rel` 함수만 호출 할 수 있음.
  **`TaskTeleopType`**
  - `ABSOLUTE`: 작업공간 절대위치를 타겟으로 움직이도록 설정. 이 설정에서는 `movetelel_abs` 함수만 호출 할 수 있음.
  - `RELATIVE`: 작업공간 상대위치 (`start_teleop`을 실행한 시점에서의 로봇 위치가 기준)를 타겟으로 움직이도록 설정. 이 설정에서는 `movetelel_rel` 함수만 호출 할 수 있음.

### **`movetelej_rel(jpos, vel_ratio, acc_ratio)`**

```python
indy.start_teleop(method=JointTeleopType.RELATIVE)
indy.movetelej_rel(jpos=[10, 0, 0, 0, 0, 0], vel_ratio=1.0, acc_ratio=1.0)

(...)
indy.stop_teleop()
```

- jpos: 목표 관절 위치
- vel_ratio: 속도 비율 (0 - 1)
- acc_ratio: 가속도 비율 (0 - 1)

### **`movetelel_rel(tpos, vel_ratio, acc_ratio)`**

```python
indy.start_teleop(method=TaskTeleopType.RELATIVE)

# x 방향으로 10mm 만큼 이동
indy.movetelel_rel(tpos=[10, 0, 0, 0, 0, 0], vel_ratio=0.5, acc_ratio=1.0)

(...)
indy.stop_teleop()
```

### **`get_teleop_device()`**

현재 연결된 텔레오퍼레이션 장치에 대한 정보를 가져옵니다.

```python
teleop_device_info = indy.get_teleop_device()
print(teleop_device_info)
```

### **`get_teleop_state()`**

현재 텔레오퍼레이션 상태를 가져옵니다.

```python
teleop_state = indy.get_teleop_state()
print(teleop_state)
```

### **`connect_teleop_device(name, type, ip, port)`**

지정된 매개변수로 텔레오퍼레이션 장치에 연결합니다.

```python
indy.connect_teleop_device(
    name="TeleOpDevice1",
    type=control_msgs.TeleOpDevice.JOYSTICK,
    ip="192.168.0.2",
    port=5555
)
```

- **`name`**: 텔레오퍼레이션 장치의 이름
- **`type`**: 텔레오퍼레이션 장치의 종류(e.g., `JOYSTICK`, `VR_CONTROLLER`)
- **`ip`**: 텔레오퍼레이션 장치의 IP 주소
- **`port`**: 텔레오퍼레이션 장치의 통신 Port

### **`disconnect_teleop_device()`**

현재 연결된 텔레오퍼레이션 장치의 연결을 해제합니다.

```python
indy.disconnect_teleop_device()
```

### **`read_teleop_input()`**

텔레오퍼레이션 장치에서 현재 입력 값을 읽어옵니다.

```python
teleop_input = indy.read_teleop_input()
print(teleop_input)
```

### **`get_tele_file_list()`**

저장된 텔레오퍼레이션 모션 파일 목록을 가져옵니다.

```python
tele_file_list = indy.get_tele_file_list()
print(tele_file_list)
```

### **`save_tele_motion(name)`**

현재 텔레오퍼레이션 모션을 지정된 이름으로 저장합니다.

```python
indy.save_tele_motion(name="Motion1")
```

- **`name`**: 저장할 텔레오퍼레이션 모션의 이름.

### **`load_tele_motion(name)`**

저장된 텔레오퍼레이션 모션을 이름으로 불러옵니다.

```python
indy.load_tele_motion(name="Motion1")
```

- **`name`**: 저장된 텔레오퍼레이션 모션 중 불러올 모션의 이름

### **`delete_tele_motion(name)`**

저장된 텔레오퍼레이션 모션을 이름으로 삭제합니다.

```python
indy.delete_tele_motion(name="Motion1")
```

- **`name`**: 저장된 텔레오퍼레이션 모션 중 삭제할 모션의 이름

### **`enable_tele_key(enable)`**

텔레오퍼레이션 키 입력을 활성화하거나 비활성화합니다.

```python
# Enable teleoperation key input
indy.enable_tele_key(enable=True)

# Disable teleoperation key input
indy.enable_tele_key(enable=False)
```

- **`enable`**: Boolen 값:
  - `True`: 텔레오퍼레이션 키 입력 활성화.
  - `False`: 텔레오퍼레이션 키 입력 비활성화.

### **`set_play_rate(rate)`**

텔레오퍼레이션 모션 재생 속도를 설정합니다.

```python
indy.set_play_rate(rate=1.5)
```

- **`rate`**: 모션 재생 속도 비율을 나타내는 float 값.
  - `1.0`: 보통 속도.
  - `1.0`보다 높을 경우: 더 빠른 모션 재생.
  - `1.0`보다 낮을 경우: 더 느린 모션 재생.

### **`get_play_rate()`**

텔레오퍼레이션 모션 재생의 현재 재생 속도를 가져옵니다.

```python
play_rate = indy.get_play_rate()
print(play_rate)
```

## 변수 (Variable)

**Indy Framework**에서는 Conty 및 API와의 연동을 위한 5가지 타입의 변수를 제공합니다. 이 변수들은 **Conty** 와 **Indy API** 모두에서 접근이 가능하며 읽기와 쓰기가 가능합니다. 이를 통해 로봇을 프로그래밍하는 **Conty**와 외부에서 **Indy API**를 사용하는 장치 간의 변수 교환을 통한 연동이 가능합니다. 변수 활용을 통해 외부 장치와 다양한 로직을 구성할 수 있습니다.

제공되는 변수 타입 다섯가지는 아래와 같습니다.

- Bool 타입, Integer 타입, Float 타입, JPos 타입 (관절공간의 각 관절 각도 변수), TPos 타입 (작업공간의 작업공간 좌표 변수)

| Function | Description |
| --- | --- |
| `get_bool_variable()` | Bool 타입 변수의 주소, 값 `list` |
| `get_int_variable()` | Integer 타입 변수의 주소, 값 `list` |
| `get_float_variable()` | Float 타입 변수의 주소, 값 `list` |
| `get_jpos_variable()` | JPos 타입 변수의 주소, 값 `list` |
| `get_tpos_variable()` | TPos 타입 변수의 주소, 값 `list` |
| `set_bool_variable(bool_variables)` | Bool 타입 변수의 주소, 값 `list` |
| `set_int_variable(int_variables)` | Integer 타입 변수의 주소, 값 `list` |
| `set_float_variable(float_variables)` | Float 타입 변수의 주소, 값 `list` |
| `set_jpos_variable(jpos_variables)` | JPos 타입 변수의 주소, 값 `list` |
| `set_tpos_variable(tpos_variables)` | TPos 타입 변수의 주소, 값 `list` |

### **`get_bool_variable()`**

```python
indy.get_bool_variable()
```

```yaml
{'variables': [{'addr': 100, 'value': True}, {'addr': 150, 'value': False}]}
```

### **`set_bool_variable(bool_variables)`**

```python
# bool 변수 주소 100에 값 True 할당
indy.set_bool_variable([{'addr': 100, 'value': True}])
# bool 변수 주소 150에 값 False 할당
indy.set_bool_variable([{'addr': 150, 'value': False}])
```

### **`get_int_variable()`**

```python
indy.get_int_variable()
```

```yaml
{'variables': [{'addr': 300, 'value': '0'}, {'addr': 10, 'value': '20'}, {'addr': 15, 'value': '5'}]}
```

### **`set_int_variable(int_variables)`**

```python
# int 변수 주소 10에 값 20 할당
int_variables = [{'addr': 10, 'value': 20}]
indy.set_int_variable(int_variables=int_variables)
# int 변수 주소 15에 값 5 할당
int_variables = [{'addr': 15, 'value': 5}]
indy.set_int_variable(int_variables=int_variables)
```

### **`get_float_variable()`**

```python
indy.get_float_variable()
```

```yaml
{
  'variables': [
    {'addr': 10, 'value': -23.3},
    {'addr': 15, 'value': 55.12}
  ]
}
```

**`set_float_variable()`**

```python
# float 변수 주소 10에 값 -23.3 할당
indy.set_float_variable([{'addr': 10, 'value': -23.3}])
# float 변수 주소 15에 값 55.12 할당
indy.set_float_variable([{'addr': 15, 'value': 55.12}])
```

### **`get_jpos_variable()`**

```python
indy.get_jpos_variable()
```

```yaml
[{'jpos': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'addr': 0},
 {'addr': 200, 'jpos': [10.0, 10.0, 10.0, 10.0, 10.0, 10.0]}]
```

**`set_jpos_variable()` 예시**

```python
# jpos 변수 주소 0에 값 [0,0,0,0,0,0] 할당
indy.set_jpos_variable([{'addr': 0, 'jpos': [0,0,0,0,0,0]}])
# jpos 변수 주소 200에 값 [10,10,10,10,10,10] 할당
indy.set_jpos_variable([{'addr': 200, 'jpos': [10,10,10,10,10,10]}])
```

### **`get_tpos_variable()`**

```python
indy.get_tpos_variable()
```

```yaml
{
  'variables': [
    {'addr': 10, 'tpos': [100.0, 100.0, 200.0, 0.0, 180.0, 0.0]},
    {'addr': 20, 'tpos': [100.0, 100.0, 350.0, 0.0, 180.0, 0.0]}
  ]
}
```

### **`set_tpos_variable(tpos_variables)`**

```python
# tpos 변수 주소 10에 값 [100,100,200,0,180,0] 할당
indy.set_tpos_variable([{'addr': 10, 'tpos': [100,100,200,0,180,0]}])
# tpos 변수 주소 20에 값 [100,100,350,0,180,0] 할당
indy.set_tpos_variable([{'addr': 20, 'tpos': [100,100,350,0,180,0]}])
```

## 역기구학과 시뮬레이션 모드 관련 함수

| Function | Description |
| --- | --- |
| `inverse_kin(tpos, init_jpos)` | `tpos`: 목표 작업공간 위치, `init_jpos`: 초기 관절 위치 |
| `set_direct_teaching(enable)` | True/False 를 통해 직접교시 모드 활성/비활성화 |
| `set_simulation_mode(enable)` | True/False 를 통해 시뮬레이션 모드 활성/비활성화 |
| `recover()` | 로봇 에러 상태에서 복구 |

### **`inverse_kin(tpos, init_jpos)`**

작업공간 좌표로부터 해당 좌표에 도달 가능한 관절 위치를 계산하는 함수입니다. 초기 관절 위치를 기준으로 가장 가까운 해를 찾습니다. 아래의 예시는 현재 로봇의 관절각도를 `init_jpos`로, 현재 로봇의 작업공간 위치를 `tpos`로 하여 역기구학 연산을 하였을 때에 현재의 관절각도가 나오는지를 보여주는 예제입니다.

```python
tpos = indy.get_control_data()['p']
init_jpos = indy.get_control_data()['q']

print("Current tpos", tpos)
print("Current jpos", init_jpos)

indy.inverse_kin(tpos, init_jpos)
```

```yaml
Current tpos [299.6449, -107.58244, 1002.9704, 2.3324265, 84.555115, 16.708658]
Current jpos [21.618074, 13.531353, -64.26601, -12.834319, -34.454514, 10.170495]
{'jpos': [21.618074, 13.531353, -64.26601, -12.834319, -34.454514, 10.170495],
 'response': {'msg': 'InverseKinematics Success', 'code': '0'}}
```

-

tpos

: 목표 작업공간 위치 ([x, y, z, u, v, w] 형태)
-

init_jpos

: 초기 관절 위치
-

jpos

: 계산된 관절 위치의 리스트

### **`set_direct_teaching(enable)`**

```python
indy.set_direct_teaching(enable=True)

(...)

indy.set_direct_teaching(enable=False)
```

- **enable**: True (활성화) | False (비활성화)

### **`set_simulation_mode(enable)`**

시뮬레이션 모드를 설정하는 함수입니다. 이 모드가 활성화되면, 실제 로봇 대신 시뮬레이션된 로봇이 작동합니다.

```python
indy.set_simulation_mode(enable=True)

(...)

indy.set_simulation_mode(enable=False)
```

- **enable**: True (활성화) | False (비활성화)

### **`recover()`**

에러나 충돌 상황에서 로봇을 회복시키는 함수입니다. 로봇이 비정상적인 상태에 빠졌을 때, 이 함수를 호출하여 정상 상태로 복구시킬 수 있습니다.

```python
indy.recover()
```

## 프로그램 제어 관련 함수

IndyDCP3를 사용하여 로봇 프로그램의 재생, 일시 정지, 재개, 정지 등을 제어할 수 있습니다. 이 기능들을 통해 사용자는 프로그램의 실행 흐름을 유연하게 관리할 수 있습니다.

| Function | Description |
| --- | --- |
| `play_program(prog_name, prog_idx)` | 프로스램 시작, `prog_name`: 프로그램 파일 이름, `prog_idx`: 프로그램 인덱스 |
| `pause_program()` | 프로그램 일시정지 |
| `resume_program()` | 프로그램 재개 |
| `stop_program()` | 프로그램 정지 |

### **`play_program(prog_name, prog_idx)`**

지정된 이름 또는 인덱스의 프로그램을 재생합니다. 프로그램 이름과 인덱스 중 하나를 사용하여 특정 프로그램을 선택할 수 있습니다.

Note

프로그램은 **Conty**를 이용하여 사전 작성 후 저장을 해야 합니다.

```python
# 프로그램 파일 이름으로 재생
indy.play_program(prog_name='example_program.indy7v2.json')

# 프로그램 인덱스로 재생
indy.play_program(prog_idx=1)
```

- 프로그램 파일 이름으로 재생 시 프로그램 파일 경로 (STEP): ~/ProgramScripts
- 프로그램 인덱스로 재생 시 프로그램 파일 경로 (STEP): ~/ProgramScripts/index

### **`pause_program()`**

현재 실행 중인 프로그램을 일시 정지합니다.

```python
indy.pause_program()
```

### **`resume_program()`**

일시 정지된 프로그램을 다시 재개합니다. 프로그램의 실행을 일시정지 했다가 다시 시작할 필요가 있을 때 사용합니다.

```python
indy.resume_program()
```

### **`stop_program()`**

현재 실행 중인 프로그램을 정지합니다.

```python
indy.stop_program()
```

## IndySDK 사용

Indy SDK를 활성화하고 사용자 정의 제어 모드를 설정하기 위한 프로토콜 입니다.

| Function | Description |
| --- | --- |
| `activate_sdk()` | IndySDK 활성화 |
| `set_custom_control_mode()` | 사용자 컨트롤러 활성화/비활성화 모드 선택 |
| `get_custom_control_mode()` | 사용자 컨트롤러 모드 확인 |
| `set_custom_control_gain()` | 사용자 컨트롤러의 제어게인 설정 |
| `get_custom_control_gain()` | 사용자 컨트롤러의 제어게인 확인 |
| `set_joint_control_gain(kp, kv, kl2)` | Joint-Level 컨트롤러의 제어게인 설정 |
| `get_joint_control_gain()` | Joint-Level 컨트롤러의 제어게인 확인 |
| `set_task_control_gain(kp, kv, kl2)` | Task-Level 컨트롤러의 제어게인 설정 |
| `get_task_control_gain()` | Task-Level 컨트롤러의 제어게인 확인 |
| `set_impedance_control_gain(mass, damping, stiffness, kl2)` | 임피던스 제어게인 설정 |
| `get_impedance_control_gain()` | 현재 임피던스 제어게인 확인 |
| `set_force_control_gain(kp, kv, kl2, mass, damping, stiffness, kpf, kif)` | 힘 제어게인 설정 |
| `get_force_control_gain()` | 현재 힘 제어게인 확인 |

### **`activate_sdk()`**

IndySDK를 활성화하는 함수입니다. 매개변수는 아래와 같습니다.

```python
indy.activate_sdk(
license_key="345HW8PEQB35114AABS34U591366E134BW35AS83663AASB23ABS83481AA9DB33",
expire_date="2025-02-01"
)
```

- `license_key`: 발급받은 라이선스 키입니다.
- `expire_date`: 라이선스의 만료 날짜입니다. 포맷은 `YYYY-MM-DD`입니다.

`SDKLicenseResp` 객체를 반환하며, 다음 정보를 포함합니다.

- `activated`: 불리언 값으로, 활성화 상태를 나타냅니다.
- `response`: 튜플 `(code, msg)`로, 다음 값들을 포함할 수 있습니다.
  - `0, 'Activated'`: SDK가 활성화되었습니다.
  - `1, 'Invalid'`: 잘못된 키 또는 만료 날짜입니다.
  - `2, 'No Internet Connection'`: 라이선스 검증을 위해 인터넷 연결이 필요합니다.
  - `3, 'Expired'`: 라이선스가 만료되었습니다.
  - `4, 'HW_FAILURE'`: 하드웨어 ID 검증 실패입니다.

### **`set_custom_control_mode()`**

사용자 정의 제어 모드를 설정하는 함수입니다. 매개변수는 다음과 같습니다.

- `mode`:
  - `False (0)`: IndyFramework의 기본 컨트롤러가 사용됩니다.
  - `True (1)`: IndySDK를 통해 사용자가 빌드한 컴포넌트가 사용됩니다.

### **`get_custom_control_mode()`**

현재 설정된 사용자 정의 제어 모드를 확인하는 함수입니다. 현재 설정된 모드를 나타내는 객체를 반환합니다.

### **`set_custom_control_gain()`**

사용자 제어기의 게인을 설정하기 위한 함수입니다.

```python
# Default gain
gain0 = [100, 100, 100, 100, 100, 100]
gain1 = [20, 20, 20, 20, 20, 20]
gain2 = [800, 800, 600, 400, 400, 400]
gain3 = [100, 100, 100, 100, 100, 100]
gain4 = [20, 20, 20, 20, 20, 20]
gain5 = [800, 800, 600, 400, 400, 400]

indy.set_custom_control_gain(gain0=gain0, gain1=gain1, gain2=gain2,
                              gain3=gain3, gain4=gain4, gain5=gain5)
```

- `gain0`: 각 관절에 대한 gain0
- `gain1`: 각 관절에 대한 gain1
- `gain2`: 각 관절에 대한 gain2
- `gain3`: 각 관절에 대한 gain3
- `gain4`: 각 관절에 대한 gain4
- `gain5`: 각 관절에 대한 gain5

제어게인 변수는 `gain0`부터 `gain9` 까지 정의되어 있습니다.

Note

여기서 `gain0`부터 `gain9` 까지의 변수는 IndySDK에서 호출할 수 있는 gRPC 변수이며 실 사용 예시는 [IndySDK 저장소](https://gitlab.com/neuromeka-group/nrmkc/indysdk3)의 예제를 확인해주시기 바랍니다.

### **`get_custom_control_gain()`**

이 함수는 현재 사용자 정의 제어 게인 설정을 확인합니다.

```python
indy.get_custom_control_gain()
```

```yaml
{'gain0': [100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
 'gain1': [20.0, 20.0, 20.0, 20.0, 20.0, 20.0],
 'gain2': [800.0, 800.0, 600.0, 400.0, 400.0, 400.0],
 'gain3': [100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
 'gain4': [20.0, 20.0, 20.0, 20.0, 20.0, 20.0],
 'gain5': [800.0, 800.0, 600.0, 400.0, 400.0, 400.0],
 'gain6': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
 'gain7': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
 'gain8': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
 'gain9': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}
```

### **`set_joint_control_gain(kp, kv, kl2)`**

Joint-Level 컨트롤러의 제어게인을 설정합니다.

```python
indy.set_joint_control_gain(kp=[...], kv=[...], kl2=[...])
```

- **`kp`**: 각 관절의 비례 게인
- **`kv`**: 각 관절의 속도 게인
- **`kl2`**: 각 관절의 2차 게인

### **`get_joint_control_gain()`**

Joint-Level 컨트롤러의 제어게인을 확인합니다.

```python
joint_gains = indy.get_joint_control_gain()
print(joint_gains)
```

### **`set_task_control_gain(kp, kv, kl2)`**

Task-Level 컨트롤러의 제어게인을 설정합니다.

```python
indy.set_task_control_gain(kp=[...], kv=[...], kl2=[...])
```

- **`kp`**: 각 Task 좌표계의 비례 게인
- **`kv`**: 각 Task 좌표계의 속도 게인
- **`kl2`**: 각 Task 좌표계의 2차 게인

### **`get_task_control_gain()`**

Task-Level 컨트롤러의 제어게인을 확인합니다.

```python
task_gains = indy.get_task_control_gain()
print(task_gains)
```

### **`set_impedance_control_gain(mass, damping, stiffness, kl2)`**

임피던스 제어게인을 설정합니다.

```python
indy.set_impedance_control_gain(
    mass=[...],
    damping=[...],
    stiffness=[...],
    kl2=[...]
)
```

- **`mass`**: 각 Task 좌표계의 Inertial 게인
- **`damping`**: 각 Task 좌표계의 Damping 게인
- **`stiffness`**: 각 Task 좌표계의 Stiffness 게인
- **`kl2`**: 각 Task 좌표계의 2차 게인

### **`get_impedance_control_gain()`**

현재 임피던스 제어게인을 확인합니다.

```python
impedance_gains = indy.get_impedance_control_gain()
print(impedance_gains)
```

### **`set_force_control_gain(kp, kv, kl2, mass, damping, stiffness, kpf, kif)`**

힘 제어게인을 설정합니다.

```python
indy.set_force_control_gain(
    kp=[...],
    kv=[...],
    kl2=[...],
    mass=[...],
    damping=[...],
    stiffness=[...],
    kpf=[...],
    kif=[...]
)
```

- **`kp`**: 각 관절 또는 Task 좌표계의 비례 게인
- **`kv`**: 각 관절 또는 Task 좌표계의 속도 게인
- **`kl2`**: 각 관절 또는 Task 좌표계의 2차 게인
- **`mass`**: 각 Task 좌표계의 Inertial 게인
- **`damping`**: 각 Task 좌표계의 Damping 게인
- **`stiffness`**: 각 Task 좌표계의 Stiffness 게인
- **`kpf`**: 힘제어를 위한 비례 게인
- **`kif`**: 힘제어를 위한 적분 게인

### **`get_force_control_gain()`**

현재 힘 제어게인을 확인합니다.

```python
force_gains = indy.get_force_control_gain()
print(force_gains)
```

## 유틸리티 함수

이 섹션에서는 작업 효율성을 높이기 위한 필수 유틸리티 함수들을 설명합니다.

| Function | Description |
| --- | --- |
| `start_log()` | 실시간 데이터로깅 시작 |
| `end_log()` | 실시간 데이터로깅 종료 및 저장 |
| `wait_for_operation_state(op_state)` | 로봇이 특정 운영 상태에 도달할 때까지 대기 |
| `wait_for_motion_state(motion_state)` | 로봇이 특정 모션 상태에 도달할 때까지 대기 |
| `set_friction_comp_state(enable)` | 마찰 보상 활성화 / 비활성화 |
| `get_friction_comp_state()` | 마찰 보상의 현재 상태 불러오기 |
| `set_mount_pos(rot_y, rot_z)` | 로봇 베이스의 마운팅 각도 설정 |
| `get_mount_pos()` | 로봇 베이스의 현재 마운팅 각도 불러오기 |
| `set_brakes(brake_state_list)` | 각 모터의 브레이크 상태 설정 |
| `set_servo_all(enable)` | 모든 서보 활성화 / 비활성화 |
| `set_servo(index, enable)` | 특정 인덱스의 서보 활설화 / 비활성화 |
| `set_endtool_led_dim(led_dim)` | 엔드 이펙터의 LED 밝기 설정 |
| `execute_tool(name)` | 입력된 이름의 툴 함수 실행 |
| `get_el5001()` | EL5001 장치로부터 데이터 불러오기 |
| `get_el5101()` | EL5101 장치로부터 데이터 불러오기 |
| `get_brake_control_style()` | 현재 브레이크 제어 방법 불러오기 |
| `set_conveyor_name(name)` | 컨베이어의 이름 설정 |
| `set_conveyor_encoder(encoder_type, channel1, channel2, sample_num, mm_per_tick, vel_const_mmps, reversed)` | 컨베이어 엔코더의 환경설정 |
| `set_conveyor_trigger(trigger_type, channel, detect_rise)` | 컨베이어 트리거 설정 |
| `set_conveyor_offset(offset_mm)` | 컨베이어 작업의 offset 값 설정 (밀리미터 단위) |
| `set_conveyor_starting_pose(jpos, tpos)` | 컨베이어 작업의 시작 joint 및 task 위치 설정 |
| `set_conveyor_terminal_pose(jpos, tpos)` | 컨베이어 작업의 마지막 joint 및 task 위치 설정 |

### **`start_log()`**, **`end_log()`**

이 두 함수는 실시간 데이터 로깅에 사용됩니다. `start_log()` 호출과 동시에 메모리에 로봇의 데이터를 저장합니다. 이후 특정 시간이 지난 후 `end_log()`를 호출하면 메모리 로깅을 종료하고 이를 STEP 내에 파일로 작성합니다. 실시간 데이터 로깅 파일은 다음 경로에서 찾을 수 있습니다.

*/home/user/release/IndyDeployments/RTlog/RTLog.csv*

### **`wait_for_operation_state(op_state)`**

예를 들어, 로봇이 IDLE 상태에 도달할 때까지 기다리고 싶다면 (여기서 IDLE은 5로 정의됨), 다음과 같이 호출할 수 있습니다.

```python
IDLE = 5
indy.wait_for_operation_state(IDLE)
```

### **`wait_for_motion_state(motion_state)`**

- `motion_state`:
  - `is_target_reached` (목표 도달 여부)
  - `is_in_motion` (모션 진행 중)
  - `is_pausing` (일시 중지 상태)
  - `is_stopping` (정지 상태)
  - `has_motion` (모션 발생 여부)

예를 들어, 로봇의 모션이 완료될 때까지 기다리고 싶다면, 'is_target_reached' 상태를 사용하여 다음과 같이 호출할 수 있습니다.

```python
indy.wait_for_motion_state('is_target_reached')
```

### **`set_friction_comp_state(enable)`**

마찰 보상을 활성화 또는 비활성화합니다.

```python
indy.set_friction_comp_state(enable=True)
```

- **`enable`**: boolean 값:
  - `True`: 마찰 보상 활성화
  - `False`: 마찰 보상 비활성화

### **`get_friction_comp_state()`**

마찰 보상의 현재 상태를 불러옵니다.

```python
friction_state = indy.get_friction_comp_state()
print(friction_state)
```

### **`set_mount_pos(rot_y, rot_z)`**

로봇 베이스의 마운팅 각도를 설정합니다.

```python
indy.set_mount_pos(rot_y=5.0, rot_z=10.0)
```

- **`rot_y`**: Y축 방향 회전 각도 (degrees 단위)
- **`rot_z`**: Z축 방향 회전 각도 (degrees 단위)

### **`get_mount_pos()`**

로봇 베이스의 현재 마운팅 각도를 불러옵니다.

```python
mount_pos = indy.get_mount_pos()
print(mount_pos)
```

### **`set_brakes(brake_state_list)`**

각 모터의 브레이크 상태를 설정합니다.

```python
indy.set_brakes(brake_state_list=[True, False, True, True, False, True])
```

- **`brake_state_list`**: 각 모터의 브레이크 상태를 boolean 값의 list로 한번에 설정
  - `True`: 브레이크를 작동
  - `False`: 브레이크를 해제

### **`set_servo_all(enable)`**

모든 서보를 활성화 또는 비활성화합니다.

```python
indy.set_servo_all(enable=True)
```

- **`enable`**: boolean 값:
  - `True`: 모든 서보 활성화.
  - `False`: 모든 서보 비활성화.

### **`set_servo(index, enable)`**

특정 인덱스의 서보를 활설화 또는 비활성화합니다.

```python
indy.set_servo(index=3, enable=False)
```

- **`index`**: 해당 인덱스의 서보 활성화 / 비활성화 (정수).
- **`enable`**: boolean 값:
  - `True`: 특정 서보 활성화.
  - `False`: 특정 서보 비활성화.

### **`set_endtool_led_dim(led_dim)`**

엔드 이펙터 LED의 밝기를 설정합니다.

```python
indy.set_endtool_led_dim(led_dim=128)
```

- **`led_dim`**: LED 밝기를 나타내는 정수 값 (0-255).
  - `0`: LED 꺼짐
  - `255`: 최대 밝기

### **`execute_tool(name)`**

입력된 이름의 툴 함수를 실행합니다.

```python
indy.execute_tool(name="GripperOpen")
```

- **`name`**: string 타입으로 실행될 툴 함수의 이름을 설정

### **`get_el5001()`**

EL5001 장치로부터 데이터를 불러옵니다.

```python
el5001_data = indy.get_el5001()
print(el5001_data)
```

### **`get_el5101()`**

EL5101 장치로부터 데이터를 불러옵니다.

```python
el5101_data = indy.get_el5101()
print(el5101_data)
```

### **`get_brake_control_style()`**

현재 브레이크의 제어 방법을 불러옵니다.

```python
brake_control_style = indy.get_brake_control_style()
print(brake_control_style)
```

### **`set_conveyor_name(name)`**

컨베이어의 이름을 설정합니다.

```python
indy.set_conveyor_name(name="Conveyor1")
```

- **`name`**: string 타입으로 컨베이어의 이름을 설정

### **`set_conveyor_encoder(encoder_type, channel1, channel2, sample_num, mm_per_tick, vel_const_mmps, reversed)`**

컨베이어 엔코더의 파라미터를 설정합니다.

```python
indy.set_conveyor_encoder(
    encoder_type=1,
    channel1=0,
    channel2=1,
    sample_num=10,
    mm_per_tick=0.1,
    vel_const_mmps=500.0,
    reversed=False
)
```

- **`encoder_type`**: 엔코더의 타입.
- **`channel1`**: 엔코더의 첫번째 채널.
- **`channel2`**: 엔코더의 두번째 채널.
- **`sample_num`**: 위치 측정에서 평균을 계산하기 위한 샘플 수
- **`mm_per_tick`**: 엔코더 틱 당 밀리미터 값
- **`vel_const_mmps`**: 고정 속도 (mm/s 단위)
- **`reversed`**: 엔코더의 방향을 반전시키는 boolean 값

### **`set_conveyor_trigger(trigger_type, channel, detect_rise)`**

컨베이어 작업의 트리거를 설정합니다.

```python
indy.set_conveyor_trigger(
    trigger_type=2,
    channel=0,
    detect_rise=True
)
```

- **`trigger_type`**: 트리거의 타입
- **`channel`**: 트리거로 사용될 채널
- **`detect_rise`**: 신호의 상승 엣지(`True`) 또는 하강 엣지(`False`) 감지를 boolean으로 설정

### **`set_conveyor_offset(offset_mm)`**

컨베이어 작업에 대해 밀리미터 단위의 offset 값을 설정합니다.

```python
indy.set_conveyor_offset(offset_mm=50.0)
```

- **`offset_mm`**: 밀리미터 단위의 offset 값.

### **`set_conveyor_starting_pose(jpos, tpos)`**

컨베이어 작업의 시작 joint 및 task 위치 설정합니다.

```python
indy.set_conveyor_starting_pose(
    jpos=[0, 0, 0, 0, 0, 0],
    tpos=[]
)
```

- **`jpos`**: 시작 자세에 대한 joint position 리스트
- **`tpos`**: 시작 자세에 대한 task position 리스트.

### **`set_conveyor_terminal_pose(jpos, tpos)`**

컨베이어 작업의 마지막 joint 및 task 위치 설정합니다.

```python
indy.set_conveyor_terminal_pose(
    jpos=[0, 0, -90, 0, -90, 0],
    tpos=[]
)
```

- **`jpos`**: 마지막 자세에 대한 joint position 리스트
- **`tpos`**: 마지막 자세에 대한 task position 리스트.

## 부록: HTML 주석에 포함된 로봇 설정 명령 관련 함수

## 로봇 설정 명령 관련 함수
로봇 설정 관련 함수를 통해 로봇의 다양한 전역 상태를 설정할 수 있고 현재의 설정 상태를 확인할 수 있습니다.

| Function | Argument | Return |
|--------|-----------|-------------|
| `get_home_pos()` | - | 로봇의 홈 위치 (관절각도) `list` |
| `set_home_pos(home_jpos)` | 로봇의 홈 위치 (관절각도) `list` | - |
| `get_ref_frame()` | `fpos: list` | 로봇의 참조 프레임을 설정합니다. |
| `set_ref_frame()` | `fpos: list` | 로봇의 참조 프레임을 설정합니다. |
| `set_ref_frame_planar()` | `fpos0: list`,

`fpos1: list`,

`fpos2: list` | 평면 참조 프레임을 설정합니다. |
| `set_tool_frame()` | `fpos: list` | 작업공간의 프레임 위치를 설정합니다. |
| `set_speed_ratio()` | `speed_ratio: int` | 로봇의 동작 속도 비율을 설정합니다. |
| `set_auto_servo_Off()` | `time: float`,

`enable: bool` | 자동 서보 오프 기능을 설정합니다. |
| `set_coll_sens_level()` | `level: int` | 충돌 감지 시의 감도 레벨을 설정합니다. |
| `get_coll_sens_level()`        | -                      | 충돌 감지 시의 감도 레벨을 조회합니다. |
| `set_safety_limits()` | `power_limit: float`,

`tcp_force_limit: float`,

`tcp_speed_limit: float` | 로봇의 안전한 움직임을 위한 제한 사항을 설정합니다. |
| `get_home_pos()` | - | 설정된 홈 위치를 조회합니다. |
| `get_auto_servo_off()` | - | 설정된 자동 서보 오프 설정을 조회합니다. |
| `get_coll_sens_level()` | - | 설정된 충돌 감도 레벨을 조회합니다. |
| `get_safety_limits()` | - | 설정된 안전 제한을 조회합니다. |

### 홈 위치 설정
#### `set_home_pos(), get_home_pos()` 예시
**Input:**

```python
home_jpos = [30, 0, 10, 0, 20, 0]
indydcp3.set_home_pos(home_jpos)
```

- **목적**: 로봇의 홈 위치를 설정합니다.
- **입력**: `home_jpos = [30, 0, 10, 0, 20, 0]` - 로봇의 홈 위치를 나타내는 관절 위치 배열입니다.
- **출력**: 성공적으로 설정 시 `{'code': '0', 'msg': ''}`
**Input:**

```python
indydcp3.get_home_pos()
```

**Output**

```python
{'jpos': [30.0, 0.0, 10.0, 0.0, 20.0, 0.0]}
```

- **목적**: 설정된 로봇의 홈 위치를 조회합니다.
- **출력**: 현재 설정된 홈 위치의 관절 값입니다.
### 프레임 설정
#### `set_ref_frame(), set_ref_frame_planar(), set_tool_frame()` 예시
**Input:**

```python
fpos = [0,0,0,0,0,0]
indydcp3.set_ref_frame(fpos)
```

- **목적**: 로봇의 참조 프레임을 설정합니다.
- **입력**: `fpos = [0,0,0,0,0,0]` - 참조 프레임 위치를 나타내는 배열입니다.
- **출력**: 성공적으로 설정 시 `{'code': '0', 'msg': ''}`
**Input:**

```python
fpos0 = [0,180,0]
fpos1 = [100,10,0]
fpos2 = [0,180,50]
indydcp3.set_ref_frame_planar(fpos0, fpos1, fpos2)
```

**Output**

```python
{'fpos': [0.0, 180.0, 0.0, -90.0, -180.0, 120.465546]}
```

- **목적**: 평면 참조 프레임을 설정합니다.
- **입력**: `fpos0`, `fpos1`, `fpos2` - 평면을 정의하는 세 점입니다.
- **출력**: 성공적으로 설정 시 설정된 평면 참조 프레임의 위치와 각도 정보입니다.
**Input:**

```python
fpos = [0,0,0,0,0,0]
indydcp3.set_tool_frame(fpos)
```

- **목적**: 툴 프레임 위치를 설정합니다.
- **입력**: `fpos = [0,0,0,0,0,0]` - 툴 프레임의 위치와 각도를 나타내는 배열입니다.
- **출력**: 성공적으로 설정 시 `{'code': '0', 'msg': ''}`
### 속도 비율 설정
#### `set_speed_ratio()` 예시
**Input:**

```python
indydcp3.set_speed_ratio(speed_ratio=40)
```

- **목적**: 로봇의 동작 속도 비율을 설정합니다.
- **입력**: `speed_ratio=40` - 속도 비율(0~100) 값입니다.
- **출력**: 성공적으로 설정 시 `{'code': '0', 'msg': ''}`
### 자동 서보 오프 설정 및 조회
#### `set_auto_servo_Off(), get_auto_servo_off()` 예시
**Input:**

```python
indydcp3.set_auto_servo_Off(time= 1.0, enable= True)
```

- **목적**: 자동 서보 오프 기능을 설정합니다.
- **입력**: `time= 1.0, enable= True` - 자동 서보 오프 기능을 활성화하고, 지연 시간을 설정합니다.
- **출력**: 성공적으로 설정 시 `{'code': '0', 'msg': ''}`
**Input:**

```python
indydcp3.get_auto_servo_off()
```

**Output**

```python
{'enable': True, 'time': 1.0}
```

- **목적**: 설정된 자동 서보 오프 설정을 조회합니다.
- **출력**: 현재 설정된 자동 서보 오프 기능의 활성화 상태와 지연 시간입니다.
### 충돌 감도 레벨 설정 및 조회
#### `set_coll_sens_level(), get_coll_sens_level()` 예시
**Input:**
충돌 감지 시의 감도 레벨을 설정하는 메소드입니다. 로봇이 작업 중 충돌을 감지할 때의 반응 감도를 조절할 수 있습니다. 낮은 값은 더 민감한 충돌 감지를 의미합니다.

```python
indydcp3.set_coll_sens_level(level=5)
```

- **목적**: 충돌 감도 레벨을 설정합니다.
- **입력**: `level=5` - 충돌 감도 레벨 값입니다. 범위는 로봇 모델 및 설정에 따라 다를 수 있으며, 일반적으로 1(가장 민감)부터 5(가장 둔감)까지 설정할 수 있습니다.
- **출력**: 성공적으로 설정 시 `{'code': '0', 'msg': ''}`
**Input:**
현재 설정된 충돌 감도 레벨을 조회하는 메소드입니다. 설정된 값을 확인하여 로봇의 충돌 감지 민감도를 알 수 있습니다.

```python
indydcp3.get_coll_sens_level()
```

**Output**

```python
{'level': 5}
```

- **목적**: 현재 설정된 충돌 감도 레벨을 조회합니다.
- **출력**: `level`에 현재 설정된 충돌 감도 레벨 값이 반환됩니다. 이 값은 로봇의 충돌 감지 시 반응하는 민감도를 나타냅니다.
### 안전 제한 설정 및 조회
#### `set_safety_limits(), get_safety_limits()` 예시
**Input:**
로봇의 안전한 동작을 위한 제한 사항을 설정하는 메소드입니다. 이 설정을 통해 로봇의 전력, 속도, 힘 등의 안전 제한을 정의할 수 있습니다.

```python
indydcp3.set_safety_limits(
    power_limit=1500.0,
    power_limit_ratio=100.0,
    tcp_force_limit=800.0,
    tcp_force_limit_ratio=100.0,
    tcp_speed_limit=4.0,
    tcp_speed_limit_ratio=100.0
)
print(response)
```

- **목적**: 로봇의 안전 제한을 설정합니다.
- **입력**:
- `power_limit`: 전력 제한 (와트 단위)
- `power_limit_ratio`: 전력 제한 비율 (%)
- `tcp_force_limit`: TCP(Tool Center Point) 힘 제한 (뉴턴 단위)
- `tcp_force_limit_ratio`: TCP 힘 제한 비율 (%)
- `tcp_speed_limit`: TCP 속도 제한 (m/s 단위)
- `tcp_speed_limit_ratio`: TCP 속도 제한 비율 (%)
- **출력**: 성공적으로 설정 시 `{'code': '0', 'msg': ''}`
**Input:**
현재 설정된 안전 제한을 조회하는 메소드입니다. 설정된 값들을 확인하여 로봇 동작의 안전 범위를 알 수 있습니다.

```python
response = indydcp3.get_safety_limits()
print(response)
```

**Output**

```python
{
 'power_limit': 1500.0,
 'power_limit_ratio': 100.0,
 'tcp_force_limit': 800.0,
 'tcp_force_limit_ratio': 100.0,
 'tcp_speed_limit': 4.0,
 'tcp_speed_limit_ratio': 100.0,
 'joint_limits': [175.0, 175.0, 175.0, 175.0, 175.0, 215.0]
}
```

- **목적**: 현재 설정된 안전 제한을 조회합니다.
- **출력**: 각 안전 제한의 현재 설정 값이 반환됩니다.
## 로봇 설정 상세 메뉴얼
이 섹션에서는 로봇의 상세 설정(Config) 기능을 다룹니다. 각 기능은 로봇의 성능과 상호작용을 최적화하기 위한 것입니다.
|          IndyDCP3 함수명        | Arguments       | Description |
|---------------------------------|-----------------------------------|-------------|
| `set_di_config_list()`            | `di_config_list: dict`       | 디지털 입력 설정을 구성합니다. |
| `get_di_config_list()`            | -              | 현재 디지털 입력 구성을 조회합니다. |
| `set_do_config_list()`            | `do_config_list: dict`                     | 디지털 출력 설정을 구성합니다. |
| `get_do_config_list()`            | -                  | 현재 디지털 출력 구성을 조회합니다. |
| `set_auto_servo_Off()`         | `enable: bool`, `time: float`        | 자동 서보 오프 기능을 설정합니다. |
| `get_auto_servo_off()`         | -               | 자동 서보 오프 설정을 조회합니다. |
| `set_friction_comp()`          | `control_comp: bool`,

`control_comp_levels: list`,

`dt_comp: bool`, `dt_comp_levels: list`              | 마찰 보상 설정을 합니다. |
| `get_friction_comp()`          | -                     | 마찰 보상 설정을 조회합니다. |
| `set_tool_property()`          | `mass: float`, `center_of_mass: list`, `inertia: list`          | 툴의 속성을 설정합니다. |
| `get_tool_property()`          | -                          | 툴의 속성을 조회합니다. |
| `set_coll_sens_param()`        | `j_torque_bases: list`,

`j_torque_tangents: list`,

`t_torque_bases: list`,

`t_torque_tangents: list`,

`error_bases: list`,

`error_tangents: list`,

`t_constvel_torque_bases: list`,

`t_constvel_torque_tangents: list`,

`t_conveyor_torque_bases: list`,

`t_conveyor_torque_tangents: list` | 충돌 감지 파라미터를 설정합니다. |
| `get_coll_sens_param()`        | -              | 충돌 감지 파라미터를 조회합니다. |
| `set_safety_limits()`          | `power_limit: float`,

`power_limit_ratio: float`,

`tcp_force_limit: float`,

`tcp_force_limit_ratio: float`,

`tcp_speed_limit: float`,

`tcp_speed_limit_ratio: float`                              | 안전 제한을 설정합니다. |
| `get_safety_limits()`          | -             | 안전 제한을 조회합니다. |
| `set_safety_stop_config()`     | `jpos_limit_stop_cat: int`,

`jvel_limit_stop_cat: int`,

`jtau_limit_stop_cat: int`,

`tvel_limit_stop_cat: int`,

`tforce_limit_stop_cat: int`,

`power_limit_stop_cat: int` | 안전 정지 구성을 설정합니다. |
| `get_safety_stop_config()`     | -           | 안전 정지 구성을 조회합니다. |
### 디지털 입력 및 출력 구성
#### `set_di_config_list(), set_do_config_list()` 예시
**Input:**
디지털 입력 기능을 구성합니다. 각 입력에 대한 기능 코드, 기능 이름, 트리거 신호, 성공 신호 및 실패 신호를 설정합니다.

```python
di_config_list = {
    'di_configs': [
      {
        'function_code': 2,
        'function_name': "ExampleFunction",
        'triggerSignals': [{'address': 1, 'state': 1}, {'address': 2, 'state': 0}],
        'successSignals': [{'address': 1, 'state': 1}, {'address': 2, 'state': 0}],
        'failureSignals': [{'address': 1, 'state': 1}, {'address': 2, 'state': 0}]
      }
    ]
}
indydcp3.set_di_config_list(di_config_list)
```

**Input:**
디지털 출력 구성을 설정합니다. 각 출력에 대한 상태 코드와 상태 이름, 켜짐 신호 및 꺼짐 신호를 설정합니다.

```python
do_config_list = {
    'do_configs': [
        {'state_code': 11,
        'state_name': 'ExampleState',
        'onSignals': [],
        'offSignals': []}
        ]
}
indydcp3.set_do_config_list(do_config_list)
```

### 마찰 보상
#### `set_friction_comp()` 예시
**Input:**
로봇의 마찰 보상을 설정합니다. 컨트롤 보상 활성화 여부, 컨트롤 보상 수준, DT 보상 활성화 여부, DT 보상 수준을 설정합니다.

```python
indydcp3.set_friction_comp(
    control_comp=True,
    control_comp_levels=[1, 1, 1, 1, 1, 1],
    dt_comp=True,
    dt_comp_levels=[1, 1, 1, 1, 1, 1])
```

### 툴 속성
#### `set_tool_property()` 예시
**Input:**
툴 무게, 질량 중심, 관성 모멘트를 설정합니다.

```python
response = indydcp3.set_tool_property(
    mass=1.0,
    center_of_mass=[3.0, 3.0, 3.0],
    inertia=[3.0, 2.0, 50.0, 3.0, 3.0, 3.0])
```

### 충돌 감지 파라미터
#### `set_coll_sens_param()` 예시
**Input:**
충돌 감지를 위한 파라미터 설정. 관절 토크 기준, 관절 토크 경사, 태스크 토크 기준, 태스크 토크 경사, 에러 기준, 에러 경사를 설정합니다.

```python
indydcp3.set_coll_sens_param(
    j_torque_bases=[50.0234, 45.5333, 21.0633, 11.3943, 7.8671, 4.7646],
    j_torque_tangents=[40.476, 31.2463, 11.1491, 7.377, 6.7769, 4.231],
    t_torque_bases=[52.4463, 48.9087, 18.2926, 11.2937, 7.5726, 4.7598],
    t_torque_tangents=[81.8369, 75.4495, 42.8034, 6.6005, 13.9731, 9.6169],
    error_bases=[0.0015, 0.0011, 0.0005, 0.0006, 0.0005, 0.0004],
    error_tangents=[0.0009, 0.0009, 0.0004, 0.0003, 0.0004, 0.0001])
```

### 안전 정지 구성
#### `set_safety_stop_config()` 예시
**Input:**
안전 정지 구성을 설정합니다. 관절 위치, 속도, 토크, 태스크 속도, 태스크 힘, 전력 제한의 정지 카테고리를 설정합니다.

```python
indydcp3.set_safety_stop_config(jpos_limit_stop_cat=1, jvel_limit_stop_cat=2, jtau_limit_stop_cat=2, tvel_limit_stop_cat=2, tforce_limit_stop_cat=2, power_limit_stop_cat=2)
```

### 충돌 튜닝
#### `set_coll_tuning()` 예시
충돌 감지 시스템의 튜닝을 설정합니다. 정밀도, 튜닝 공간, 최대 속도 레벨을 설정합니다.

```python
indydcp3.set_coll_tuning(precision=1, tuning_space=0, vel_level_max=3)
```

각 설정은 로봇의 특정 기능을 세밀하게 조정하고, 로봇의 움직임을 최적화하기 위한 것입니다. 설정 변경 시, 관련 문서와 사양을 참조하여 로봇의 안전과 성능을 보장해야 합니다.
