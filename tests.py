import asyncio
from bleak import BleakClient

address = "F0:A9:85:92:21:CE"
MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"

async def run(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
