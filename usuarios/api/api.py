from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from usuarios.models import Usuario , Rol 
from usuarios.api.serializers import UsuarioSerializer, RolSerializer, UsuarioSerializerCreate

#----------------------------------------------------------------
# CRUD Usuarios
#----------------------------------------------------------------
@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        usuarios_serializer = UsuarioSerializer(usuarios, many = True)
        return Response(usuarios_serializer.data)
    
    elif request.method == 'POST':
        usuario_serializer = UsuarioSerializerCreate(data = request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.validated_data["password"] = make_password(usuario_serializer.validated_data["password"])
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def user_detail_view(request,pk=None):
    if request.method == 'GET':
        usuario = Usuario.objects.filter(id = pk).first()
        usuario_serializer = UsuarioSerializer(usuario)
        return Response(usuario_serializer.data)
    
    elif request.method == 'PUT':
        usuario = Usuario.objects.filter(id = pk).first()
        usuario_serializer = UsuarioSerializer(usuario,data = request.data)
        if usuario_serializer.is_valid():
            usuario_serializer.validated_data["password"] = make_password(usuario_serializer.validated_data["password"])
            usuario_serializer.save()
            return Response(usuario_serializer.data)
        return Response(usuario_serializer.errors)
    
    elif request.method == 'DELETE':
        usuario = Usuario.objects.filter(id = pk).first()
        usuario.delete()
        return Response('Eliminado')
    
#----------------------------------------------------------------
# CRUD Rol
#----------------------------------------------------------------
@api_view(['GET', 'POST'])
def rol_api_view(request):
    if request.method == 'GET':
        roles = Rol.objects.all()
        roles_serializer = RolSerializer(roles, many = True)
        return Response(roles_serializer.data)
    
    elif request.method == 'POST':
        rol_serializer = RolSerializer(data = request.data)
        if rol_serializer.is_valid():
            rol_serializer.save()
            return Response(rol_serializer.data)
        return Response(rol_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def rol_detail_view(request,pk=None):
    if request.method == 'GET':
        rol = Rol.objects.filter(id = pk).first()
        rol_serializer = RolSerializer(rol)
        return Response(rol_serializer.data)
    
    elif request.method == 'PUT':
        rol = Rol.objects.filter(id = pk).first()
        roles_serializer = RolSerializer(rol,data = request.data)
        if roles_serializer.is_valid():
            roles_serializer.save()
            return Response(roles_serializer.data)
        return Response(roles_serializer.errors)
    
    elif request.method == 'DELETE':
        rol = Rol.objects.filter(id = pk).first()
        rol.delete()
        return Response('Eliminado')