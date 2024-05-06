import redis
import asyncio
import json
import os
from ..compute import Shared


async def connect_redis(config: dict, shared: Shared) -> None:
  HOST = config['REDIS']['HOST']
  PORT = config['REDIS']['PORT']
  DB = config['REDIS']['DB']
  print(f"Connecting to Redis Broker {HOST}:{PORT}...")

  r = redis.Redis(host=HOST, port=PORT, db=DB)
  print('Redis connection established')

  r.set('map', os.path.abspath(config['COMPUTER']['LAYOUT_FILE']))

  while True:

    if shared.event_stop.is_set():
      print('Redis connection closed')
      return
    if len(shared.output.items()) == 0:
      await asyncio.sleep(0.2)
      continue

    # print(shared.output)
    items = shared.output.copy()
    shared.output.clear()

    for key, value in items.items():
      r.hset('users', key, json.dumps(value))