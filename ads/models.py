from django.db import models

from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=400)
    author = models.ForeignKey(User, verbose_name='Автор', related_name='ads', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=1000, null=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Selection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name







