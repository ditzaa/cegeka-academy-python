from config import Config
from flask import Flask, jsonify
from controllers.todo_controller import todo_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # register blueprint controllers
    app.register_blueprint(todo_blueprint)
    return app
