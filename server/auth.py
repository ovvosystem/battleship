from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from server.models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    """Renders the register page template and handles user registration
    
    On bad input, flashes an error message explaining what must be changed. 
    On success, hashes the password, adds user to the database and redirects the user to the
    homepage with a success message
    
    Returns:
        template/redirect: either returns the rendered template on GET or failure to register,
                           or redirects the user back to the homepage on successful registering
    """
    if request.method == "GET":
        return render_template("register.html", user=current_user)
    
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm-password")

    if User.query.filter_by(username=username).first():
        flash("Username already taken", category="error")
    elif " " in username:
        flash("Username cannot contain spaces", category="error")
    elif len(username) < 4:
        flash("Username must be at least 4 characters long", category="error")
    elif len(username) > 20:
        flash("Username cannot be longer than 20 characters", category="error")
    elif len(password) < 8:
        flash("Password must be at least 8 characters long", category="error")
    elif password != confirm_password:
        flash("Passwords don't match", category="error")
    else:
        new_user = User(username=username, 
                        password=generate_password_hash(password, method="scrypt"))
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            flash("Account created!", category="success")
            return redirect("/")
        except:
            flash("An error occurred saving the user to database")

    return render_template("register.html", user=current_user)

@auth.route("/login", methods=["GET", "POST"])
def login():
    """Renders the login page template and handles user login
    
    If inputted username and password correspond to a user in the database, logs in the user
    
    Returns:
        template/redirect: either returns the rendered template on GET or failure to login,
                           or redirects the user back to the homepage on successful login
    """
    if request.method == "GET":
        return render_template("login.html", user=current_user)
    
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user, remember=True)
            flash("Logged in succesfully!", category="success")
            return redirect("/")
        else:
            flash("Wrong password, try again", category="error")
    else:
        flash("Username does not exist", category="error")

    return render_template("login.html", user=current_user)

@auth.route("/logout")
@login_required
def logout():
    """Logs out the user
    
    Returns:
        redirect: redirect to the login page
    """
    logout_user()
    return redirect("/auth/login")