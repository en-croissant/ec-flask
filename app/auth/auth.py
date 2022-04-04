from flask import request, jsonify, Blueprint
from flask_cors import CORS
from werkzeug import exceptions
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt

from app.models import Users
from app.extensions import db

auth = Blueprint('auth', __name__) 
CORS(auth)
# Bcrypt(auth)

# from app.models import User

# Login route
@auth.route("/auth/login", methods=["POST"])
def login():
    if request.method=="POST":
        try:
            req = request.get_json()
            if not req['username']:
                raise exceptions.BadRequest('No username provided')
            if not req['password']:
                raise exceptions.BadRequest('No password provided')
            
            user = Users.query.get(username=req['username'])
            
            authed = check_password_hash(user.password_digest, req['password'])
            if not authed:
                # Raise error if user is unauthorized (incorrect password)
                pass
            token = user.encode_auth_token(user.username)
            if token:
                response = {
                    'success': True,
                    'token': 'Bearer ' + token.decode('UTF-8')
                }
                return jsonify(response), 200
            
        except exceptions.BadRequest:
            # Be specific about the error
            # Might not even need to catch errors here as they get caught automatically by the error handle routes
            # Are the error handling routes being correctly imported?
            raise exceptions.BadRequest()
        except:
            raise exceptions.InternalServerError()
  
# Registration route
@auth.route("/auth/register", methods=["POST"])
def register():
    if request.method=="POST":
        try:
            req = request.get_json()
            newUsername = req['username']
            # newEmail = req['email']
            newPass = req['password']
            
            user = Users.query.get(username=newUsername)
            if user:
                return jsonify('Username already exists!'), 202
            
            hash = generate_password_hash(newPass)
            print(hash)
            print(hash.length)
            new_user = Users(
                username = req['username'],
                email = req['email'], 
                password_digest = hash,
                rank = 0
            )
            db.session.add(new_user)
            db.session.commit()
            
            return jsonify(f"New user was added!"), 201
        
        except:
            raise exceptions.InternalServerError()

@auth.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@auth.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@auth.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500
