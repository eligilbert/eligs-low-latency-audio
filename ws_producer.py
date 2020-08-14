import asyncio
import websockets

async def produce(message):
    # async with websockets.connect("ws://eligs-low-latency-audio.herokuapp.com") as ws:
    async with websockets.connect("ws://10.0.0.157") as ws:
        await ws.send(message)
        await ws.recv()

import pyaudio
import time

CHUNK = 512
WIDTH = 2
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

while True:
    # try:
    #     data = stream.read(CHUNK)
    #     asyncio.run(produce(data))
    # except OSError:
    #     print("Input overflowed. Please restart producer!")
    #     break
    data = stream.read(CHUNK)
    # print(data)
    asyncio.run(produce(data))