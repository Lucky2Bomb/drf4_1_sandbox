from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from .models import Post, Article

class PostSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['id', 'user', 'user_id', 'title', 'description', 'image_url']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

from rest_framework.exceptions import ValidationError
# from django.core.files.images import get_image_dimensions

MEGABYTE_LIMIT = 0.5
# REQUIRED_WIDTH = 200
# REQUIRED_HEIGHT = 200

def image_validator(image):
    filesize = image.size
    # width, height = get_image_dimensions(image)

    # if width != REQUIRED_WIDTH or height != REQUIRED_HEIGHT:
    #     raise ValidationError(_(f"You need to upload an image with {REQUIRED_WIDTH}x{REQUIRED_HEIGHT} dimensions"))

    if filesize > MEGABYTE_LIMIT * 1024 * 1024:
        raise ValidationError(_(f"Max file size is {MEGABYTE_LIMIT}MB"))


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    image = serializers.ImageField(required=False, validators=[image_validator])
    # video = serializers.FileField(required=False)
    class Meta:
        model = Article
        fields = "__all__"
