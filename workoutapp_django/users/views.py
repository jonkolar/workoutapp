from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework import permissions

from .managers import CustomUserManager
from .models import CustomUser
from .serializers import RegistrationSerializer

# Create your views here.
class RegisterUser(CreateAPIView):

    model = CustomUser
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = RegistrationSerializer