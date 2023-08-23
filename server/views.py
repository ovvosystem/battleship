from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

rooms = {}

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

        if join != False and not code:
            flash("Please input a room code to join", category="error")
        elif join != False and code not in rooms:
            flash(f'No room of code "{code}"', category="error")

    return render_template("play.html", user=current_user)