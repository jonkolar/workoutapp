from django.urls import path, include
from .views import RegisterUser

urlpatterns = [
    path('users/create/', RegisterUser.as_view()),
]