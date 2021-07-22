import asyncio
from bleak import BleakClient
import simpleaudio as sa
wave_obj = sa.WaveObject.from_wave_file("buzzer.wav")


address = "E7:B3:50:17:EE:50"
MODEL_NBR_UUID = "50c9727e-4cb8-4c84-b745-0e58a0280cd6"
sheeesh = 1

async def run(address):
    async with BleakClient(address) as client:
        while sheeesh > 0:
            model_number = await client.read_gatt_char(MODEL_NBR_UUID)
            pressedfile = open("pressed.txt","rb")
            pressedvalue = pressedfile.read()
            if model_number != pressedvalue:
                pressedwrite = open("pressed.txt","w")
                pressedwrite.close()
                pressedfile.close()
                writebytes = open("pressed.txt","wb")
                writebytes.write(model_number)
                print(model_number)
                print('POG THROUGH THE PAIN')
                play_obj = wave_obj.play()
                writebytes.close()
loop = asyncio.get_event_loop()
loop.run_until_complete(run(address))