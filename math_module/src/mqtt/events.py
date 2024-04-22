import paho.mqtt.client as mqtt
import paho.mqtt.reasoncodes as reasoncodes
import typing
import json
from ..compute import Shared
from ..calc import get_distance

def on_connect(topic: str) -> typing.Callable[[mqtt.Client, reasoncodes.ReasonCode], None]:
  def on_connect_cb(client: mqtt.Client, userdata, connect_flags, reason_code: reasoncodes.ReasonCode, properties):
    if reason_code.is_failure:
      print(f"Failed to connect to MQTT Broker with result code {reason_code}.")
      return
    
    print(f"Connected to MQTT Broker with result code {reason_code}.")
    print("")
    client.subscribe(topic, qos=2)
  
  return on_connect_cb


def on_subscribe(topic: str) -> typing.Callable[[], None]:
  def on_subscribe_cb(client, userdata, mid, reason_code_list, properties):
    print(f"Subscribed to topic {topic}.")

  return on_subscribe_cb


def on_message(client, user_data: dict, message: mqtt.MQTTMessage):
  CALC = user_data['config']['CALC']
  lock = user_data['shared'].lock
  payload = json.loads(message.payload)

  lock.acquire()
  user_data['shared'].input_queue.append({
    'distance': get_distance(payload['rs'], payload['r1'], CALC),
    'device': payload['mc'],
    'lighthouse': message.topic.split('/')[1],
  })
  # print(len(user_data['shared'].input_queue))
  lock.release()

  print(f"Lighthouse: {message.topic.split('/')[1]}; Distance to {payload['mc']} is {round(get_distance(payload['rs'], payload['r1'], CALC) * 1000) / 1000}m", end="\r")



def on_disconnect(client, userdata, disconnect_flags, reason_code: reasoncodes.ReasonCode, properties):
  print(f"Disconnected from MQTT Broker with result code {reason_code}.")