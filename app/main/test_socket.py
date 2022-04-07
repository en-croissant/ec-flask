import chess

def test_home(sock):
    """connects to api"""
    sock.connect()
    assert sock.get_received()[0]['name'] == "hello world"

def test_create_board(sock):
    """creates a fresh chessboard"""
    sock.connect()
    sock.emit('join', {"lobby_id":'default'})
    assert chess.Board().fen() == sock.get_received()[1]['args'][0]['board']

def test_move(sock):
    """recieves move"""
    sock.connect()
    sock.emit('join', {"lobby_id":'default'})
    move = {'color': 'w', 'from': 'e2', 'to': 'e4', 'flags': 'b', 'piece': 'p', 'san': 'e4'}
    sock.emit('move piece', {'move': move})
    assert len(list(sock.get_received())) > 0
def test_reset_board(sock):
    """resets the boards state"""
    sock.connect()
    sock.emit('join', {"lobby_id":'default'})
    sock.emit('reset board')
    assert chess.Board().fen() == sock.get_received()[-1]['args'][0]['chessboard']


