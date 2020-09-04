import json
import multiprocessing
import os
import threading
import time

import requests

import lpr

CONNECTION_URL = "http://127.0.0.1:3000/update"
try:
    import cv2.cv2 as cv2
except Exception as e:

    exit(1)

CPU_COUNT = os.cpu_count()
PROC_COUNT = CPU_COUNT + 2

REMAIN_ALL = 30
REMAIN_EFFECITVE = 25


def upload(msg: dict):
    try:
        r = requests.post(CONNECTION_URL, json=msg)
        print(f"[host feedback]{r}")
    except Exception as e:
        print("[error]network error")


def process(i, frameQueue, resQueue):
    print(f"[proc {i}] pid {os.getpid()}")
    # fetch frame and push to work queqe
    if i == 0:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            '''
            演示模式请取消下面注释以获得视频体验
            '''
            # if you want to view image, enable line below
            cv2.imshow('cam', frame)
            cv2.waitKey(1)

            frameQueue.put(frame)
    # fetch result and output
    elif i == 1:
        lastP = ''
        resList = list()
        resList = ['' for i in range(REMAIN_ALL)]
        while True:
            res = resQueue.get()
            resList.append(res)
            del resList[0]
            remain = 0
            for i in resList:
                if i == res:
                    remain += 1
            print(f"{time.time():.3f}s {res} times = {remain}", end='')
            print(''*10, end='\r')
            if (len(res) == 0 or len(res[0]) > 6) and remain >= REMAIN_EFFECITVE:
                if lastP != res:
                    data = dict()
                    data['time'] = time.time()
                    data['plate'] = res
                    print(data)
                    lastP = res
                    threading.Thread(target=upload, args=(data,)).start()

            # fetch frame and recognize plate then put result into result queue
    else:
        while True:
            frame = frameQueue.get()
            res = lpr.recognition(frame)
            resQueue.put(res)
            # print(f"[proc {i}] recognized, {time.time()-t:.2f} s,{res}")


def client():
    print(f"Process :{PROC_COUNT}")
    pool = multiprocessing.Pool(PROC_COUNT)
    frameQueue = multiprocessing.Manager().Queue(PROC_COUNT)
    resQueue = multiprocessing.Manager().Queue(PROC_COUNT)
   #
    for i in range(PROC_COUNT):
        pool.apply_async(
            process, (i, frameQueue, resQueue))
    pool.close()
    pool.join()
    print("finish")


if __name__ == '__main__':
    client()
