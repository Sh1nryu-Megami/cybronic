from paho.mqtt.enums import MQTTErrorCode
import sys
import asyncio
import os
import json
from src.compute import Shared
from src.compute import computer
from src.mqtt import connect_mqtt
from src.db import connect_redis


def raise_system_exit():
  raise SystemExit


async def main_loop(CONFIG: dict, shared: Shared) -> None:
  await asyncio.gather(
    computer(CONFIG, shared),
    connect_redis(CONFIG, shared)
  )


def main():
  try:
    with open("./config.json", 'r') as f:
      CONFIG = json.loads(f.read())
  except FileNotFoundError:
    print("ERROR: config.json file not found")
    sys.exit(1)
  
  # Creating asyncio event loop
  loop = asyncio.new_event_loop()
  
  if os.environ.get('DBHOST') != None:
    CONFIG['REDIS']['HOST'] = os.environ.get('DBHOST')
  if os.environ.get('MQTTHOST') != None:
    CONFIG['MQTT']['HOST'] = os.environ.get('MQTTHOST')
  
  MQTT_HOST = CONFIG['MQTT']['HOST']
  MQTT_PORT = CONFIG['MQTT']['PORT']

  shared = Shared()

  # Start the MQTT client
  mqtt_client, mqtt_status = connect_mqtt(CONFIG, shared)

  if mqtt_status == MQTTErrorCode.MQTT_ERR_SUCCESS:
    print(f"Connected to MQTT broker at {MQTT_HOST}:{MQTT_PORT}")
  else:
    print(f"Failed to connect to MQTT broker at {MQTT_HOST}:{MQTT_PORT} with error code {mqtt_status}")
    sys.exit(1)
  
  try:
    loop.run_until_complete(main_loop(CONFIG, shared))
  except (KeyboardInterrupt, SystemExit):
    print("Tring to stop program execution")

    # Disconnect from MQTT broker
    mqtt_status = mqtt_client.disconnect()

    if mqtt_status == MQTTErrorCode.MQTT_ERR_SUCCESS:
      print(f"Disconnected from MQTT broker at {MQTT_HOST}:{MQTT_PORT}")
    else:
      print(f"Failed to disconnect from MQTT broker at {MQTT_HOST}:{MQTT_PORT} with error code {mqtt_status}")
      sys.exit(1)
    
    # Stopping all the corutines
    shared.event_stop.set()


if __name__ == "__main__":
  main()