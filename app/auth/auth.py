from flask import request, jsonify, Blueprint
from flask_cors import CORS
from werkzeug import exceptions
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import Users
from app.extensions import db

auth = Blueprint('auth', __name__) 
CORS(auth)

# from app.models import User

# Login route
@auth.route("/auth/login", methods=["POST"])
def login():
    if request.method=="POST":
        try:
            req = request.get_json()
            username = req['username']
            password = req['password']
            
            if not username:
                raise exceptions.BadRequest('No username provided')
            if not password:
                raise exceptions.BadRequest('No password provided')
            
            user = Users.query.filter_by(username=username).first()
            
            authed = check_password_hash(user.password_digest, req['password'])
            if not authed:
                raise exceptions.Unauthorized('Incorrect password.')
            
            token = user.encode_auth_token(user.username)
            if token:
                print(1)
                response = {
                    'success': True,
                    'token': 'Bearer ' + token
                }
                return jsonify(response), 200
            
        except exceptions.BadRequest:
            # Be specific about the error
            # Might not even need to catch errors here as they get caught automatically by the error handle routes
            # Are the error handling routes being correctly imported?
            raise exceptions.BadRequest()
        except exceptions.Unauthorized:
            raise exceptions.Unauthorized('Incorrect password.')
        except:
            raise exceptions.InternalServerError()
  
# Registration route
@auth.route("/auth/register", methods=["POST"])
def register():
    if request.method=="POST":
        try:
            req = request.get_json()
            username = req['username']
            password = req['password']
            
            user = Users.query.filter('username'==username)
            if user:
                return jsonify('Username already exists!'), 202
            
            hash = generate_password_hash(password)
            
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
        
        
        
@auth.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400


@auth.errorhandler(exceptions.Unauthorized)
def handle_401(err):
    return {'message': f'Not authorized! {err}'}, 401


@auth.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404


@auth.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500
