import paho.mqtt.client as mqtt
from datetime import datetime

# Global counter
message_count = 0
start_time = None

# Define the callback function for when a message is received
def on_message(client, userdata, msg):
    global message_count, start_time
    if start_time is None:
        start_time = datetime.now()
    
    message_count += 1
    if message_count % 10000 == 0:  # Progress update every 10000 messages
        print(f"Received {message_count} messages")

# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic", qos=1)  # Using QoS 1 for at least once delivery
    print(f"Listening for messages... Started at {datetime.now()}")

# Create a client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
broker = "127.0.0.1"
port = 1883

try:
    client.connect(broker, port, 60)
except Exception as e:
    print(f"Failed to connect to broker: {e}")
    exit(1)

try:
    # Start the loop to process callbacks
    client.loop_forever()
except KeyboardInterrupt:
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds() if start_time else 0
    print("\nSubscription interrupted by user")
    print(f"Total messages received: {message_count}")
    if duration > 0:
        print(f"Time taken: {duration:.2f} seconds")
        print(f"Average rate: {message_count/duration:.2f} messages/second")
    client.disconnect()