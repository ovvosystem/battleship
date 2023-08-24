from flask import Blueprint, request, jsonify, session
from flask_login import current_user
from flask_socketio import join_room, leave_room

from . import socketio
from server.views import rooms

api = Blueprint("api", __name__)

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