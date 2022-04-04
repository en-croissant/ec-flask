def test_home(sock):
    """connects to api"""
    sock.connect()
    assert sock.get_received()[0]['name'] == "hello world"
