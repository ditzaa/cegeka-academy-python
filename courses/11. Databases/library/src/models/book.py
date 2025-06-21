from sqlalchemy.orm import relationship
from src.models.user_book import user_book
from src.db import BaseClass
from sqlalchemy import Column, Integer, String


class Book(BaseClass):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String(500), nullable=False, default='NA')
    author = Column(String(500), nullable=False, default="NA")
    isbn = Column(String(500), nullable=False, default="NA")
    no_copies = Column(Integer, nullable=False, default=0)
    publication_year = Column(Integer, nullable=False, default="NA")
    genre = Column(String(500), nullable=True, default="NA")

    borrowers = relationship("User", secondary=user_book, back_populates="borrowed_books")

    def __init__(self, title="NA", author="NA", isbn="NA", no_copies=0, publication_year="NA", genre="NA"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.no_copies = no_copies
        self.publication_year = publication_year
        self.genre = genre

    def get_id(self):
        return self.id

    def set_id(self, book_id):
        self.id = book_id

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_no_copies(self):
        return self.no_copies

    def set_no_copies(self, no_copies):
        self.no_copies = no_copies

    def get_publication_year(self):
        return self.publication_year

    def set_publication_year(self, publication_year):
        self.publication_year = publication_year

    def __str__(self):
        return (f"ID: {self.id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn},"
                f"Nb. of copies: {self.no_copies}, Publication Year: {self.publication_year}, Genre: {self.genre}")

    def to_json_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "no_copies": self.no_copies,
            "publication_year": self.publication_year,
            "genre": self.genre,
        }
