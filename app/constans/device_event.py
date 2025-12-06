from enum import Enum


class DeviceState(str, Enum):
    ON = "ON"
    OFF = "OFF"


class EventType(str, Enum):
    DEVICE_ON = "DEVICE_ON"
    DEVICE_OFF = "DEVICE_OFF"
    GPIO_CHANGE = "GPIO_CHANGE"
    AUTO_TRIGGER = "AUTO_TRIGGER"
    SCHEDULE_TRIGGER = "SCHEDULE_TRIGGER"
    MANUAL_TRIGGER = "MANUAL_TRIGGER"
    ERROR = "ERROR"
