from os import environ as env

from dotenv import find_dotenv, load_dotenv
from flask import Flask

from server.views import views

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = env.get("SECRET_KEY")
    app.register_blueprint(views, url_prefix="/")

    return app