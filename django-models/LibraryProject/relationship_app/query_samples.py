from relationship_app.models import *

"""Query all books by a specific author"""
author = Author.objects.get(name=author_name)
objects.filter(author=author)

"""List all books in the Library"""
Library_books = Library.objects.get(name=library_name)
books.all()

"""Retrieve librarian for a library"""
library = Library.ojects.get(name=library_name)
objects.filter(library= library)





