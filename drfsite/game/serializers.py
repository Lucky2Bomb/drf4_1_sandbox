from rest_framework import serializers

from .models import Game

class GameSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Game
        fields = "__all__"