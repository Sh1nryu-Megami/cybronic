import math


def get_distance(rssi: int, tx: int, consts: dict) -> int:
  LIGHTHOUSE_TEST_DISTANCE = 1
  SIGNAL_TEST_POWER = tx
  LOSE_FACTOR = consts['LOSE_FACTOR']

  return LIGHTHOUSE_TEST_DISTANCE * 10 ** ((SIGNAL_TEST_POWER - rssi) / (10 * LOSE_FACTOR))
  # ratio = rssi / tx

  # if ratio < 1:
  #   return math.pow(ratio, 10)
  # else:
  #   return 0.89976 * math.pow(ratio, 7.7095) + 0.111