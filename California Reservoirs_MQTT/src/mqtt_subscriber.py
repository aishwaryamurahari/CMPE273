import paho.mqtt.client as mqtt
import json
import os

# Initialize data storage
reservoir_data = {
    "oroville": [],
    "shasta": [],
    "sonoma": []
}

def save_data_to_file():
    with open("reservoir_data.json", "w") as f:
        json.dump(reservoir_data, f)

def on_message(client, userdata, message):
    topic = message.topic.split('/')[-1]
    payload = json.loads(message.payload.decode())
    if topic in reservoir_data:
        reservoir_data[topic].append(payload)
        print(f"Received data for {topic}: {payload}")
        save_data_to_file()  # Save updated data to file

def start_subscriber():
    client = mqtt.Client()
    client.connect("localhost", 1883)

    client.subscribe("/reservoirs/oroville")
    client.subscribe("/reservoirs/shasta")
    client.subscribe("/reservoirs/sonoma")

    client.on_message = on_message
    client.loop_start()
