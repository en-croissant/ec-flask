from .. import socketio
from flask_socketio import emit

def test():
    @socketio.on('connect')
    def test_connect():
        print("""
    WOW SO AMAZING
                """)
        emit('hello world', {'data': 'hello world'})


