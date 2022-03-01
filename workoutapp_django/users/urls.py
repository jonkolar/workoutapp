from django.urls import path, include
from .views import RegisterUser

urlpatterns = [
    path('user/register/', RegisterUser.as_view()),
]