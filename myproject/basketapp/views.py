from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import BookBasket
from django.urls import reverse

from mainapp.models import Book

def index(request):
    return render(request, 'basketapp/basket.html')


def add(request, book_id):
    book = Book.objects.get(pk=book_id)
    BookBasket.objects.get_or_create(
        user=request.user,
        book=book
    )

    return HttpResponseRedirect(reverse('mainapp:catalog_page',
                                        kwargs={'pk': book.publisher_id}))
