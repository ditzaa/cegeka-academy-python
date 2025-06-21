from src.services.books_service import get_books, get_book, add_book, borrow_book, return_book, remove_book
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


@book_blueprint.route('/books/borrow/<int:book_id>', methods=['PATCH'])
def patch_borrow_book(book_id):
    book = get_book(book_id)
    if book.get_no_copies() == 0:
        return jsonify({"error": "Book has no copies available"}), 400
    borrowed_book = borrow_book(book_id)
    if not borrowed_book:
        return jsonify({"error": "Book could not be borrowed"}), 400

    borrowed_book = borrowed_book.to_json_dict()
    return jsonify(borrowed_book), 200


@book_blueprint.route('/books/return/<int:book_id>', methods=['PATCH'])
def patch_return_book(book_id):
    book = get_book(book_id)
    returned_book = return_book(book_id)
    if not returned_book:
        return jsonify({"error": "Book could not be returned"}), 400
    returned_book = returned_book.to_json_dict()
    return jsonify(returned_book), 200


@book_blueprint.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    deleted_book = remove_book(book_id)
    if not deleted_book:
        return jsonify({"error": "Book could not be deleted"}), 404
    deleted_book = deleted_book.to_json_dict()
    return jsonify(deleted_book), 200
