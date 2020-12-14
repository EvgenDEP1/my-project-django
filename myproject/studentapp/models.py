from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
