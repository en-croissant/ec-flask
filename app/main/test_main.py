def test_home(api):
    """connects to root route"""
    app = api.get('/')
    assert app.get_data() == b'<h1>Hello world</h1>'
