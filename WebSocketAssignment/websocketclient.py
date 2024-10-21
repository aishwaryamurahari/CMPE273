from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import websocket
import threading

app = Flask(__name__)
socketio = SocketIO(app)

messages = []  # Store WebSocket messages here

def on_message(ws, message):
    global messages
    messages.append(message)
    socketio.emit('new_message', {'message': message})  # Send message to UI

def run_websocket_client():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:6789/",
                                on_message=on_message)
    ws.run_forever()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Run WebSocket client in a separate thread
    threading.Thread(target=run_websocket_client).start()
    socketio.run(app, port=5000)
