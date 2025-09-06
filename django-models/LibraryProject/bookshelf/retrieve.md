from bookshelf.models import Book

books = Book.objects.get(publication_year = 1949)

for book in books:
    print(book.title, book.author, book.publication_year)

# Output: 1984 George Orwell 1949