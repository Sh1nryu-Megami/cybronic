import paho.mqtt.client as mqtt
import sys


def parseArgv() -> dict[dict]:
  arguments = {
    '-h': {
      'exists': False,
    },
    '-o': {
      'exists': False,
      'data': None,
    },
    '-f': {
      'exists': False,
      'data': None,
    },
  }
  
  for arg in sys.argv[1:]:
    if arg == '-h':
      arguments['-h']['exists'] = True
    elif arg == '-o':
      arguments['-o']['exists'] = True
    elif arg == '-f':
      arguments['-f']['exists'] = True
    else:
      arguments['-o']['data'] = arg

  return arguments

def main():
  args = parseArgv()