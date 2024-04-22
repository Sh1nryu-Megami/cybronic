import asyncio
import json
from .type import Shared
from .store import Store


async def computer(config: dict, shared: Shared) -> None:
  with open(config['COMPUTER']['LAYOUT_FILE']) as f:
    layout = json.loads(f.read())
  
  store = Store(config['COMPUTER'], layout)
  
  while True:

    if shared.event_stop.is_set():
      return
    
    if len(shared.input_queue) == 0:
      await asyncio.sleep(0.2)
      continue

    shared.lock.acquire()
    input_data = shared.input_queue.copy()
    shared.input_queue.clear()
    shared.lock.release()


    for item in input_data:
      res = store.add(item['device'], item['lighthouse'], item['distance'])

      if res['x'] != -1:
        shared.output[item['device']] = res
        
      
