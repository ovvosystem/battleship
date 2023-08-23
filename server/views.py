from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route("/")
def home():
    """Renders the homepage
    
    Returns:
        template: index.html
    """
    return render_template("index.html", user=current_user)

@views.route("/play")
def play():
    return render_template("play.html", user=current_user)