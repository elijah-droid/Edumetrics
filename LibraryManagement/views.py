from django.shortcuts import render

def books(request):
    return render(request, 'books.html')


def add_book(request):
    return render(request, 'add_book.html')