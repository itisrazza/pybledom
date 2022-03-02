import sys
import os
import asyncio
from random import randint
from matplotlib.colors import to_rgb
from bleak import BleakScanner, BleakClient
from bleak.exc import BleakDBusError
from bledom.device import BleLedDevice


async def main():
    try:
        prefix = os.environ.get("ELK-BLEDOM", "ELK-BLEDOM")
        devices = await BleakScanner.discover()
        devices = [d for d in devices if d.name.startswith(prefix)]  # avoid padding spaces
        for device in devices:
            client = BleakClient(device)
            await client.connect()
            device = await BleLedDevice.new(client)
            
            if c == "off":
                print("Turning off")
                return await device.power_off()
            if c.isdigit():
                print("Setting brightness", c)
                await device.set_brightness(int(c))
            else:
                print("Setting color", c)
                await device.set_color(*[int(f*255) for f in to_rgb(c)])
        if not devices:
            print(f"No device with prefix {prefix} found. If your device has another prefix, set the environment variable ELK-BLEDOM")
    except BleakDBusError:
        await main()  # retry on common error
 
    
if __name__ == "__main__":
    c = sys.argv[-1]
    if "main" in c or "bledom" in c:
        print("Usage: python -m bledom [off | color-name | brightness-level [0-100]]")
    else:
        asyncio.run(main())

