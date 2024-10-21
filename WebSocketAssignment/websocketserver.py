import asyncio
import websockets
import random

async def handler(websocket, path):
    while True:
        try:
            # Receive a message from the client
            message = await websocket.recv()
            print(f"Received message: {message}")

            # Modify the message by appending a random number
            modified_message = f"{message} {random.randint(1, 100)}"
            print(f"Sending modified message: {modified_message}")

            # Send the modified message back to the client
            await websocket.send(modified_message)
        except websockets.ConnectionClosed:
            print("Connection closed")
            break

# Start the server
start_server = websockets.serve(handler, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
print("WebSocket server started")
asyncio.get_event_loop().run_forever()

