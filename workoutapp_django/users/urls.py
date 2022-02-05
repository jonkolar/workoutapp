from django.urls import path, include
from .views import RegisterUser, LoginUser

urlpatterns = [
    path('users/register/', RegisterUser.as_view()),
    path('users/login/', LoginUser.as_view())
]