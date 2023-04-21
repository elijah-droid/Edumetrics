from django.urls import path
from .views import books, add_book, unreturned, lend_book, returned


urlpatterns = [
    path('books/', books, name="books"),
    path('add-book/', add_book, name="add-book"),
    path('unreturned/', unreturned, name='unreturned'),
    path('lend-book/<int:book>/', lend_book, name='lend-book'),
    path('returned/<int:lendout>/', returned, name='returned')
]