import threading
import time
import requests

CONNECTION_URL = "http://127.0.0.1:3000/update"


def upload(msg: int):
    print("a")
    t = time.time()
    r = requests.post(CONNECTION_URL, json={
                      "plant": msg, "time": time.time(), "manual": "leave"})
    print(f"{time.time()-t}{r.text}")


while True:
    a = 1
    threading.Thread(target=upload, args=(a,)).start()
    time.sleep(5)
