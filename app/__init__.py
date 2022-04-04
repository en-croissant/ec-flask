from flask import Flask 
# from flask_socketio import SocketIO, emit 

from .extensions import db
from .main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    # socket = SocketIO(app, cors_allowed_origins="*")

    # @socket.on('connect')
    # def test_connect():
    #   emit('hello world', {'data': 'hello world'})

    # socket.run(app)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(main)

    return app
