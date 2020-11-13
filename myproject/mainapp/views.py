from django.shortcuts import render

from mainapp.models import Publisher, Book


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = Publisher.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог',
    }

    return render(request, 'mainapp/catalog.html', context)


def basket(request):
    return render(request, 'mainapp/basket.html')


def catalog_page(request, pk):
    books = Book.objects.filter(publisher_id=pk)
    context = {
        'books': books,
        'page_title': 'страница каталога',
    }

    return render(request, 'mainapp/catalog_page.html', context)


def book_page(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
        'page_title': 'страница книги',
    }

    return render(request, 'mainapp/book_page.html', context)
