from flask import Flask
from flask_socketio import SocketIO, emit 
import secrets

app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key
socket = SocketIO(app)

@app.route("/")
def home_view():
        return "<h1>Hello world</h1>"

@socket.on('connect')
def test_connect():
    emit('hello world', {'data': 'hello world'})


if __name__ == '__main__':
    socket.run(app)
