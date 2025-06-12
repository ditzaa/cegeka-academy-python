from abc import ABC, abstractmethod


class Borrower(ABC):
    @abstractmethod
    def borrow_book(self, library, book):
        pass

    @abstractmethod
    def display_borrowed_books(self):
        pass
