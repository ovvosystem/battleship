import random
from string import ascii_uppercase

from flask import Blueprint, render_template, request, flash, session
from flask_login import login_required, current_user

from server.apps.game import Game

views = Blueprint("views", __name__)

rooms = {}

def generate_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)

        if code not in rooms:
            return code

@views.route("/")
def home():
    """Renders the homepage
    
    Returns:
        template: index.html
    """
    return render_template("index.html", user=current_user)

@views.route("/play", methods=["GET", "POST"])
@login_required
def play():
    if request.method == "POST":
        create = request.form.get("create", False)
        join = request.form.get("join", False)
        code = request.form.get("code")
        if code:
            code = code.upper()
        room = None

        if join != False:
            if not code:
                flash("Please input a room code to join", category="error")
            elif code not in rooms:
                flash(f'No room of code "{code}"', category="error")
            room = code
        
        elif create != False:
            room = generate_code(6)
            game = Game()
            rooms[room] = {"players": 0, "game": game}
        
        session["room"] = room

    return render_template("play.html", user=current_user)