from src.db import Session
from src.models.book import Book
from src.models.user import User
from src.models.user_book import user_book
from src.services.books_service import get_book


def loan_book(book_id, user_id):
    with Session() as session:
        loaned_book = get_book(book_id)
        user = session.query(User).get(user_id)

        if not user or not loaned_book:
            return None

        borrowed_books = [book for book in user.borrowed_books]
        for borrowed_book in borrowed_books:
            if borrowed_book.id == book_id:
                return 0

        no_loaned_books = loaned_book.get_no_loaned_books()
        loaned_book.set_no_loaned_books(no_loaned_books + 1)
        user.borrowed_books.append(loaned_book)
        user.set_no_borrowed_books(user.get_no_borrowed_books() + 1)

        session.add(loaned_book)
        session.add(user)
        session.commit()
        session.refresh(loaned_book)

        return loaned_book


def return_book(book_id, user_id):
    with Session() as session:
        user = session.query(User).get(user_id)
        book = session.query(Book).get(book_id)

        if not user or not book:
            return None

        if book not in user.borrowed_books:
            return 0

        user.borrowed_books.remove(book)
        user.set_no_borrowed_books(user.get_no_borrowed_books() - 1)
        book.set_no_loaned_books(book.get_no_loaned_books() - 1)

        session.add(user)
        session.add(book)
        session.commit()

        return book


def log_borrowing_state(user_id=None):
    with Session() as session:

        result = session.execute(user_book.select()).fetchall()
        print("\nTabela 'user_book' (user_id <-> book_id):")
        for row in result:
            print(f"User ID: {row.user_id} <-> Book ID: {row.book_id}")

        print("========================\n")
