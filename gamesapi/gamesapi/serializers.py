from rest_framework import serializers

from django.contrib.auth.models import User
from games.models import Game

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# Serializers define the API representation.
class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'genre',
            'platform',
            'score',
            'editors_choice',
            'created',
            'modified'
        )
        model = Game
