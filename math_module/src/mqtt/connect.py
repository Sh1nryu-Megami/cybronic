import paho.mqtt.client as mqtt
from paho.mqtt.enums import MQTTErrorCode
from .events import on_connect, on_disconnect, on_message, on_subscribe
from ..compute import Shared


def connect_mqtt(config: dict, shared: Shared) -> tuple[mqtt.Client, MQTTErrorCode]:
  HOST = config['MQTT']['HOST']
  PORT = config['MQTT']['PORT']
  TOPIC = config['MQTT']['TOPIC']
  USERNAME = config['MQTT']['USERNAME']
  PASSWORD = config['MQTT']['PASSWORD']

  print(f"Connecting to MQTT Broker {HOST}:{PORT}...")

  mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
  mqtt_client.on_connect = on_connect(TOPIC)
  mqtt_client.on_disconnect = on_disconnect
  mqtt_client.on_message = on_message
  mqtt_client.on_subscribe = on_subscribe(TOPIC)
  mqtt_client.username_pw_set(USERNAME, PASSWORD)
  mqtt_client.user_data_set({
    'config': config,
    'shared': shared,
  })

  mqtt_client.connect(HOST, PORT)
  status = mqtt_client.loop_start()

  return mqtt_client, status 
  

