from flask import Flask, request, jsonify, Blueprint
from flask_socketio import SocketIO, emit 
import secrets
from werkzeug import exceptions
from flask_cors import CORS

from app.models import Users

main = Blueprint('main', __name__) 
CORS(main)

# secret_key = secrets.token_hex(16)
# main.config['SECRET_KEY'] = secret_key
# socket = SocketIO(main, cors_allowed_origins="*")

@main.route("/")
def home_view():
        return "<h1>Hello world</h1>"

@main.route('/users', methods=['GET','POST'])
def getAllUsers():
    if request.method == 'GET':
        try: 
            allUsers = Users.query.all()
            return  jsonify([e.serialize() for e in allUsers])
        except exceptions.NotFound:
            raise exceptions.NotFound("There are no users currently!")
        except:
            raise exceptions.InternalServerError()

# @socket.on('connect')
# def test_connect():
#     emit('hello world', {'data': 'hello world'})


# if __name__ == '__main__':
#     socket.run(main)
