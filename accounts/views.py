from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsAuthenticateduser, IsLibarianOrAdmin

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer
    