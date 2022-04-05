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

def test_get_allchats(api):
    app = api.get('/chat')
    assert app.status == '200 OK'
    assert b'message' in app.get_data()

