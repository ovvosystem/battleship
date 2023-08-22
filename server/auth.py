from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash

from server.models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")

    if len(username) < 4:
        flash("Username must be at least 4 characters long", category="error")
    elif len(password) < 8:
        flash("Password must be at least 8 characters long", category="error")
    elif password != confirm_password:
        flash("Passwords don't match", category="error")
    else:
        new_user = User(username=username, 
                        password=generate_password_hash(password, method="sha256"))
        try:
            db.session.add(new_user)
            db.session.commit()

            flash("Account created!", category="success")
            return redirect("/")
        except:
            flash("An error occurred saving the user to database")

    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")