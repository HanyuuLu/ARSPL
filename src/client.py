import lpr
import requests
import os
import multiprocessing
import time
CONNECTION_URL = "http://127.0.0.1:3000/update"
try:
    import cv2.cv2 as cv2
    import websockets
except:
    print("websockets or opencv are not ready.trying to install these package.")
    exit(1)

CPU_COUNT = os.cpu_count()
PROC_COUNT = CPU_COUNT + 2


def process(i, frameQueue, resQueue):
    print(os.getpid())
    if i == 0:
        cap = cv2.VideoCapture(0)
        while True:
            t = time.time()
            ret, frame = cap.read()
            '''
            演示模式请取消下面注释以获得视频体验
            '''
            # if you want to view image, enable line below
            # cv2.imshow('cam', frame)
            # cv2.waitKey(1)

            frameQueue.put(frame)
            #print(f"[proc {i}] pushed, {time.time()-t} s")
    elif i == 1:
        while True:
            t = time.time()
            res = resQueue.get()
            #print(f"[proc {i}] fetched, {res} {time.time()-t} s")
    else:
        while True:
            t = time.time()
            frame = frameQueue.get()
            res = lpr.recognition(frame)
            resQueue.put(res)
            print(f"[proc {i}] recognized, {time.time()-t} s")


def client():
    print(f"CPU core:{PROC_COUNT}")
    # print(os.getpid())
    pool = multiprocessing.Pool(PROC_COUNT)
    frameQueue = multiprocessing.Manager().Queue(PROC_COUNT)
    #frameLock = multiprocessing.Lock()
    resQueue = multiprocessing.Manager().Queue(PROC_COUNT)
    # resLock = multiprocessing.Lock()
   #
    for i in range(PROC_COUNT):
        pool.apply_async(
            process, (i, frameQueue, resQueue))
    pool.close()
    pool.join()
    print("finish")


if __name__ == '__main__':
    client()
