from django.shortcuts import render

from mainapp.models import Subscription, Style, Hall, Trainer


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = Subscription.objects.all()
    context = {
        'categories': categories
    }

    return render(request, 'mainapp/catalog.html', context)


def basket(request):
    return render(request, 'mainapp/basket.html')


def catalog_page(request, pk):
    styles = Style.objects.filter(category_id=pk)
    halls = Hall.objects.filter(category_id=pk)
    trainers = Trainer.objects.filter(category_id=pk)
    context = {
        'styles': styles,
        'halls': halls,
        'trainers': trainers,
    }

    return render(request, 'mainapp/catalog_page.html', context)
