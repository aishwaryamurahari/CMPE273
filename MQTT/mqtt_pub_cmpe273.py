import time
import paho.mqtt.client as mqtt
from datetime import datetime

# Define the callback function for when a message is published
def on_publish(client, userdata, mid, properties=None):
    global message_count
    message_count += 1
    if message_count % 10000 == 0:  # Progress update every 10000 messages
        print(f"Published {message_count} messages")

# Global counter
message_count = 0

# Create a client instance
client = mqtt.Client()

# Assign the callback function
client.on_publish = on_publish

# Connect to the broker
broker = "127.0.0.1"
port = 1883

try:
    client.connect(broker, port, 60)
except Exception as e:
    print(f"Failed to connect to broker: {e}")
    exit(1)

# Start the loop in a non-blocking way
client.loop_start()

topic = "test/topic"
total_messages = 1000000

print(f"Starting message publication at {datetime.now()}")
start_time = time.time()

try:
    for i in range(total_messages):
        msg = f"Message {i+1} from IoT sensor"
        info = client.publish(
            topic,
            payload=msg.encode('utf-8'),
            qos=1,  # Using QoS 1 for at least once delivery
        )
        info.wait_for_publish()
        
        # Optional: Add a tiny sleep to prevent overwhelming the broker
        if i % 1000 == 0:
            time.sleep(0.001)

except KeyboardInterrupt:
    print("\nPublication interrupted by user")
except Exception as e:
    print(f"Error during publication: {e}")
finally:
    end_time = time.time()
    duration = end_time - start_time
    print(f"\nPublication completed at {datetime.now()}")
    print(f"Total messages published: {message_count}")
    print(f"Time taken: {duration:.2f} seconds")
    print(f"Average rate: {message_count/duration:.2f} messages/second")
    
    # Clean up
    client.loop_stop()
    client.disconnect()