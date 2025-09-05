from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, BookInstance, Author


def index(request):
    text_head = 'У нас большой выбор книг'
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact=3).count()
    author = Author.objects.all()
    num_author = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        "text_head": text_head,
        "books": books,
        "num_books": num_books,
        "num_instance": num_instance,
        "num_instance_available": num_instance_available,
        'author': author,
        'num_author': num_author,
        'num_visits': num_visits,
    }

    return render(request, 'catalog/index.html', context)


class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "catalog/book_list.html"
    paginate_by = 4


class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = 'catalog/book_detail.html'


class AuthorListView(ListView):
    model = Author
    context_object_name = "authors"
    template_name = "catalog/author_list.html"
    paginate_by = 3


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = "author"
    template_name = 'catalog/author_detail.html'