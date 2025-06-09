from models.book import Book
from exceptions.book_already_exists_error import BookAlreadyExistsError
from exceptions.book_not_in_library_error import BookNotExistsError


class Library:

    def __init__(self):
        self._books = {}

    def get_books(self):
        return self._books.copy()

    def add_book(self, book):
        if book.get_isbn() in self._books:
            raise BookAlreadyExistsError("Book already exists in library")
        else:
            self._books[book.get_isbn()] = book

    def display_books(self):
        for book in self._books.values():
            print(str(book))

    def remove_book(self, isbn):
        if isbn not in self._books:
            raise BookNotExistsError("Book with given ISBN does not exists")
        removed_book = self._books.pop(isbn)

        return removed_book

    def get_book_by_title(self, title):
        for book in self._books.values():
            if book.get_title() == title:
                return book

    def borrow_book(self, book):
        if book.get_isbn() not in self._books:
            raise BookNotExistsError("Book with given ISBN does not exists")
        book_from_library = self._books[book.get_isbn()]
        book_from_library.set_availability(False)

    def __add__(self, book):
        if isinstance(book, Book):
            self.add_book(book)
        return self
