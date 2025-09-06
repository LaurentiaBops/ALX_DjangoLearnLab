"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('books/',views.list_books, name='books'),
    path('Library/',views.LibraryDetailView.as_view(), name='Library'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/',
    #         TemplateView.as_view(template_name='accounts/profile.html'),
    #         name= 'profile'),
    # path("signup/",SignUpView.as_view(), name="templates/relationship_app/signup"),
    # path('login/', LoginView.as_view(template_name='registration/login.html'),name='login'),
    # path('logout/',LogoutView.as_view(), name='logout'),
]
