from os import path, environ as env

from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Load environment variables
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Database variables
db = SQLAlchemy()
DB_NAME = env.get("DB_NAME")

def create_app():
    """Creates and configures the app
    
    Returns:
        object (Flask): app
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = env.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from server.views import views
    from server.auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth/")

    from server.models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app


def create_database(app):
    """Creates database if it doesn't exist
    
    Returns:
        None
    """
    if not path.exists(f'instance/{DB_NAME}'):
        with app.app_context():
            db.create_all()
        print("Database Created")