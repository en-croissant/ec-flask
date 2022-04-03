from flask import request, jsonify

from app import app
from app.controllers import auth

# Login route
@app.route("/auth/login", methods=["POST"])
def handle_login():
  if request.method=="POST":
    response, code = auth.login(request)
    return jsonify(response), code
  
# Registration route
@app.route("/auth/register", methods=["POST"])
def handle_reg():
  if request.method=="POST":
    response, code  = auth.register(request)
    return jsonify(response), code
