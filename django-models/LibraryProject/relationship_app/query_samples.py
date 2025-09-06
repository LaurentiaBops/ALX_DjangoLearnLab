from relationship_app.models import *

"""Get first author in database and filter all books by that author"""
author = Author.objects.get(name=author_name)
query_books = Book.objects.filter(author = author)

"""List all books in the Library"""
Library_books = Library.objects.get(name=library_name)
books.all()

"""Retrieve librarian for a library"""
library = Library.ojects.get(name=library_name)
Librarian_name = Librarian.objects.filter(library= library)





