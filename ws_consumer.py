import asyncio
import websockets
import pyaudio

CHUNK = 128
WIDTH = 2
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

async def consumer_handler(websocket):
    async for message in websocket:
        # print(message)
        # print("got it!")
        stream.write(message, CHUNK)

async def consume():
    # websocket_resource_url = "wss://eligs-low-latency-audio.herokuapp.com/0.0.0.0"
    websocket_resource_url = "ws://10.0.0.157"
    async with websockets.connect(websocket_resource_url) as websocket:
        await consumer_handler(websocket)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume())
    loop.run_forever()