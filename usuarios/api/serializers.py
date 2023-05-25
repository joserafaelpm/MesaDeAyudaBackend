from rest_framework import serializers
from usuarios.models import Usuario, Rol

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    rol = serializers.SerializerMethodField(method_name='getRol')

    def getRol(self, usuario: Usuario):
        return RolSerializer(usuario.rol).data

    class Meta:
        model = Usuario
        fields = '__all__'

class UsuarioSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ['id']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Si se quiere agregar algo al token
        # ...
        token['user'] = UsuarioSerializer(user).data

        return token

class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(MyTokenRefreshSerializer, self).validate(attrs)
        
        # En caso de que se requiera personalizar el token de refresh
        #decoded_payload = token_backend.decode(data['access'], verify=True)
        #user_uid=decoded_payload['user_id']

        return data