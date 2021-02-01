from rest_framework.serializers import ModelSerializer

from .models import User


class RegisterSerializer(ModelSerializer):
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
