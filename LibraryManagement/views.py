from django.shortcuts import render, redirect
from .forms import BookForm, LendOutForm
from .models import Book, LendOut


def books(request):
    return render(request, 'books.html')


def add_book(request):
    context = {
        'form': BookForm()
    }
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.School = request.user.schooladministrator.current_school
            book.save()
            request.user.schooladministrator.current_school.Books.add(book)
            return redirect('books')
    else:
        return render(request, 'add_book.html', context)

def unreturned(request):
    unreturned = LendOut.objects.filter(Book__School=request.user.schooladministrator.current_school, Returned=False)
    context = {
        'unreturned': unreturned
    }
    return render(request, 'unreturned.html', context)


def returned(request, lendout):
    lendout = LendOut.objects.get(id=lendout)
    lendout.Returned = True
    lendout.save()
    lendout.Book.Number += 1
    lendout.Book.save()
    lendout.Book.Lend_Outs.remove(lendout)
    return redirect('books')

def lend_book(request, book):
    book = Book.objects.get(id=book)
    context = {
        'form': LendOutForm()
    }
    if request.method  == 'POST':
        form = LendOutForm(request.POST)
        if form.is_valid():
            lendout = form.save(commit=False)
            lendout.Book = book
            lendout.save()
            book.Number -= lendout.Number
            book.save()
            book.Lend_Outs.add(lendout)
            return redirect('books')
    else:
        return render(request, 'lend_book.html', context)