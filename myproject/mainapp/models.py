from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Book(models.model):
    author = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    publisher = models.Foreignkey(Publisher,
                                  on_delete=models.CASCADE)
    publication_year = models.CharField(max_length=10)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
