from threading import Lock

class Shared:
  input_queue = []
  output = {}
  lock = Lock()