import paho.mqtt.client as mqtt
import json
import time

# MQTT broker configuration
BROKER_HOST = "localhost"
BROKER_PORT = 1883

# Define reservoir topics
topics = {
    "Oroville": "/reservoirs/oroville",
    "Shasta": "/reservoirs/shasta",
    "Sonoma": "/reservoirs/sonoma"
}

def publish_data(client, topic, data):
    client.publish(topic, json.dumps(data))
    print(f"Published data to topic {topic}")

if __name__ == "__main__":
    client = mqtt.Client()
    client.connect(BROKER_HOST, BROKER_PORT)

    # Load JSON data for each reservoir and publish it
    for reservoir, topic in topics.items():
        file_path = f"./data/{reservoir}_WML,.json"
        with open(file_path) as f:
            data = json.load(f)
        
        for record in data:
            publish_data(client, topic, record)
            time.sleep(1) 
