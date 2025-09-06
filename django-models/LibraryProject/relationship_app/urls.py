from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("",views.index, name="index"),
]