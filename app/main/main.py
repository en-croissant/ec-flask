from flask import Flask, request, jsonify, Blueprint
# from flask_socketio import SocketIO, emit 
# import secrets
from werkzeug import exceptions
from flask_cors import CORS

from app.models import Users, Admin, Lobby, Chat
from app.extensions import db

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
    elif request.method == 'POST':
        try:
            req = request.get_json()
            new_user = Users(
                username = req['username'],
                email = req['email'], 
                password_digest = req['password_digest'],
                rank = req['rank']
            )

            db.session.add(new_user)
            db.session.commit()
            return f"New user was added!", 201

        except: 
            raise exceptions.InternalServerError()

@main.get('/users/<int:user_id>')
def getUserById(user_id):
    try: 
        user = Users.query.get_or_404(user_id)
        return  jsonify([user.serialize()])
    except exceptions.NotFound:
        raise exceptions.NotFound("User not found!")
    except:
        raise exceptions.InternalServerError()




@main.route('/admins', methods=['GET','POST'])
def getAllAdmins():
    if request.method == 'GET':
        try: 
            allAdmins = Admin.query.all()
            return  jsonify([e.serialize() for e in allAdmins])
        except exceptions.NotFound:
            raise exceptions.NotFound("There are no admins currently!")
        except:
            raise exceptions.InternalServerError()
    elif request.method == 'POST':
        try:
            req = request.get_json()
            new_admin = Admin(
                username = req['username'],
                email = req['email'], 
                password_digest = req['password_digest'],
            )

            db.session.add(new_admin)
            db.session.commit()
            return f"New admin was added!", 201

        except: 
            raise exceptions.InternalServerError()





@main.route('/lobby', methods=['GET','POST'])
def getAllLobbies():
    if request.method == 'GET':
        try: 
            allLobby = Lobby.query.all()
            return  jsonify([e.serialize() for e in allLobby])
        except exceptions.NotFound:
            raise exceptions.NotFound("There are no lobbies to view at the moment!")
        except:
            raise exceptions.InternalServerError()

    elif request.method == 'POST':
        try:
            req = request.get_json()
            new_lobby = Lobby(
                player_1_key = req['player_1_key'],
                player_2_key = req['player_2_key'], 
                history = req['history'],
            )
            db.session.add(new_lobby)
            db.session.commit()
            return f"New lobby was added!", 201

        except: 
            raise exceptions.InternalServerError()




@main.route('/chat', methods=['GET','POST'])
def getAllChats():
    if request.method == 'GET':
        try: 
            allChats = Chat.query.all()
            return  jsonify([e.serialize() for e in allChats])
        except exceptions.NotFound:
            raise exceptions.NotFound("There are no chats!")
        except:
            raise exceptions.InternalServerError()

    elif request.method == 'POST':
        try:
            req = request.get_json()
            new_chat = Chat(
                lobby_id = req['lobby_id'],
                user_id = req['user_id'], 
                message = req['message'],
                time = req['time']
            )
            db.session.add(new_chat)
            db.session.commit()
            return f"New chat was added!", 201

        except: 
            raise exceptions.InternalServerError()














# @socket.on('connect')
# def test_connect():
#     emit('hello world', {'data': 'hello world'})


# if __name__ == '__main__':
#     socket.run(main)