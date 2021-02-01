from rest_framework.serializers import ModelSerializer

from .models import User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'phone_number',
            'address',
        ]
        read_only_fields = ['id', 'username']
        extra_kwargs = {
            'phone_number': {'required': False},
            'middle_name': {'required': False},
        }
