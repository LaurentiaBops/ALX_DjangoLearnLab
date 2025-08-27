from bookshelf.models import Book

book = Book.objects.filter.(author="Geaorge Orwell")
book = book.delete

book = Book.objects.all()

# Output: (1, {'Bookshelf.book': 1})

