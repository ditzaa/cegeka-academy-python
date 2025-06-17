import json
from json import JSONDecodeError
from src.models.book import Book
from src.config import Config


def load_books_json():
    try:
        with open(Config.JSON_PATH) as json_file:
            books_data = json.load(json_file)
            books = []

            counter = 0

            for element in books_data:
                book = Book(
                    title=element["title"],
                    author=element["author"],
                    isbn=element["isbn"],
                    availability=element["availability"],
                    publication_year=element["publication_year"],
                    genre=element["genre"]
                )
                book.set_id(element["id"])
                books.append(book)
                counter = max(counter, book.id)
                Book.set_counter(counter + 1)

            return books
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        print("JSONDecodeError")
        return []


def save_books_json(books):
    with open(Config.JSON_PATH, 'w') as json_file:
        books = [book.to_json_dict() for book in books]
        books_json = json.dumps(books, indent=4)
        json_file.write(books_json)
