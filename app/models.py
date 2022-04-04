import datetime
import jwt

from .extensions import db 

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password_digest = db.Column(db.String(100))
    rank = db.Column(db.Integer)
    admin = db.Column(db.Boolean)

    def __init__(self, username, email, password_digest, rank, admin=False):
        self.username = username
        self.email = email
        self.password_digest = password_digest
        self.rank = rank
        self.admin = admin

    
    def __repr__(self):
        return '<id {}>'.format(self.user_id)
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username, 
            'email': self.email,
            'password_digest': self.password_digest,
            'rank': self.rank,
            'admin': self.admin
    }


class Lobby(db.Model):
    lobby_id = db.Column(db.Integer, primary_key=True)
    player_1_key = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    player_2_key = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    history = db.Column(db.String(50000))

    # history should be array

    def __init__(self, player_1_key, player_2_key, history):
        self.player_1_key = player_1_key
        self.player_2_key = player_2_key
        self.history = history

    def __repr__(self):
        return '<id {}>'.format(self.lobby_id)
    
    def serialize(self):
        return {
            'lobby_id': self.lobby_id,
            'player_1_key': self.player_1_key, 
            'player_2_key': self.player_2_key,
            'history': self.history
    }

class Chat(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    lobby_id = db.Column(db.Integer, db.ForeignKey('lobby.lobby_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    message = db.Column(db.String(500))
    time = db.Column(db.DateTime)

    def __init__(self, user_id, lobby_id, message, time):
        self.lobby_id = lobby_id
        self.user_id = user_id
        self.message = message
        self.time = time

    def __repr__(self):
        return '<id {}>'.format(self.message_id)
    
    def serialize(self):
        return {
            'message_id': self.message_id,
            'lobby_id': self.lobby_id,
            'user_id': self.user_id, 
            'message': self.message,
            'time': self.time
    }



