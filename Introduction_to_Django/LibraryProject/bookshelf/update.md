from bookshelf.models import Book

books = Book.object.all()
books.update(title = "Nineteen Eighty-Four")


# Output: Nineteen Eighty-Four
