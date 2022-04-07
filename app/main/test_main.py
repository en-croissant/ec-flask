import json


def test_home(api):
    """connects to root route"""
    app = api.get('/')
    assert app.status == '200 OK'
    assert app.get_data() == b'<h1>Hello world</h1>'

def test_get_allusers(api):
    app = api.get('/users')
    assert app.status == '200 OK'
    assert b'user_id' in app.get_data()

def test_get_oneuser(api):
    app = api.get('/users/1')
    assert app.status == '200 OK'
    assert b'user_id' in app.get_data()

def test_get_oneuser_notfound(api):
    app = api.get('/users/100')
    assert app.status == '404 NOT FOUND'
    assert b'User not found' in app.get_data()

def test_get_alllobbies(api):
    app = api.get('/lobby')
    assert app.status == '200 OK'
    assert b'player_1_key' in app.get_data()


def test_get_onelobby(api):
    app = api.get('/lobby/1')
    assert app.status == '200 OK'
    assert b'lobby_id' in app.get_data()

def test_get_onelobby_notfound(api):
    app = api.get('/lobby/100')
    assert app.status == '404 NOT FOUND'
    assert b'Lobby not found' in app.get_data()



def test_get_allchats(api):
    app = api.get('/chat')
    assert app.status == '200 OK'
    assert b'message' in app.get_data()

def test_404(api):
    app = api.get('/gg')
    assert app.status == '404 NOT FOUND'



def test_post_lobby(api):
    lobby_data = json.dumps({'player_1_username': "noah", 'player_2_username': "test", 'history': 'history101'})
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/lobby', data = lobby_data, headers=mock_headers)
    assert app.status == '201 CREATED'



def test_post_chat(api):
    chat_data = json.dumps({'lobby_id': 1, 'user_id': 1, 'message': 'hello', 'time': '2022-04-05' })
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/chat', data = chat_data, headers=mock_headers)
    assert app.status == '201 CREATED'


def test_post_lobby_500(api):
    lobby_data = json.dumps({'player_1_key': 1, 'player_2_key': 2, 'historyy': 'history101'})
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/lobby', data = lobby_data, headers=mock_headers)
    assert app.status == '500 INTERNAL SERVER ERROR'


def test_post_chat_500(api):
    chat_data = json.dumps({'lobby_id': 1, 'user_id': 1, 'message': 'hello', 'timee': '2022-04-05' })
    mock_headers = {'Content-Type': 'application/json'}
    app= api.post('/chat', data = chat_data, headers=mock_headers)
    assert app.status == '500 INTERNAL SERVER ERROR'


