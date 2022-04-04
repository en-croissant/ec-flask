from flask import Flask, request, jsonify, Blueprint
from flask_socketio import SocketIO, emit 


from .. import socketio

@socketio.on('connect')
def test_connect():
    emit('hello world', {'data': 'hello world'})
