from flask import Flask, jsonify
from src.config import Config
from src.controllers.api_controller import api_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(api_blueprint)

    return app
