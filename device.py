from enum import IntFlag


class Days(IntFlag):
    MONDAY = 1 << 1
    TUESDAY = 1 << 2
    WEDNESDAY = 1 << 3
    THURSDAY = 1 << 4
    FRIDAY = 1 << 5
    SATURDAY = 1 << 6
    SUNDAY = 1 << 7
    ALL = MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY
    WEEKEND_DAYS = SATURDAY | SUNDAY
    WEEK_DAYS = ALL & ~WEEKEND_DAYS
    NONE = 0


class Effects(IntFlag):
    JUMP_RED_GREEN_BLUE = 0x87
    JUMP_RED_GREEN_BLUE_YELLOW_CYAN_MAGENTA_WHITE = 0x88
    CROSSFADE_RED = 0x8b
    CROSSFADE_GREEN = 0x8c
    CROSSFADE_BLUE = 0x8d
    CROSSFADE_YELLOW = 0x8e
    CROSSFADE_CYAN = 0x8f
    CROSSFADE_MAGENTA = 0x90
    CROSSFADE_WHITE = 0x91
    CROSSFADE_RED_GREEN = 0x92
    CROSSFADE_RED_BLUE = 0x93
    CROSSFADE_GREEN_BLUE = 0x94
    CROSSFADE_RED_GREEN_BLUE = 0x89
    CROSSFADE_RED_GREEN_BLUE_YELLOW_CYAN_MAGENTA_WHITE = 0x8a
    BLINK_RED = 0x96
    BLINK_GREEN = 0x97
    BLINK_BLUE = 0x98
    BLINK_YELLOW = 0x99
    BLINK_CYAN = 0x9a
    BLINK_MAGENTA = 0x9b
    BLINK_WHITE = 0x9c
    BLINK_RED_GREEN_BLUE_YELLOW_CYAN_MAGENTA_WHITE = 0x95


class BleLedDevice:
    def __init__(self):
        self.peripheral = None
        self.characteristics = None

        self.sync_time()
        self.power_on()

    def sync_time(self):
        pass

    def set_custom_time(self, hour: int, minute: int, second: int, day_of_week: int):
        pass

    def power_on(self):
        pass

    def power_off(self):
        pass

    def set_color(self, red: int, green: int, blue: int):
        pass

    def set_brightness(self, value: int):
        pass

    def set_effect(self, value: int):
        pass

    def set_effect_speed(self, value: int):
        pass

    def set_schedule_on(self, days: int, hours: int, minutes: int, enabled: bool):
        pass

    def set_schedule_off(self, days: int, hours: int, minutes: int, enabled: bool):
        pass

    def generic_command(self, id: int, sub_id: int, arg1: int, arg2: int, arg3: int):
        pass
