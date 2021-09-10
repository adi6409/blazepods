import asyncio
from bleak import BleakClient

address = "C5:02:0A:BD:EF:E3"
MODEL_NBR_UUID = "50c9727e-4cb8-4c84-b745-0e58a0280cd6"

async def run(address):
    async with BleakClient(address) as client:
        print("connected!")
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))
