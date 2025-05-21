book_sales_data = [
    ["Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 500],
    ["The Hobbit", "J.R.R. Tolkien", 300],
    ["To Kill a Mockingbird", "Harper Lee", 450],
    ["The Catcher in the Rye", "J.D. Salinger", 200],
    ["The Da Vinci Code", "Dan Brown", 350]
]

sales_by_author = {}

for sale_data in book_sales_data:
    sales_by_author[sale_data[1]] = sales_by_author.get(sale_data[1], 0) + sale_data[2]

for author, sales in sales_by_author.items():
    print(author + ": " + str(sales))


