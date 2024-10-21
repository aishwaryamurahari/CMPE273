from flask import Flask, render_template
import threading
import websocket

app = Flask(__name__)

messages = []  # To store the WebSocket messages

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

def on_message(ws, message):
    global messages
    messages.append(message)

def on_open(ws):
    def run(*args):
        for i in range(10000):  # Send 10000 messages
            message = f"Hello {i}"
            ws.send(message)
        ws.close()
    threading.Thread(target=run).start()

def run_websocket_client():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:6789/",
                                on_open=on_open,
                                on_message=on_message)
    ws.run_forever()

if __name__ == '__main__':
    # Start WebSocket client in a separate thread
    threading.Thread(target=run_websocket_client).start()

    # Start Flask app
    app.run(port=5005)

