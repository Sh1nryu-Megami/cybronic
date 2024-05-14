CONFIG = {
  # Constants for calculating distance for person to lighthouse
  'CALC': {
    'LIGHTHOUSE_TEST_DISTANCE': 1,
    'SIGNAL_TEST_POWER': -49,
    'LOSE_FACTOR': 2.2,
  },

  # Constants for connecting to MQTT broker
  'MQTT': {
    'HOST': "192.168.43.52",
    'PORT': 1883,
    'USERNAME': "test",
    'PASSWORD': "123456",
    'TOPIC': "maircom_tag_scanner/#",
  },

  # Constants for computing person position
  'COMPUTER': {
    # 'LAYOUT_FILE': './tools/map_create/output/test.json',
    'LAYOUT_FILE': '.\\tools\\map_create\\output\\build8_ass.json',
    'VIEW_FILE': '..\\sketches\\map_sketch\\sketch1.svg',
    'HISTORY_INTERVAL': 3,
  },

  # Constants for redis connection
  'REDIS': {
    'HOST': "localhost",
    'PORT': 6379,
    'DB': 0,
    'PASSWORD': None,
  },
}