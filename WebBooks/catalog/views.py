from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Book, BookInstance, Author


def index(request):
    text_head = 'У нас большой выбор книг'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact=3).count()
    author = Author.objects.all()
    num_author = Author.objects.count()
    text_body = 'Содержание'
    context = {
        "text_head": text_head,
        "books": books,
        "num_books": num_books,
        "num_instance": num_instance,
        "num_instance_available": num_instance_available,
        'author': author,
        'num_author': num_author,
    }

    return render(request, 'catalog/index.html', context)


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "catalog/book_list.html"
