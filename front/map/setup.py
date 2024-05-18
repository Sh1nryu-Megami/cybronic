import sys
import os


def parseArgv() -> dict[dict]:
  arguments = {
    '--ip': {
      'exists': False,
    },
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
  args = parseArgv()
  if args['--ip']['exists']:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src/config.js'), 'w') as f:
      f.write(f"export const fetch_addr = 'http://{args['--ip']['data']}/';")


if __name__ == '__main__':
  main()