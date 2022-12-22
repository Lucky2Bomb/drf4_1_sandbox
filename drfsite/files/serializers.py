from rest_framework import serializers
from django.contrib.auth.models import User
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


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    image_url = serializers.ImageField(required=False)
    class Meta:
        model = Article
        fields = "__all__"
