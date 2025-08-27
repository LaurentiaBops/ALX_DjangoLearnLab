>>> from bookshelf.models import Book
>>> books = Book.objects.all()
>>> newbook = Book(title = '1984', author = 'George Orwell', publication
949)
>>> newbook.save()

>>> books = Book.objects.all()
>>> for book in books:
...     print(book.title, book.author, book.publication_year)
...
1984 George Orwell 1949

>>> books.update(title = "Nineteen Eighty-Four")
1
>>>for book in books:
...     print(book.title)

>>> books = Book.objects.filter(author = "George Orwell")
>>> books.delete()
(1, {'bookshelf.Book': 1})

>>> books = Book.objects.all()
>>> for book in books:
...     print:(book.title, book.author)
...
>>>

