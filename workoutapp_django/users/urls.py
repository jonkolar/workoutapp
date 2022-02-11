from django.urls import path, include
from .views import RegisterUser, LoginUser

urlpatterns = [
    path('user/register/', RegisterUser.as_view()),
]