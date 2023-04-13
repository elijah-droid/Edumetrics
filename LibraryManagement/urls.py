from django.urls import path
from .views import books, add_book


urlpatterns = [
    path('books/', books, name="books"),
    path('add-book/', add_book, name="add-book")
]