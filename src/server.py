import asyncio
import logging
import sys
import os

try:
    import websockets
except:
    print("websockets not ready.trying to install websockets.")
    exit(1)

logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '%(asctime)s %(levelname)-8s %(message)s', '%Y-%b-%d %H:%M:%S')
file_handler = logging.FileHandler("ARSPL.log", encoding='utf8')
file_handler.setFormatter(formatter)
steam_handler = logging.StreamHandler(stream=sys.stdout)
steam_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(steam_handler)
logger.setLevel(logging.INFO)
ADDRESS = '0.0.0.0'
PORT = 8000


async def server(websocket, path):
    message = await websocket.recv()
    logger.info(message)
try:
    start_server = websockets.serve(server, ADDRESS, PORT)
    print("==== Automatic reporting system of parking lot Server ====")
    print(f"Listening at {ADDRESS}:{PORT}")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except Exception:
    print(f"[ERROR]:network not available at {ADDRESS}:{PORT}.")
