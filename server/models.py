from flask_login import UserMixin

from . import db


class User(db.Model, UserMixin):
    """A class representing the user table in the database
    
    Attributes:
        id (Integer): column containing user ids, the primary key of the user table
        username (String): column containing usernames, must be unique
        password (String): column containing hashed passwords
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))