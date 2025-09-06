from bookshelf.models import Book

Book = Book.objects.create(title='1984', author = 'George Orwell', publication_year = '1949')

# Output : No output if it succeeds, model is added to database