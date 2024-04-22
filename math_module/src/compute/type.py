from threading import Lock
import asyncio

class Shared:
  input_queue = []
  output = {}
  lock = Lock()
  event_stop = asyncio.Event()