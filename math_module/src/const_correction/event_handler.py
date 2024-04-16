from watchdog.events import FileSystemEvent, FileSystemEventHandler
import json
# from ...config import *


class EventHandler(FileSystemEventHandler):
  def __init__(self, config) -> None:
    super().__init__()
    self.config = config

  
  def on_modified(self, event: FileSystemEvent) -> None:
    super().on_modified(event)

    print("FileSystemEventHandler ./config.json modified.")

    with open('./config.json', 'r') as f:
      update_config = json.loads(f.read())
    
    self.config['LIGHTHOUSE_TEST_DISTANCE'] = update_config['LIGHTHOUSE_TEST_DISTANCE']
    self.config['SIGNAL_TEST_POWER'] = update_config['SIGNAL_TEST_POWER']
    self.config['LOSE_FACTOR'] = update_config['LOSE_FACTOR']