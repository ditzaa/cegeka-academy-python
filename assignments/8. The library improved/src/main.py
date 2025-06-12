from models.book import Book
from models.borrower import Borrower
from models.library import Library
from models.user import User


def main():
    book1 = Book("1984", "George Orwell", "9780451524935",
                 True, 1949, "Dystopian")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084",
                 True, 1960, "Classic")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565",
                 True, 1925, "Novel")
    book4 = Book("The Great Gatsby 2", "F. Scott Fitzgerald", "9480745273565",
                 True, 1925, "Novel")
    book5 = Book("The Great Gatsby 3", "F. Scott Fitzgerald", "9766643273565",
                 True, 1925, "Novel")

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    library.display_books()
    print()

    isbn2 = book2.get_isbn()
    removed_book = library.remove_book(isbn2)
    print("Removed: " + str(removed_book))
    print()

    searched_book = library.get_book_by_title("1984")
    if searched_book:
        print("Searched: " + str(searched_book))
    else:
        print("Book not found")
    searched_book = library.get_book_by_title("This book is not in library")
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

    print()
    print("User methods")
    user1 = User("Mitu Adrian")
    user1.borrow_book(library, book1)
    user1.borrow_book(library, book2)
    print("Borrowed books:")
    user1.display_borrowed_books()
    print("Library state after 2 borrowed books:")
    library.display_books()
    user1.return_book(library, book1)
    print("Borrowed books:")
    user1.display_borrowed_books()
    print("Library state after 1 return:")
    library.display_books()
    print()

    print("Polymorphism")
    borrower: Borrower = User("Alice")
    borrower.borrow_book(library, book4)
    borrower.display_borrowed_books()
    print()

    print("Iterate through library")
    for book in library:
        print(str(book))


if __name__ == '__main__':
    main()
