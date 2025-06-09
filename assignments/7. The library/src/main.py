from models.book import Book
from models.library import Library


def main():
    book1 = Book("1984", "George Orwell", "9780451524935",
                 True, 1949, "Dystopian")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084",
                 True, 1960, "Classic")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565",
                 False, 1925, "Novel")

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.display_books()
    print()

    isbn2 = book2.get_isbn()
    removed_book = library.remove_book(isbn2)
    print("Removed: " + str(removed_book))
    print()

    searched_book = library.search_book_by_title("1984")
    if searched_book:
        print("Searched: " + str(searched_book))
    else:
        print("Book not found")

    print()
    print("Overloading: ")
    library + book2
    library.display_books()
    print()
    if book1 == book2:
        print("Books are the same")
    else:
        print("Books are not the same")

    copy_book1 = Book("1984", "George Orwell", "9780451524935",
                 True, 1949, "Dystopian")

    if book1 == copy_book1:
        print("Books are the same")
    else:
        print("Books are not the same")


if __name__ == '__main__':
    main()
