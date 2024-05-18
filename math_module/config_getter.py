import json
import sys


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
  try:
    with open("./config.json", 'r') as f:
      CONFIG = json.load(f)
  except FileNotFoundError:
    print("ERROR: config.json file not found")
    sys.exit(1)
  
  args = parseArgv()

  if args['-v']['exists']:
    print(CONFIG["COMPUTER"]["VIEW_FILE"])
    sys.exit(0)
  elif args['-l']['exists']:
    print(CONFIG["COMPUTER"]["LAYOUT_FILE"])
    sys.exit(0)
  elif args['-h']['exists']:
    print(CONFIG["HOST"]["IP"])


if __name__ == '__main__':
  main()