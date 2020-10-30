from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=128)
    lessons = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Абонемент'
        verbose_name_plural = 'Абонементы'


class Style(models.Model):
    subscription = models.ForeignKey(Subscription,
                                     on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'


class Hall(models.Model):
    subscription = models.ForeignKey(Subscription,
                                     on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    people_capacity = models.IntegerField(default=0)
    availability_of_inventory = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'


class Trainer(models.Model):
    subscription = models.ForeignKey(Subscription,
                                     on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренера'
# class SubjectCategory(models.Model):
#     name = models.CharField(max_length=128)
#     desc = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Направление подготовки'
#         verbose_name_plural = 'Направления подготовки'
#
#
# class Course(models.Model):
#     category = models.ForeignKey(SubjectCategory,
#                                  on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     desc = models.TextField(blank=True)
#     hours = models.IntegerField(default=0)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Курс'
#         verbose_name_plural = 'Курсы'
