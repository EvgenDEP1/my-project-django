from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from basketapp.models import BookBasket
from django.urls import reverse

from mainapp.models import Book


def index(request):
    items = BookBasket.objects.filter(user=request.user)
    context = {
        'object_list': items
    }

    return render(request, 'basketapp/basket.html', context)


def add(request, book_id):
    book = Book.objects.get(pk=book_id)
    BookBasket.objects.get_or_create(
        user=request.user,
        book=book
    )

    return HttpResponseRedirect(reverse('mainapp:catalog_page',
                                        kwargs={'pk': book.publisher_id}))


def remove(request, book_basket_id):
    if request.is_ajax():
        item = BookBasket.objects.get(id=book_basket_id)
        item.delete()
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return JsonResponse({'status': 'ok',
                             'book_basket_id': book_basket_id})
