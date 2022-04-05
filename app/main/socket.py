from .. import socketio
from flask_socketio import emit
import chess  

def chess_game():
    @socketio.on('connect')
    def test_connect():
        emit('hello world', {'data': 'hello world'})

    @socketio.on('create board')
    def test_create_board(settings):
        board = chess.Board()
        emit('new game', {'chessboard': board.board_fen()})
        
        @socketio.on('move piece')
        def test_move(data):
            board.push_san(data['data'])
            emit('opponent move', {'chess move': data['data']})

        @socketio.on('reset board')
        def test_reset_board():
            board.reset()
            emit('new board', {'chessboard': board.board_fen()})

