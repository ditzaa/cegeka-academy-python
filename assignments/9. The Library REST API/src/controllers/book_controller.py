from src.services.db_service import get_books
from flask import blueprints, jsonify, request

book_blueprint = blueprints.Blueprint('book', __name__)


@book_blueprint.route('/books', methods=['GET'])
def get_books_list():
    books = get_books()
    json_data = [book.to_json_dict() for book in books]
    return jsonify(json_data), 200
