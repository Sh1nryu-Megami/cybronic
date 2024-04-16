import asyncio
import os
from watchdog.observers import Observer
from .event_handler import EventHandler


async def create_observer(stop_event: asyncio.Event, config: dict) -> None:
  """
  Create a new observer and start watching updates to config.json file.

  :param stop_event:
  :type stop_event: asyncio.Event

  :param config:
  :type config: dict

  :return: None
  """

  # create a new event handler
  event_handler = EventHandler(config)
  observer = Observer()
  print(os.getcwd())
  observer.schedule(event_handler, './', recursive=True)
  observer.start()
  print("Start observer for watching updates to config.json...")

  # waiting for Keyboard Interrupt or something else stop signal
  await stop_event.wait()

  # stop the observer
  observer.stop()
  observer.join()
  print("Stop observer for watching updates to config.json")