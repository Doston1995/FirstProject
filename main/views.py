from django.views.generic import ListView
from .models import Book, User


class BookListView(ListView):
    model = Book
    template_name = 'index.html'
