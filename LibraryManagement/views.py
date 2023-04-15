from django.shortcuts import render
from .forms import BookForm, LendOutForm


def books(request):
    return render(request, 'books.html')


def add_book(request):
    context = {
        'form': BookForm()
    }
    return render(request, 'add_book.html', context)

def unreturned(request):
    return render(request, 'unreturned.html')

def lend_book(request, book):
    context = {
        'form': LendOutForm()
    }
    return render(request, 'lend_book.html', context)