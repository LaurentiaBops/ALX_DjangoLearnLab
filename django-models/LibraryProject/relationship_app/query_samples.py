from relationship_app.models import *

"""Get first author in database and filter all books by that author"""
first_author = Author.objects.first()
query_books = Book.objects.filter(author = first_author)

"""List all books in the Library"""
Library_books = Library.objects.get()

"""Retrieve librarian for a library"""
Library_name = Library.ojects.get()
Librarian_name = Librarian.objects.filter(library= Library_name)





