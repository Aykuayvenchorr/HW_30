from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=400)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"


class User(AbstractUser):
    ROLES = (
        ('admin', 'Администратор'),
        ('member', 'Пользователь'),
        ('moderator', 'Модератор')
    )

    role = models.CharField(choices=ROLES, default='member', max_length=20)
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'