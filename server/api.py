from flask import Blueprint, request, jsonify, session
from flask_login import current_user
from flask_socketio import join_room, leave_room, emit

from . import socketio
from server.views import rooms

api = Blueprint("api", __name__)


# Game events

def get_boards(room, user):
    """Retrieves the correct board information for an user in a room
    
    Returns:
        dict: player and opponent's boards
    """
    game =  rooms[room]["game"]
    if user ==  rooms[room]["creator"]["user_id"]:
        return {"player_board": game.player1_board.get_board(),
                "opponent_board": game.player2_board.get_board()}
    elif user == rooms[room]["challenger"]["user_id"]:
        return {"player_board": game.player2_board.get_board(),
                "opponent_board": game.player1_board.get_board()}


# SocketIO events

@socketio.on("connect")
def connect(auth):
    room = session.get("room")
    user = current_user.get_id()

    # Check if room exists
    if room is None:
        return
    if room not in rooms:
        leave_room(room)
        return
    
    # Checks if the user is already connected or if the room is full
    if rooms[room]["creator"]: 
        if user == rooms[room]["creator"]["user_id"]:
            emit("update", get_boards(room, user), to=request.sid)
            return
        
        if rooms[room]["challenger"]:
            if user ==  rooms[room]["challenger"]["user_id"]:
                emit("update", get_boards(room, user), to=request.sid)
                return
            else: # Room is full
                return

    join_room(room)

    # Updates creator and challenger information when new user joins room
    if not rooms[room]["creator"]:
        rooms[room]["creator"] = {"user_id": user, "session_id": request.sid}
    elif not rooms[room]["challenger"]:
        rooms[room]["challenger"] = {"user_id": user, "session_id": request.sid}

    emit("update", get_boards(room, user), to=request.sid)