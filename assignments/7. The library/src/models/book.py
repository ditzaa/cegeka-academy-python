from exceptions.invalid_author_error import InvalidAuthorError
from exceptions.invalid_availability_error import InvalidAvailabilityError


class Book:
    _counter = 1

    def __init__(self, title, author, isbn, availability, publication_year, genre):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._availability = availability
        self._publication_year = publication_year
        self._genre = genre
        self.__id = Book._counter
        Book._counter += 1

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_author(self):
        return self._author

    def set_author(self, author):
        if len(author) < 2:
            raise InvalidAuthorError("Name of the author is too short")
        self._author = author

    def get_isbn(self):
        return self._isbn

    def set_isbn(self, isbn):
        self._isbn = isbn

    def get_availability(self):
        return self._availability

    def set_availability(self, availability):
        if not (availability is True or availability is False):
            raise InvalidAvailabilityError("Availability of the book is too truth value")
        self._availability = availability

    def get_publication_year(self):
        return self._publication_year

    def set_publication_year(self, publication_year):
        # if not (availability is True or availability is False):
        #     raise InvalidAvailabilityError("Availability of the book is too truth value")
        self._publication_year = publication_year

    def __str__(self):
        return (f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}"
                f" Availability: {self._availability}, ID: {self.__id}")
