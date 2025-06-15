from src.services.db_service import get_books, get_book, add_book, borrow_book, return_book, remove_book
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
    if book:
        json_data = book.to_json_dict()
        return jsonify(json_data), 200
    return jsonify({"error": "Book not found"}), 404


@book_blueprint.route('/books', methods=['POST'])
def post_book():
    book = request.get_json()
    if book:
        new_book = add_book(book)
        new_book = new_book.to_json_dict()
        return jsonify(new_book), 200
    return jsonify({"error": "Book could not be added"}), 404


@book_blueprint.route('/books/borrow/<int:book_id>', methods=['PATCH'])
def patch_borrow_book(book_id):
    borrowed_book = borrow_book(book_id)
    if borrowed_book:
        borrowed_book = borrowed_book.to_json_dict()
        return jsonify(borrowed_book), 200
    return jsonify({"error": "Book could not be borrowed"}), 400


@book_blueprint.route('/books/return/<int:book_id>', methods=['PATCH'])
def patch_return_book(book_id):
    returned_book = return_book(book_id)
    if returned_book:
        returned_book = returned_book.to_json_dict()
        return jsonify(returned_book), 200
    return jsonify({"error": "Book could not be returned"}), 400


@book_blueprint.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    deleted_book = remove_book(book_id)
    if deleted_book:
        deleted_book = deleted_book.to_json_dict()
        return jsonify(deleted_book), 200
    return jsonify({"error": "Book could not be deleted"}), 404
