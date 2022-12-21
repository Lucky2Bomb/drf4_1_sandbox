from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Game(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(get_user_model(), verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
