from src.services.books_service import get_books, get_book, add_book, remove_book
from flask import blueprints, jsonify, request

book_blueprint = blueprints.Blueprint('book', __name__)


@book_blueprint.route('/books', methods=['GET'])
def get_books_list():
    books = get_books()
    json_data = [book.to_json_dict() for book in books]
    return jsonify(json_data), 200


@book_blueprint.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = get_book(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    json_data = book.to_json_dict()
    return jsonify(json_data), 200


@book_blueprint.route('/books', methods=['POST'])
def post_book():
    book = request.get_json()
    if not book:
        return jsonify({"error": "Book could not be added"}), 404
    books = get_books()
    if any(b.get_isbn() == book["isbn"] for b in books):
        return jsonify({"error": "Book already exists"}), 400
    new_book = add_book(book)
    new_book = new_book.to_json_dict()
    return jsonify(new_book), 200


@book_blueprint.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    deleted_book = remove_book(book_id)
    if not deleted_book:
        return jsonify({"error": "Book could not be deleted"}), 404
    deleted_book = deleted_book.to_json_dict()
    return jsonify(deleted_book), 200
