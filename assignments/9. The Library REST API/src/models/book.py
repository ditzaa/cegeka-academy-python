class Book:
    _counter = 1

    def __init__(self, title="NA", author="NA", isbn="NA", availability=False, publication_year="NA", genre="NA"):
        self.id = Book._counter
        Book._counter += 1
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability
        self.publication_year = publication_year
        self.genre = genre

    def get_id(self):
        return self.id

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

    def get_availability(self):
        return self.availability

    def set_availability(self, availability):
        self.availability = availability

    def get_publication_year(self):
        return self.publication_year

    def set_publication_year(self, publication_year):
        self.publication_year = publication_year

    def __str__(self):
        return (f"ID: {self.id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
                f" Availability: {self.availability}, Publication Year: {self.publication_year}, Genre: {self.genre}")

    def to_json_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "availability": self.availability,
            "publication_year": self.publication_year,
            "genre": self.genre,
        }
