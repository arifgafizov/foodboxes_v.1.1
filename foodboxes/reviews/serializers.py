from rest_framework.serializers import ModelSerializer

from .models import Review
from users.serializers import UserSerializer


class ReviewSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Review
        fields = ['id', 'author', 'status', 'text', 'created_at', 'published_at']
