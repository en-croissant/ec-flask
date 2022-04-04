from .extensions import db 


# psql postgresql://yaegrrmpgbwrti:ec575d01211bf2d06c70954781406007730dd6efc093eecb12972f44c9c530f7@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/dcqpm3ubt7k4mk


# DROP TABLE IF EXISTS users;
# CREATE TABLE users (
#     user_id serial PRIMARY KEY,
#     username varchar(100),
#     email varchar(100),
#     password_digest varchar(100),
#     rank int
# );

# INSERT INTO users (username, email, password_digest, rank) VALUES ('test', 'test@test.com', 'test', 4);

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password_digest = db.Column(db.String(100))
    rank = db.Column(db.Integer)

    def __init__(self, username, email, password_digest, rank):
        self.username = username
        self.email = email
        self.password_digest = password_digest
        self.rank = rank

    
    def __repr__(self):
        return '<id {}>'.format(self.user_id)
    
    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username, 
            'email': self.email,
            'password_digest': self.password_digest,
            'rank': self.rank
    }

class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password_digest = db.Column(db.String(100))

    def __init__(self, username, email, password_digest):
        self.username = username
        self.email = email
        self.password_digest = password_digest

    
    def __repr__(self):
        return '<id {}>'.format(self.admin_id)
    
    def serialize(self):
        return {
            'admin_id': self.admin_id,
            'username': self.username, 
            'email': self.email,
            'password_digest': self.password_digest
    }

class Lobby(db.Model):
    lobby_id = db.Column(db.Integer, primary_key=True)
    player_1_key = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    player_2_key = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    history = db.Column(db.String(50000))

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


