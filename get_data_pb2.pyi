from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

Channel1Off: States
Channel1On: States
Channel2Off: States
Channel2On: States
ChannelOff: ChannelStates
ChannelOn: ChannelStates
Close: DoorLockStates
DESCRIPTOR: _descriptor.FileDescriptor
DoorLockClose: States
DoorLockOpen: States
Error: Statuses
LightOff: States
LightOn: States
Off: LightStates
Ok: Statuses
On: LightStates
Open: DoorLockStates

class ClientMessage(_message.Message):
    __slots__ = ["get_info", "get_state", "set_state"]
    GET_INFO_FIELD_NUMBER: _ClassVar[int]
    GET_STATE_FIELD_NUMBER: _ClassVar[int]
    SET_STATE_FIELD_NUMBER: _ClassVar[int]
    get_info: GetInfo
    get_state: GetState
    set_state: SetState
    def __init__(self, get_info: _Optional[_Union[GetInfo, _Mapping]] = ..., set_state: _Optional[_Union[SetState, _Mapping]] = ..., get_state: _Optional[_Union[GetState, _Mapping]] = ...) -> None: ...

class ControllerResponse(_message.Message):
    __slots__ = ["info", "state", "status"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    info: Info
    state: State
    status: Statuses
    def __init__(self, info: _Optional[_Union[Info, _Mapping]] = ..., state: _Optional[_Union[State, _Mapping]] = ..., status: _Optional[_Union[Statuses, str]] = ...) -> None: ...

class GetInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetState(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class IdentifyRequest(_message.Message):
    __slots__ = ["Token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    Token: str
    def __init__(self, Token: _Optional[str] = ...) -> None: ...

class Info(_message.Message):
    __slots__ = ["ble_name", "ip", "mac", "token"]
    BLE_NAME_FIELD_NUMBER: _ClassVar[int]
    IP_FIELD_NUMBER: _ClassVar[int]
    MAC_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ble_name: str
    ip: str
    mac: str
    token: str
    def __init__(self, ip: _Optional[str] = ..., mac: _Optional[str] = ..., ble_name: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class SetState(_message.Message):
    __slots__ = ["state"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: States
    def __init__(self, state: _Optional[_Union[States, str]] = ...) -> None: ...

class State(_message.Message):
    __slots__ = ["channel_1", "channel_2", "door_lock", "humidity", "light_on", "pressure", "temperature"]
    CHANNEL_1_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_2_FIELD_NUMBER: _ClassVar[int]
    DOOR_LOCK_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    LIGHT_ON_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    channel_1: ChannelStates
    channel_2: ChannelStates
    door_lock: DoorLockStates
    humidity: float
    light_on: LightStates
    pressure: float
    temperature: float
    def __init__(self, light_on: _Optional[_Union[LightStates, str]] = ..., door_lock: _Optional[_Union[DoorLockStates, str]] = ..., channel_1: _Optional[_Union[ChannelStates, str]] = ..., channel_2: _Optional[_Union[ChannelStates, str]] = ..., temperature: _Optional[float] = ..., pressure: _Optional[float] = ..., humidity: _Optional[float] = ...) -> None: ...

class Statuses(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class LightStates(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class DoorLockStates(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ChannelStates(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class States(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
