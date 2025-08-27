from bookshelf.models import Book

books = Book.objects.get(title="1984")
books.title = "Nineteen Eighty-Four"


# Output: Nineteen Eighty-Four
