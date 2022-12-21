from rest_framework import serializers
from .models import MyModel

class PostSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = MyModel
        fields = ['id', 'user', 'user_id', 'title', 'description', 'image_url']
