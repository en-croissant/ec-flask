from .. import socketio
from flask_socketio import emit
import chess  

def chess_game():
    @socketio.on('connect')
    def test_connect():
        emit('hello world', {'data': 'hello world'})


