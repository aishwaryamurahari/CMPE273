#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consumer Script
"""

import pika

# Callback function to handle messages received from the queue
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue from which messages will be consumed
channel.queue_declare(queue='hello')

# Set up subscription on the queue
channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
