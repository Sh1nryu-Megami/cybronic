import json
import sys
import os


def get_relpath(relpath) -> str:
  if not os.path.isabs(relpath):
    return relpath
  return os.path.relpath(relpath, os.path.dirname(os.path.abspath(__file__)))

def parseArgv() -> dict[dict]:
  arguments = {
    '-v': {
      'exists': False,
      'single': True,
    },
    '-l': {
      'exists': False,
      'single': True,
    },
    '-h': {
      'exists': False,
      'single': True,
    }
  }

  for index, arg in enumerate(sys.argv):
    if arg in arguments:
      arguments[arg]['exists'] = True

      if 'single' not in arguments[arg]:
        try:
          arguments[arg]['data'] = sys.argv[index + 1]
        except IndexError:
          print(f"Argument {arg} requires an argument")
          sys.exit(1)
      
  return arguments

def main() -> None:
  conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
  try:
    with open(conf_path, 'r') as f:
      CONFIG = json.load(f)
  except FileNotFoundError:
    print("ERROR: config.json file not found")
    sys.exit(1)
  
  args = parseArgv()

  if args['-v']['exists']:
    CONFIG["COMPUTER"]["VIEW_FILE"] = get_relpath(CONFIG["COMPUTER"]["VIEW_FILE"])
    print(CONFIG["COMPUTER"]["VIEW_FILE"], end='')
  elif args['-l']['exists']:
    CONFIG["COMPUTER"]["LAYOUT_FILE"] = get_relpath(CONFIG["COMPUTER"]["LAYOUT_FILE"])
    print(CONFIG["COMPUTER"]["LAYOUT_FILE"], end='')
  elif args['-h']['exists']:
    print(CONFIG["HOST"]["IP"])
  
  try:
    with open(conf_path, 'w') as f:
      json.dump(CONFIG, f, indent=2)
  except FileNotFoundError:
    print("ERROR: config.json file not found")
    sys.exit(1)

if __name__ == '__main__':
  main()