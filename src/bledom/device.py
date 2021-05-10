from datetime import datetime
from enum import IntFlag, IntEnum
from bleak import BleakClient, BleakScanner
from typing import Optional, List

BLEDOM_CHARACTERISTIC = "0000fff3-0000-1000-8000-00805f9b34fb"


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


class Effects(IntEnum):
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
    def __init__(self, peripheral, characteristics):
        self.peripheral = peripheral
        self.characteristics = characteristics

    @staticmethod
    async def new(bt_client: BleakClient) -> "BleLedDevice":
        characteristics = []
        for service in await bt_client.get_services():
            for characteristic in service.characteristics:
                if characteristic.uuid == BLEDOM_CHARACTERISTIC:
                    characteristics.append(characteristic)

        device = BleLedDevice(bt_client, characteristics)
        await device.sync_time()
        await device.power_on()
        return device

    def _characteristic(self):
        return self.characteristics[0]

    async def sync_time(self):
        print("BleLedDevice::sync_time - stub !")

    async def set_custom_time(self, time: datetime):
        hour = time.hour()
        minute = time.minute()
        second = time.second()
        day_of_week = time.weekday() + 1    # 1 (monday) -> 7 (sunday)
        print("BleLedDevice::set_custom_time - stub !")

    async def power_on(self):
        await self.generic_command(0x04, 0xF0, 0x00, 0x01, 0xFF)

    async def power_off(self):
        await self.generic_command(0x04, 0x00, 0x00, 0x00, 0xFF)

    async def set_color(self, red: int, green: int, blue: int):
        await self.generic_command(0x05, 0x03, red, green, blue)

    async def set_brightness(self, value: int):
        await self.generic_command(0x01, min(value, 100), 0, 0, 0)

    async def set_effect(self, value: Effects):
        await self.generic_command(0x03, value.value, 0, 0, 0)

    async def set_effect_speed(self, value: int):
        await self.generic_command(0x02, min(value, 100), 0, 0, 0)

    async def set_schedule_on(self,
                              days: int,
                              hours: int,
                              minutes: int,
                              enabled: bool):
        await self.generic_command(0x82,
                                   min(hours, 23),
                                   min(hours, 59),
                                   0,
                                   0,
                                   (days + 0x80) if enabled else days)

    async def set_schedule_off(self,
                               days: int,
                               hours: int,
                               minutes: int,
                               enabled: bool):
        await self.generic_command(0x82,
                                   min(hours, 23),
                                   min(hours, 59),
                                   0,
                                   0,
                                   (days + 0x80) if enabled else days)
        pass

    async def generic_command(self,
                              id: int,
                              sub_id: int,
                              arg1: int,
                              arg2: int,
                              arg3: int):
        data = bytearray(
            [0x7E, 0x00, id, sub_id, arg1, arg2, arg3, 0x00, 0xEF])

        print("sending message %s", list(data))
        await self.peripheral.write_gatt_char(self._characteristic(), data)
