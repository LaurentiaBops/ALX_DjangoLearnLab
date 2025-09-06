from django.urls import path
from from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('login/',LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('register/'views.register, name='register'),
    path("",views.index, name="index"),
]