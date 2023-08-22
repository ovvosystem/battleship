from os import environ as env

from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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
    app.register_blueprint(views, url_prefix="/")

    return app