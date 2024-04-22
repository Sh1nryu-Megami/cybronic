from paho.mqtt.enums import MQTTErrorCode
import sys
import asyncio
import signal
from src.compute import Shared
from src.compute import computer
from src.mqtt import connect_mqtt
from config import CONFIG


def raise_system_exit():
  raise SystemExit

def parseArgv() -> dict[dict]:
  arguments = {
    '-h': {
      'exists': False,
    }
  }
  
  for arg in sys.argv[1:]:
    if arg in arguments:
      arguments[arg]['exists'] = True

  return arguments

def main():
  args = parseArgv()

  if args['-h']['exists']:
    with open('help.txt', 'r') as f:
      help_text = f.read()
    
    print(help_text)
    sys.exit(0)

  # Creating asyncio event loop
  loop = asyncio.new_event_loop()
  
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
  
  # Registering signal handlers for interrupting the program execution
  stop_signals = (signal.SIGINT, signal.SIGTERM, signal.SIGABRT)

  try:
    for sig in stop_signals:
      loop.add_signal_handler(sig, raise_system_exit)
  except NotImplementedError:
    print(f"Unimplemented signal has tried to be handled")
  
  try:
    loop.run_until_complete(computer(CONFIG, shared))
    loop.run_forever()
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