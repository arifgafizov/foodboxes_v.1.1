from django.db import IntegrityError
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class CurrentUserRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        return self.request.user


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # handle a unique login
    def create(self, request, *args, **kwargs):
        try:
            return super(CreateAPIView, self).create(request, *args, **kwargs)
        except IntegrityError:
            content = {'error': 'IntegrityError, please enter other username'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
