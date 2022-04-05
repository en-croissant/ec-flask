import json
from unittest import mock
import werkzeug.security as security

def test_register(api):
    new_user_data = json.dumps({'username': "ulakbhvluadhbvo", 'email': "test@email.com", 'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    
    app= api.post('/auth/register', data = new_user_data, headers=mock_headers)
    assert app.status == '201 CREATED'
    
def test_register_with_taken_username(api):
    new_user_data = json.dumps({'username': "test", 'email': "test@email.com", 'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/auth/register', data = new_user_data, headers=mock_headers)
    assert app.status == '202 ACCEPTED'

def test_login(api):
    user_data = json.dumps({'username': "test",'password': 'test'})
    mock_headers = {'Content-Type': 'application/json'}
    
    app= api.post('/auth/login', data=user_data, headers=mock_headers)
    print(app)
    assert app.status == '200 CREATED'
    
def test_login_with_incorrect_password(api):
    user_data = json.dumps({'username': "test",'password': 'AJSDGOUADVOUSHBV'})
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/auth/login', data=user_data, headers=mock_headers)
    print(app)
    assert app.status == '401 UNAUTHORIZED'
