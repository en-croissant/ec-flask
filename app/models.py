from .extensions import db 

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
