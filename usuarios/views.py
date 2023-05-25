from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from usuarios.api.serializers import MyTokenObtainPairSerializer, MyTokenRefreshSerializer

# Create your views here.
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer
