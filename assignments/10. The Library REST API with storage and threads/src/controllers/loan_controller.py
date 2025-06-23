from src.services.books_service import get_book
from src.services.loans_service import loan_book, log_borrowing_state, return_book
from src.services.users_service import get_user
from flask import blueprints, jsonify, request
from src.models.user import User

loan_blueprint = blueprints.Blueprint('loans', __name__)


@loan_blueprint.route('/loans/<int:subscriber_id>', methods=['POST'])
def post_loan_book(subscriber_id):
    json_data = request.get_json()
    book_id = json_data.get('book_id')
    admin_id = json_data.get('admin_id')

    admin = get_user(admin_id)
    if admin.role != 'admin':
        return jsonify({'error': 'Unauthorized user tried to loan a book'}), 403

    user = get_user(subscriber_id)
    if user.role != 'subscriber':
        return jsonify({'error': 'Target user must be a subscriber'}), 400

    book = get_book(book_id)
    if not book:
        return jsonify({'error': 'Book not found in library'}), 404

    if book.get_no_loaned_books() == book.get_no_copies():
        return jsonify({'error': 'No more copies of the book available'}), 409

    if user.get_no_borrowed_books() == User.get_borrowing_limit():
        return jsonify({'error': 'User has reached limit of borrowed books'}), 400

    loan = loan_book(book_id, subscriber_id)
    if loan == 0:
        return jsonify({'error': 'Book already loaned to the user'}), 400

    return jsonify({
        'message': 'Book successfully returned',
        'book_id': book_id,
        'admin_id': admin_id,
        'subscriber_id': subscriber_id,
    }), 200


@loan_blueprint.route('/returns/<int:subscriber_id>', methods=['POST'])
def post_return_book(subscriber_id):
    json_data = request.get_json()
    book_id = json_data.get('book_id')
    admin_id = json_data.get('admin_id')

    admin = get_user(admin_id)
    if admin.role != 'admin':
        return jsonify({'error': 'Unauthorized user tried to return a book'}), 403

    user = get_user(subscriber_id)
    if user.role != 'subscriber':
        return jsonify({'error': 'Target user must be a subscriber'}), 400

    result = return_book(book_id, subscriber_id)
    if result is None:
        return jsonify({'error': 'User or book not found'}), 404
    if result == 0:
        return jsonify({'error': 'User has not borrowed this book'}), 400

    return jsonify({
        'message': 'Book successfully returned',
        'book_id': book_id,
        'admin_id': admin_id,
        'subscriber_id': subscriber_id,
    }), 200


@loan_blueprint.route('/loans/test/<int:user_id>', methods=['GET'])
def test_loan(user_id):
    log_borrowing_state(user_id)
    return jsonify({"tested": "yes"}), 200
