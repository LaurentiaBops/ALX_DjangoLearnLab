from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# Create your views here.
class library_booklist(DetailView):
    """Lists books stored in a specific library"""
    model = Library
    template_name = 'relationship_app/library_detail.html'



def book_list(request):
    """Lists all books stored in the database"""
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request, 'relationship_app/list_books.html', context)
