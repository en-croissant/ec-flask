from flask import Flask 
from .extensions import db
from .main.main import main
from .auth.auth import auth
from flask_socketio import SocketIO, emit

socketio = SocketIO()


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    socketio.init_app(app, cors_allowed_origins="*")

    # For some reason this is the only place I can put the import
    from .main.socket import chess_game
    chess_game()

    return app

