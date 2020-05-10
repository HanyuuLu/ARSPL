import asyncio
import time


import lpr

try:
    import cv2.cv2 as cv2
    import websockets
except:
    print("websockets or opencv are not ready.trying to install these package.")
    exit(1)


async def client():
    async with websockets.connect('ws://localhost:8000') as websocket:

        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            res = lpr.recognition(frame)
            msg = "%s %s" % (time.ctime(time.time()), res)
            print(msg)
            await websocket.send(msg)

asyncio.get_event_loop().run_until_complete(client())
