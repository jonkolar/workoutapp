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

class LoginUser(APIView):
    def post(self, request):
        data = loads(request.body)
        username = data['username']
        password = data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            request.session.set_expiry(86400)
            return Response(user.username + " is authenticated")
        else:
            return HttpResponseBadRequest("invalid username or password provided")