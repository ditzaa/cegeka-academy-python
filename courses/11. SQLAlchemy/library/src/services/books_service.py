from src.db import Session
from src.models.book import Book


def get_books():
    with Session() as session:
        books = session.query(Book).all()
        return books


def get_book(book_id):
    with Session() as session:
        book = session.query(Book).get(book_id)
        return book


def add_book(book_data):
    with Session() as session:
        book = Book(
            title=book_data.get("title"),
            author=book_data.get("author"),
            isbn=book_data.get("isbn"),
            no_copies=book_data.get("no_copies"),
            publication_year=book_data.get("publication_year"),
            genre=book_data.get("genre")
        )
        session.add(book)
        session.commit()
        session.refresh(book)
        return book


def borrow_book(book_id):
    with Session() as session:
        borrowed_book = get_book(book_id)
        no_copies = borrowed_book.get_no_copies()
        borrowed_book.set_no_copies(no_copies - 1)
        session.add(borrowed_book)
        session.commit()
        session.refresh(borrowed_book)
        return borrowed_book


def return_book(book_id):
    with Session() as session:
        returned_book = get_book(book_id)
        no_copies = returned_book.get_no_copies()
        returned_book.set_no_copies(no_copies + 1)
        session.add(returned_book)
        session.commit()
        session.refresh(returned_book)
        return returned_book


def remove_book(book_id):
    with Session() as session:
        book = get_book(book_id)
        session.delete(book)
        session.commit()
        return book
