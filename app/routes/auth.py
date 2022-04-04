from flask import request, jsonify

from app.main import main
from app.controllers import auth

# Login route
@main.route("/auth/login", methods=["POST"])
def handle_login():
  if request.method=="POST":
    req = request.get_json()
    response, code = auth.login(req)
    return jsonify(response), code
  
# Registration route
@main.route("/auth/register", methods=["POST"])
def handle_reg():
  if request.method=="POST":
    req = request.get_json()
    response, code  = auth.register(req)
    return jsonify(response), code
