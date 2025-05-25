from collections import deque

book_sales_data = [
    ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 500],
    ["The Hobbit", "J.R.R. Tolkien", 300],
    ["To Kill a Mockingbird", "Harper Lee", 450],
    ["The Catcher in the Rye", "J.D. Salinger", 200],
    ["The Da Vinci Code", "Dan Brown", 350],
]

sales_by_author = {}

for sale_data in book_sales_data:
    sales_by_author[sale_data[1]] = sales_by_author.get(sale_data[1], 0) + sale_data[2]

sorted_sales_by_author = []
for author, sales in sales_by_author.items():
    sorted_sales_by_author.append([author, sales])

sorted_sales_by_author.sort(key=lambda x: x[1], reverse=True)
for author, sales in sorted_sales_by_author:
    print(author + ": " + str(sales))
print()

books_by_authors = {}
for sale_data in book_sales_data:
    books_by_authors[sale_data[1]] = books_by_authors.get(sale_data[1], [])
    books_by_authors[sale_data[1]].append(sale_data[0])

for author, books in books_by_authors.items():
    print(author + ": " + str(books))
print()

books_names = deque()
for sale_data in book_sales_data:
    books_names.append(sale_data[0])

for i in range(0, 3):
    print(books_names.popleft())
print()

books_sales = {}
for book, author, sale in book_sales_data:
    books_sales[book] = books_sales.get(book, 0) + sale

sorted_books_sales = list(books_sales.items())
sorted_books_sales.sort(key=lambda x: x[0])
for book, sale in sorted_books_sales:
    print(book + ": " + str(sale))
print()

total_sales = 0
for sale_data in book_sales_data:
    total_sales += sale_data[2]
print("Total Book Sales: " + str(total_sales))
print("Average Book Sales: " + str(total_sales / len(book_sales_data)))
