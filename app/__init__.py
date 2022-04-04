from flask import Flask 
from .extensions import db
from .main.main import main
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(main)
    socketio.init_app(app)

    return app

