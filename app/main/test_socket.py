import chess

def test_home(sock):
    """connects to api"""
    sock.connect()
    assert sock.get_received()[0]['name'] == "hello world"

def test_create_board(sock):
    """creates a fresh chessboard"""
    sock.connect()
    sock.emit('create board', {'settings': 'default'})
    assert chess.Board().board_fen() == sock.get_received()[1]['args'][0]['chessboard']

def test_move(sock):
    """recieves move"""
    sock.connect()
    sock.emit('create board', 'default')
    sock.emit('move piece', {'data': 'e4'})
    assert 'e4' == sock.get_received()[2]['args'][0]['chess move']

def test_reset_board(sock):
    """resets the boards state"""
    sock.connect()
    sock.emit('create board', 'default')
    sock.emit('reset board')
    assert chess.Board().board_fen() == sock.get_received()[-1]['args'][0]['chessboard']


