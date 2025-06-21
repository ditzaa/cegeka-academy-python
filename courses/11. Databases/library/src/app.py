from src.models.book import Book
from src.models.user_book import user_book
from src.models.user import User
from flask import Flask
from src.config import Config
from src.controllers.api_controller import api_blueprint
from src.controllers.book_controller import book_blueprint
from src.db import BaseClass, engine, Session


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(api_blueprint)
    app.register_blueprint(book_blueprint)

    BaseClass.metadata.create_all(bind=engine)
    seed_db()

    return app


def seed_db():
    print("Seeding DB")
    with Session() as session:
        if session.query(Book).count() == 0:
            demo_books = [
                Book(title="1984", author="George Orwell", isbn="9780451524935", no_copies=3, publication_year=1949,
                     genre="Dystopian"),
                Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="9780061120084", no_copies=2,
                     publication_year=1960, genre="Fiction"),
                Book(title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="9780743273565", no_copies=4,
                     publication_year=1925, genre="Classic"),
                Book(title="Brave New World", author="Aldous Huxley", isbn="9780060850524", no_copies=1,
                     publication_year=1932, genre="Science Fiction"),
                Book(title="The Catcher in the Rye", author="J.D. Salinger", isbn="9780316769488", no_copies=5,
                     publication_year=1951, genre="Fiction"),
            ]

            session.bulk_save_objects(demo_books)
            session.commit()
