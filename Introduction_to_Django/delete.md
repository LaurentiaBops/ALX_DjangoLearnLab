from bookshelf.models import Book

books = Book.objects.filter.(author="Geaorge Orwell")
books = books.delete

books = Book.objects.all()

# Output: (1, {'Bookshelf.book': 1})

