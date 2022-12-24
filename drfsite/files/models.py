from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from common.utils.file import upload_to

# def upload_to(self, filename):
#     return 'images/{filename}'.format(filename=filename)


class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, max_length=256)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(
        upload_to=upload_to, null=True, max_length=256)
    # video = models.FileField(
    #     upload_to=upload_to, null=True, max_length=256, validators=[image_size])

    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
