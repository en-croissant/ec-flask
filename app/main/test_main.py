def test_home(api):
    """connects to root route"""
    app = api.get('/')
    assert app.status == '200 OK'
    assert app.get_data() == b'<h1>Hello world</h1>'

def test_get_allusers(api):
    app = api.get('/users')
    assert app.status == '200 OK'
    assert b'user_id' in app.get_data()
