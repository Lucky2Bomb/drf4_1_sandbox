from django.db import models
from django.contrib.auth.models import User

def upload_to(self, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, max_length=256)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    