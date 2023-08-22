from flask import Blueprint, render_template, request, flash

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
        flash("Account created!", category="success")
        return render_template("index.html")

    return render_template("register.html")

@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")