from django.urls import path

from users.views import RegisterUser, CustomAuthToken, CurrentUserRetrieveUpdateView

urlpatterns = [
    path('auth/login/', CustomAuthToken.as_view(), name='login'),
    path('auth/register/', RegisterUser.as_view(), name='register'),
    path('auth/current/', CurrentUserRetrieveUpdateView.as_view(), name='current'),

]
