#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 14:42:51 2023

@author: user
"""

import pika

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue where messages will be sent
channel.queue_declare(queue='hello')

# Loop to send 10,0000 messages
for i in range(100000):
    message = f"Hello World! Message {i+1}"
    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent '{message}'")

# Close the connection
connection.close()
