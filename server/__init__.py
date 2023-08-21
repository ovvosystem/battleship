from os import environ as env

from dotenv import find_dotenv, load_dotenv
from flask import Flask

from server.views import views

# Loads environment variables
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

def create_app():
    """Creates and configures the app
    
    Returns:
        object (Flask): app
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = env.get("SECRET_KEY")
    app.register_blueprint(views, url_prefix="/")

    return app