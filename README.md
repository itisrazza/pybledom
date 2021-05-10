# Python library for controlling BLEDOM devices

> This library is still in development. Functionality hasn't fully been tested yet. If you find bugs or "stub" messages, please [create an issue](https://github.com/thegreatrazz/pybledom/issues).

## Demo Program

This library comes with a demo program.

```bash
python -m bledom
```

## API

### Run API

You can let the library do the Bluetooth set up for you by creating a main function which the library will call after having set up the Bluetooth device.

```python
from time import sleep
from bledom import BleLedDevice, run_sync

async def main(device: BleLedDevice):
    while True:
        sleep(2)
        await device.set_color(randint(0, 255),
                               randint(0, 255),
                               randint(0, 255))

run_sync(main)
```

### Device API

#### Creating a device from with a BleakClient

> Reading the [Bleak documentation](https://bleak.readthedocs.io/en/latest/) is recommended for connecting to a device manually.

A device connection can be created with a Bleak client. See [main.py](src/bledom/main.py) for an example.

```
device = BleLedDevice.new(client)
```

The device will be powered on and have it's time synced on when it gets connected.

#### Modes

* **`device.power_on(self)`** \
    Powers on the device
* **`device.set_color(128, 64, 255)`** \
    Sets a static colour
* **`device.set_brightness(64)`** \
    Sets a static brightness (0-100)
* **`device.set_effect(Effects.CROSSFADE_RED_GREEN_BLUE)`** \
    Sets an effect
* **`device.set_effect_speed(64)`** \
    Sets the effect speed

#### Time and Schedule

* **`device.sync_time()`** \
    Syncs the device to the system time. Gets called on connection.
* **`device.set_custom_time(datetime.now())`** \
    Syncs the device to the given [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime).
* **`device.set_schedule_on(Days.TUESDAY | Days.THURSDAY, 7, 30, True)`** \
    Schedules LED to turn on on Tuesday and Thursday at 7:30 AM. Set last argument to `False` to disable.
* **`device.set_schedule_off(Days.ALL, 0, 0, True)`** \
    Schedules LED to turn off everyday at midnight (12:00 AM). Set last argument to `False` to disable.

The `Days` enum has the days `MONDAY` through `SUNDAY` as well as `WEEK_DAY` (Monday through Friday), `WEEKEND_DAYS` (Saturday and Sunday) and `ALL` for all days.

#### Effects

For `device.set_effect(...)`, the following effects are available:

* `Effects.JUMP_RED_GREEN_BLUE`
* `Effects.JUMP_RED_GREEN_BLUE_YELLOW_CYAN_MAGENTA_WHITE`
* `Effects.CROSSFADE_RED`
* `Effects.CROSSFADE_GREEN`
* `Effects.CROSSFADE_BLUE`
* `Effects.CROSSFADE_YELLOW`
* `Effects.CROSSFADE_CYAN`
* `Effects.CROSSFADE_MAGENTA`
* `Effects.CROSSFADE_WHITE`
* `Effects.CROSSFADE_RED_GREEN`
* `Effects.CROSSFADE_RED_BLUE`
* `Effects.CROSSFADE_GREEN_BLUE`
* `Effects.CROSSFADE_RED_GREEN_BLUE`
* `Effects.CROSSFADE_RED_GREEN_BLUE_YELLOW_CYAN_MAGENTA_WHITE`
* `Effects.BLINK_RED`
* `Effects.BLINK_GREEN`
* `Effects.BLINK_BLUE`
* `Effects.BLINK_YELLOW`
* `Effects.BLINK_CYAN`
* `Effects.BLINK_MAGENTA`
* `Effects.BLINK_WHITE`
* `Effects.BLINK_RED_GREEN_BLUE_YELLOW_CYAN_MAGENTA_WHITE`


## Acknowledgements

This library is a port of [a Rust library written by TheSylex][rust-lib].

Salutations to [Joel](https://github.com/jxeldotdev).

[rust-lib]: https://github.com/TheSylex/ELK-BLEDOM-bluetooth-led-strip-controller
