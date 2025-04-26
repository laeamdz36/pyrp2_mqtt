"""Module to publish data with MQTT"""

from time import sleep
import paho.mqtt.client as mqtt
from get_data import read_sensor, get_cpu_temp

BROKER = "192.168.68.109"
PORT = 1883
username = "mqtt_usr"
password = "luismdz366"


def load_topics(selector=None):
    """Return topic selected"""

    # build topics for each sensor
    _topics = None
    if selector is None:
        _topic = "rp2/weather"
        _names = ["temperature", "humidity", "pressure"]
        _topics = {_name: {"topic": _top} for _name,
                   _top in zip(_names, [f"{_topic}/{x}" for x in _names])}
    return _topics


def create_mqtt_client():
    """Create MQTT client to connection"""

    client = mqtt.Client()
    client = mqtt.Client(client_id="rp2")
    client.username_pw_set(username, password)
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    return client


def main():
    """Execute continous comm to broker"""

    client = create_mqtt_client()
    _topics = load_topics()
    try:
        while True:
            data = read_sensor()
            cputemp = get_cpu_temp()
            if cputemp:
                client.publish("rp2/system/cpu_temp", cputemp)
            print(f"PUB: rp2/system/cpu_temp - {cputemp}")
            for sensor, value in data.items():
                client.publish(_topics.get(sensor)["topic"], value)
                print(
                    f"Pub topic: {_topics.get(sensor)["topic"]}, val: {value}")
            sleep(5)
    except Exception as e:
        print(f"ERROR: {e.args}")


if __name__ == "__main__":
    # pub_topic()
    # test topic builder
    main()
