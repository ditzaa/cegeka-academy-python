from src.db.in_memory import books


def get_books():
    return books


def get_book(book_id):
    for book in books:
        if book.get_id() == book_id:
            return book


