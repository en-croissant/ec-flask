from .. import socketio
from flask_socketio import emit

def test():
    @socketio.on('connect')
    def test_connect():
        emit('hello world', {'data': 'hello world'})


