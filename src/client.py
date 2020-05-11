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
    lastres = []
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        # if you want to view image, enable line below
        # cv2.imshow('cam', frame)
        res = lpr.recognition(frame)
        cv2.waitKey(1)
        if lastres != res:
            async with websockets.connect('ws://localhost:8000') as websocket:
                msg = "%s %s" % (time.ctime(time.time()), res)
                print(msg)
                await websocket.send(msg)
                lastres = res

asyncio.get_event_loop().run_until_complete(client())
