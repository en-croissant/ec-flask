from .. import socketio
from flask_socketio import emit, join_room
import chess
from app.models import Lobby

def chess_game():
    @socketio.on('connect')
    def test_connect():
        emit('hello world', {'data': 'hello world'})

    @socketio.on('join')
    def test_join(data):
        # when user joins a room they get the latest board state
        room = data["lobby_id"]
        join_room(room)
        
        # Get lobby info
        match_info = Lobby.query.filter_by("lobby_id"==room).first()
        match_history = match_info['history']
        player_1 = match_info['player_1_key']
        player_2 = match_info['player_2_key']

        # Get latest board state
        board = chess.Board()
        emit('inital board', {'board':board.board_fen})

        # [TODO] Checks if it is user's turn to move
        #data['user_id']

        @socketio.on('move piece')
        def test_move(data):
            # [TODO] Check if it is the player's turn

            # Save move to history

            board.push_san(data['data'])
            # [NOTE] Check how to format match history correctly
            #Lobby.query.get({"lobby_id":room}).update({"history":f"{match_history},{data['data']}"})
            
            # Check for checkmate
            if board.is_checkmate():
                # end game
                pass
            # Broadcasts move to all users in room
            emit('opponent move', {'chess move': data['data']}, to=room)

        @socketio.on('reset board')
        def test_reset_board():
            board.reset()
            emit('new board', {'chessboard': board.board_fen()})

