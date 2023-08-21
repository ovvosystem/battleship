import os

from flask import Flask

from server.views import views


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix="/")

    return app