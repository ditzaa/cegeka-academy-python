from src.services.db_service import get_books, get_book
from flask import blueprints, jsonify

book_blueprint = blueprints.Blueprint('book', __name__)


@book_blueprint.route('/books', methods=['GET'])
def get_books_list():
    books = get_books()
    json_data = [book.to_json_dict() for book in books]
    return jsonify(json_data), 200


@book_blueprint.route('/book/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = get_book(book_id)
    if book:
        json_data = book.to_json_dict()
        return jsonify(json_data), 200
    return jsonify({"error": "Book not found"}), 404
