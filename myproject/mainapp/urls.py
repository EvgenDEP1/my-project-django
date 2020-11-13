import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),

    path('catalog/', mainapp.catalog, name='catalog'),

    path('catalog/publisher/<int:pk>/', mainapp.catalog_page, name='catalog_page'),

    path('catalog/book/<int:pk>/', mainapp.book_page, name='book_page'),
]
