CONFIG = {
  # Constants for calculating distance for person to lighthouse
  'CALC': {
    'LIGHTHOUSE_TEST_DISTANCE': 1,
    'SIGNAL_TEST_POWER': -49,
    'LOSE_FACTOR': 2.8,
  },

  # Constants for connecting to MQTT broker
  'MQTT': {
    'HOST': "192.168.1.149",
    'PORT': 1883,
    'USERNAME': "test",
    'PASSWORD': "123456",
    'TOPIC': "maircom_tag_scanner/#",
  },

  # Constants for computing person position
  'COMPUTER': {
    # 'LAYOUT_FILE': './tools/map_create/output/test.json',
    'LAYOUT_FILE': 'E:\\git\\cybronic\\math_module\\tools\\map_create\\output\\new_halls.json',
    'VIEW_FILE': 'E:\\git\\cybronic\\sketches\\map_sketch\\halls_view.svg',
    'HISTORY_INTERVAL': 3,
    'UPPER_BOUND': 12,
    'LOWER_BOUND': 0.3,
  },

  # Constants for redis connection
  'REDIS': {
    'HOST': "localhost",
    'PORT': 6379,
    'DB': 0,
    'PASSWORD': None,
  },
}