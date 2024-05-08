#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys
import os
from itertools import count
import cssutils
import json
import config


def parseArgv() -> dict[dict]:
  arguments = {
    '-h': {
      'exists': False,
      'single': True,
    },
    '-o': {
      'exists': False,
      'data': None,
    },
    '-f': {
      'exists': False,
      'data': None,
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


def exclude_file_extantion(filename: str) -> str:
  start = len(filename) - 1
  while start >= 0 and filename[start] != '.':
    start -= 1
  
  if start == -1:
    return filename
  
  return filename[:start]


def svg_find(root, tag, all=False):
  res = []
  for item in root.iter():
    if item.tag.endswith(tag):
      if all:
        res.append(item)
      else:
        return item
  
  if all:
    return res
  else:
    return None


def main():
  args = parseArgv()

  if args['-h']['exists']:
    with open('help.txt', 'r') as f:
      help_text = f.read()
    
    print(help_text)
    sys.exit(0)
  elif not args['-f']['exists']:
    print("You must specify at least an input filename with -f.")
    sys.exit(1)

  try:
    tree = ET.parse(args['-f']['data'])
  except FileNotFoundError:
    print(f"File {args['-f']['data']} not found")
    sys.exit(1)
  
  root = tree.getroot()

  if svg_find(root, 'style') == None:
    print(f"File {args['-f']['data']} does not contain a style tag")
    sys.exit(1)
  else:
    style = cssutils.parseString(svg_find(root, 'style').text, validate=False)

  if len(style.cssRules) == 0:
    print(f"File {args['-f']['data']} does not contain any rules")
    sys.exit(1)
  
  classes = {
    'hall': None,
    'lighthouse': None,
  }

  for rule in style.cssRules:
    if rule.style.cssText[-7:].lower() == config.HALL_COLOR.lower():
      classes['hall'] = rule.selectorText[1:]
    elif rule.style.cssText[-7:].lower() == config.LIGHTHOUSE_COLOR.lower():
      classes['lighthouse'] = rule.selectorText[1:]
  
  if classes['hall'] is None or classes['lighthouse'] is None:
    print(f"File {args['-f']['data']} does not contain a hall or lighthouse colors.")
    sys.exit(1)

  coordinates = {
    'bounds': {
      'width': float(root.attrib['viewBox'].split(' ')[2]),
      'height': float(root.attrib['viewBox'].split(' ')[3]),
      'scale': 0,
    },
    'halls': {},
    'lighthouses': {},
  }

  text_scale = svg_find(root, 'text')

  if text_scale is None:
    print(f"File {args['-f']['data']} does not contain a text tag with scale in it.")
    sys.exit(1)

  coordinates['bounds']['scale'] = float(text_scale.text.split('=')[1])

  for rect in svg_find(root, 'rect', True):
    x = float(rect.attrib.get('x', 0))
    y = float(rect.attrib.get('y', 0))
    width = float(rect.attrib['width'])
    height = float(rect.attrib['height'])
    id = rect.attrib['id']
    classifier = rect.attrib['class']

    if classifier == classes['hall']:
      if id[-4:] == 'vert':
        baseline = x + width / 2
      elif id[-3:] == 'hor':
        baseline = y + height / 2
      else:
        print(f"File {args['-f']['data']} contains wrong id {id} notation for hall.")
        sys.exit(1)

      coordinates['halls'][id] = {
        'id': id,
        'x': x,
        'y': y,
        'width': width,
        'height': height,
        'baseline': baseline,
      }
    elif classifier == classes['lighthouse']:
      center = (x + width / 2, y + height / 2)

      coordinates['lighthouses'][id] = {
        'id': id,
        'x': center[0],
        'y': center[1],
      }
    else:
      print(f"File {args['-f']['data']} contains an unknown class {classifier}")
      sys.exit(1)
  
  for _, lighthouse in coordinates['lighthouses'].items():
    for _, hall in coordinates['halls'].items():
      if hall['x'] <= lighthouse['x'] <= hall['x'] + hall['width'] and hall['y'] <= lighthouse['y'] <= hall['y'] + hall['height']:
        lighthouse['hall'] = hall['id']
    
    if lighthouse.get('hall') is None:
      print(f"File {args['-f']['data']} contains a lighthouse that does not belong to any hall.")
      sys.exit(1)

  if args['-o']['exists']:
    basename = os.path.basename(args['-o']['data'])

    if basename == '':
      basename = exclude_file_extantion(os.path.basename(args['-f']['data']))
      basename += '.json'

    output = os.path.join(os.path.dirname(args['-o']['data']), basename)
  else:
    basename = exclude_file_extantion(os.path.basename(args['-f']['data']))
    basename += '.json'

    output = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output', basename)
  
  with open(output, 'w') as f:
    json.dump(coordinates, f, indent=2)

  print(f"Output saved to {basename}")
  sys.exit(0)


if __name__ == '__main__':
  main()
