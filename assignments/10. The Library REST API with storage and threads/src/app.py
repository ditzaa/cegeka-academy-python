from src.models.book import Book
from src.models.user_book import user_book
from src.models.user import User
from flask import Flask
from src.config import Config
from src.controllers.api_controller import api_blueprint
from src.controllers.book_controller import book_blueprint
from src.controllers.user_controller import user_blueprint
from src.controllers.loan_controller import loan_blueprint
from src.db import BaseClass, engine, Session


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(api_blueprint)
    app.register_blueprint(book_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(loan_blueprint)

    BaseClass.metadata.create_all(bind=engine)
    seed_db()

    return app


def seed_db():
    print("Seeding DB")
    with Session() as session:
        if session.query(Book).count() == 0:
            demo_books = [
                Book(title="1984", author="George Orwell", isbn="9780451524935", no_copies=3, publication_year=1949, genre="Dystopian"),
                Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="9780061120084", no_copies=2, publication_year=1960, genre="Fiction"),
                Book(title="The Great Gatsby", author="F. Scott Fitzgerald", isbn="9780743273565", no_copies=4, publication_year=1925, genre="Classic"),
                Book(title="Brave New World", author="Aldous Huxley", isbn="9780060850524", no_copies=1, publication_year=1932, genre="Science Fiction"),
                Book(title="The Catcher in the Rye", author="J.D. Salinger", isbn="9780316769488", no_copies=5, publication_year=1951, genre="Fiction"),
                Book(title="Fahrenheit 451", author="Ray Bradbury", isbn="9781451673319", no_copies=2, publication_year=1953, genre="Dystopian"),
                Book(title="Moby Dick", author="Herman Melville", isbn="9781503280786", no_copies=3, publication_year=1851, genre="Adventure"),
                Book(title="Pride and Prejudice", author="Jane Austen", isbn="9780141439518", no_copies=4, publication_year=1813, genre="Romance"),
                Book(title="The Hobbit", author="J.R.R. Tolkien", isbn="9780547928227", no_copies=3, publication_year=1937, genre="Fantasy"),
                Book(title="Crime and Punishment", author="Fyodor Dostoevsky", isbn="9780140449136", no_copies=2, publication_year=1866, genre="Philosophical Fiction"),
            ]
            session.bulk_save_objects(demo_books)

            existing_users = session.query(User).count()
            if existing_users == 0:
                demo_users = [
                    User(name="Andrei Popescu", email="andrei.popescu@example.com", role="admin"),
                    User(name="Maria Ionescu", email="maria.ionescu@example.com", role="admin"),
                    User(name="Ioana Georgescu", email="ioana.georgescu@example.com", role="subscriber"),
                    User(name="Vlad Stan", email="vlad.stan@example.com", role="subscriber"),
                    User(name="Elena Dobre", email="elena.dobre@example.com", role="subscriber"),
                    User(name="Cristian Marin", email="cristian.marin@example.com", role="subscriber"),
                    User(name="Ana Radu", email="ana.radu@example.com", role="subscriber"),
                    User(name="Roxana Mihai", email="roxana.mihai@example.com", role="subscriber"),
                    User(name="George Ilie", email="george.ilie@example.com", role="subscriber"),
                    User(name="Laura Enache", email="laura.enache@example.com", role="subscriber"),
                ]

            session.bulk_save_objects(demo_users)
            session.commit()
