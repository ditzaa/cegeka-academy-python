from flask import Blueprint
from src.config import Config

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/', methods=['GET'])
def get_api():
    return f"API version {Config.VERSION}"
