from django.contrib.auth.models import User
from django.db import models

from mainapp.models import Book


class BookBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
