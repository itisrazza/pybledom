import asyncio
import sys
import os
from time import sleep
from random import randint

# bleak imports
from bleak import BleakScanner, BleakClient
from bleak.backends.device import BLEDevice

# project imports
from . import util
from .device import BleLedDevice


async def select_bt_device() -> BLEDevice:
    """
    Scans the available devices and asks the user to choose one.
    """

    # get the devices
    devices = [device for device in await BleakScanner.discover()]
    if len(devices) == 0:
        print("No bluetooth devices available.")
        sys.exit(1)

    # ask the user to choose
    user_choice = util.choose("Select device",
                              "Choose device number",
                              map(lambda device: str(device), devices))

    # if the user hadn't picked anything, quit here
    if user_choice is None:
        sys.exit(0)

    # find the right device and return it
    return devices[user_choice]


async def connect_bt_device(device) -> BleakClient:
    """
    Connects to the provided device. Throws an exception on error.

    Make sure to disconnect when the program closes.
    """

    print("Connecting to %s (%s)..." % (device.name, device.address))

    client = BleakClient(device)
    await client.connect()
    return client


async def default_callable(device: BleLedDevice):
    """
    The default run function. Randomly sets colours on the LED strip.
    """

    while True:
        sleep(2)
        await device.set_color(randint(0, 255),
                               randint(0, 255),
                               randint(0, 255))


async def run(func: callable):
    """
    Sets up the device and calls the provided function.
    """

    bt_device = await select_bt_device()
    bt_client = await connect_bt_device(bt_device)
    try:
        device = await BleLedDevice.new(bt_client)
        await func(device)
    finally:
        # disconnect when we finish
        await bt_client.disconnect()


def run_sync(func: callable = default_callable):
    """
    Sets up the device and calls the provided function. If not provided, will
    use a demo function instead.
    """

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(func))


if __name__ == "__main__":
    run_sync()
