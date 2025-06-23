from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db import BaseClass
from src.models.user_book import user_book


class User(BaseClass):
    __tablename__ = "users"
    BORROWING_LIMIT = 5

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    no_borrowed_books = Column(Integer, unique=False, nullable=False)
    role = Column(String(100), unique=False, nullable=False)

    borrowed_books = relationship("Book", secondary=user_book, back_populates="borrowers")

    def __init__(self, name="NA", email="NA", role="NA"):
        self.name = name
        self.email = email
        self.no_borrowed_books = 0
        self.role = role

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_no_borrowed_books(self):
        return self.no_borrowed_books

    def set_no_borrowed_books(self, no_borrowed_books):
        self.no_borrowed_books = no_borrowed_books

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    @classmethod
    def get_borrowing_limit(cls):
        return cls.BORROWING_LIMIT

    def __str__(self):
        return (f"ID: {self.id}, name: {self.name}, Email: {self.email},"
                f" Nb. of borrowed books: {self.no_borrowed_books}, Role: {self.role}")

    def to_json_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "no_borrowed_books": self.no_borrowed_books,
            "role": self.role,
        }
