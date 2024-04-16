import asyncio
import json
from .type import Shared


async def computer(config: dict, shared: Shared) -> None:
  with open(config['COMPUTER']['LAYOUT_FILE']) as f:
    layout = json.loads(f.read())
  
  while True:
    if len(shared.input_queue) == 0:
      await asyncio.sleep(0.2)
      continue

    shared.lock.acquire()
    input_data = shared.input_queue.copy()
    shared.input_queue.clear()
    shared.lock.release()

    for item in input_data:
      pass
