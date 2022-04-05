def test_home(api):
    """connects to root route"""
    res = api.get('/')
    assert res.get_data() == b'<h1>Hello world</h1>'

