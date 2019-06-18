from django.views import generic
from django.shortcuts import render
from books.models import Book

import datetime


class BookListView(generic.ListView):
    def get_context_data(self, **kwargs):
        pass

def all_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(
        request,
        'books/book_list.html',
        context
    )

def one_book(request, pub_date):
    new_date = pub_date
    try:
        new_date = datetime.datetime.strptime(pub_date, '%b. %d, %Y').date()
    except ValueError:
        pass
    book = Book.objects.get(pub_date=new_date)
    prev_book = book.get_previous_by_pub_date()
    next_book = book.get_next_by_pub_date()
    context = {
        'prev_book': prev_book,
        'book': book,
        'next_book': next_book
    }
    print(context)
    return render(
        request,
        'books/one_book.html',
        context
    )