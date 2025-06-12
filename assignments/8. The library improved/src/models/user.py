from exceptions.borrowing_limit_error import BorrowingLimitError
from exceptions.book_already_borrowed_error import BookAlreadyBorrowedError
from exceptions.book_not_in_library_error import BookNotExistsError
from exceptions.book_not_borrowed_error import BookNotBorrowedError
from models.borrower import Borrower


class User(Borrower):
    _borrowing_limit = 5

    def __init__(self, name):
        self._name = name
        self._borrowed_books = {}
        self._no_borrowed_books = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_borrowed_books(self):
        return self._borrowed_books.copy()

    def get_no_borrowed_books(self):
        return self._no_borrowed_books

    def borrow_book(self, library, book):
        book_from_library = library.get_book_by_title(book.get_title())
        if book_from_library is None:
            raise BookNotExistsError("Book not found in library")
        if book_from_library.get_availability() is False:
            raise BookAlreadyBorrowedError("Book is already borrowed")
        if self._no_borrowed_books == self._borrowing_limit:
            raise BorrowingLimitError("User has reached borrowing limit")

        self._borrowed_books[book.get_isbn()] = book
        library.borrow_book(book)
        self._no_borrowed_books += 1

    def return_book(self, library, book):
        book_from_library = library.get_book_by_title(book.get_title())
        if book_from_library is None:
            raise BookNotExistsError("Book not found in library")
        if book_from_library.get_availability() is True:
            raise BookAlreadyBorrowedError("Book is already available")
        if book.get_isbn() not in self._borrowed_books:
            raise BookNotBorrowedError("Book is not borrowed by this user")

        book_from_library.set_availability(True)
        self._borrowed_books.pop(book.get_isbn())
        self._no_borrowed_books -= 1

    def display_borrowed_books(self):
        for book in self._borrowed_books.values():
            print(str(book))
