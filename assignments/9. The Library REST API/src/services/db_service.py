from src.db.in_memory import books
from src.models.book import Book


def get_books():
    return books


def get_book(book_id):
    for book in books:
        if book.get_id() == book_id:
            return book


def add_book(book):
    new_book = Book(book["title"], book["author"], book["isbn"], book["availability"],
                    book["publication_year"], book["genre"])
    books.append(new_book)
    return new_book


def borrow_book(book_id):
    borrowed_book = get_book(book_id)
    borrowed_book.set_availability(False)
    return borrowed_book


def return_book(book_id):
    returned_book = get_book(book_id)
    returned_book.set_availability(True)
    return returned_book


def remove_book(book_id):
    for book in books:
        if book.get_id() == book_id:
            books.remove(book)
            return book
