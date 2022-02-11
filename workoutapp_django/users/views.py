from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseBadRequest

from .serializers import RegistrationSerializer
from django.contrib.auth import get_user_model

from json import loads

User = get_user_model()

# Create your views here.
class RegisterUser(CreateAPIView):

    queryset = User
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = RegistrationSerializer