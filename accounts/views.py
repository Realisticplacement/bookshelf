from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny


# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer


class RefreshView(TokenRefreshView):
    permission_classes = [AllowAny]
    serializers_class = UserRegisterSerializer



    