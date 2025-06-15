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
