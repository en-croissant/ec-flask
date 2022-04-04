
from flask_socketio import emit 


from .. import socketio

@socketio.on('connect')
def test_connect():
    emit('hello world', {'data': 'hello world'})


