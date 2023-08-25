from flask import Blueprint, request, jsonify, session
from flask_login import current_user
from flask_socketio import join_room, leave_room, emit

from . import socketio
from server.views import rooms

api = Blueprint("api", __name__)


# Game events

def get_boards(room):
    game =  rooms[room]["game"]
    if current_user ==  rooms[room]["creator"]["user_id"]:
        return {"player_board": game.player1_board.get_board(),
                "opponent_board": game.player2_board.get_secret_board()}
    else:
        return {"player_board": game.player2_board.get_board(),
                "opponent_board": game.player1_board.get_secret_board()}


# SocketIO events

@socketio.on("connect")
def connect(auth):
    room = session.get("room")

    if room is None:
        return
    if room not in rooms:
        leave_room(room)
        return

    if  rooms[room]["creator"] != {} and current_user != rooms[room]["creator"]["user_id"]:
        if  rooms[room]["challenger"] != {} and current_user !=  rooms[room]["challenger"]["user_id"]:
            return
    
    join_room(room)

    if  rooms[room]["creator"] == {}:
         rooms[room]["creator"] = {"user_id": current_user, "session_id": request.sid}
    elif  rooms[room]["challenger"] == {}:
         rooms[room]["challenger"] = {"user_id": current_user, "session_id": request.sid}

    emit("update", get_boards(room), to=request.sid)