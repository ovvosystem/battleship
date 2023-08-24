from flask import Blueprint, request, jsonify, session
from flask_login import current_user
from flask_socketio import join_room, leave_room, emit

from . import socketio
from server.views import rooms

api = Blueprint("api", __name__)


# Game events

def get_boards(room):
    if current_user == rooms[room]["creator"]:
        game = rooms[room]["game"]
        return {"player_board": game.player1_board.get_board(),
                "opponent_board": game.player2_board.get_secret_board()}


# SocketIO events

@socketio.on("connect")
def connect(auth):
    room = session.get("room")

    if room is None:
        return
    if room not in rooms:
        leave_room(room)
        return
    if current_user != rooms[room]["creator"]:
        if rooms[room]["challenger"] == None:
            rooms[room]["challenger"] = current_user
        elif rooms[room]["challenger"] != current_user:
            return
    
    join_room(room)