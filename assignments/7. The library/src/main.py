from models.book import Book


def main():
    book1 = Book("1984", "George Orwell", "9780451524935",
                 True, 1949, "Dystopian")
    print(str(book1))
    book1.set_author("J.K. Rowling")
    print(str(book1))


if __name__ == '__main__':
    main()
