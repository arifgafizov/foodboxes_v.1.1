from django.urls import path

from users.views import RegisterUserView, CustomAuthToken, CurrentUserRetrieveUpdateView

urlpatterns = [
    path('auth/login/', CustomAuthToken.as_view(), name='login'),
    path('auth/register/', RegisterUserView.as_view(), name='register'),
    path('current/', CurrentUserRetrieveUpdateView.as_view(), name='current'),
]
