from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.

class register(CreateView):
    """User registration"""
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'



class LibraryDetailView(DetailView):
    """Lists books stored in a specific library"""
    model = Library
    template_name = 'relationship_app/library_detail.html'



def list_books(request):
    """Lists all books stored in the database"""
    books = Book.objects.all()
    context = {'book_list':books}
    return render(request, 'relationship_app/list_books.html', context)
