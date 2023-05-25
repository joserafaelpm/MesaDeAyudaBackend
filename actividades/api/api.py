from rest_framework.response import Response
from rest_framework.decorators import api_view
from actividades.models import Actividad, Categoria , Usuario_Actividad
from actividades.api.serializers import (
    ActividadSerializerList, 
    ActividadSerializerCreate,
    CategoriaSerializer, 
    Usuario_ActividadSerializer)

#----------------------------------------------------------------
# CRUD Actividad
#----------------------------------------------------------------
@api_view(['GET', 'POST'])
def actividad_api_view(request):
    if request.method == 'GET':
        actividades = Actividad.objects.all()
        actividades_serializer = ActividadSerializerList(actividades, many = True)
        return Response(actividades_serializer.data)
    
    elif request.method == 'POST':
        actividad_serializer = ActividadSerializerCreate(data = request.data)
        if actividad_serializer.is_valid():
            instance = actividad_serializer.save()
            return Response(ActividadSerializerList(instance).data)
        return Response(actividad_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def actividad_detail_view(request,pk=None):
    if request.method == 'GET':
        actividad = Actividad.objects.filter(id = pk).first()
        actividad_serializer = ActividadSerializerList(actividad)
        return Response(actividad_serializer.data)
    
    elif request.method == 'PUT':
        actividad = Actividad.objects.filter(id = pk).first()
        actividad_serializer = ActividadSerializerCreate(actividad,data = request.data)
        if actividad_serializer.is_valid():
            actividad_serializer.save()
            return Response(actividad_serializer.data)
        return Response(actividad_serializer.errors)
    
    elif request.method == 'DELETE':
        actividad = Actividad.objects.filter(id = pk).first()
        actividad.delete()
        return Response('Eliminado')
    
#----------------------------------------------------------------
# CRUD Categoria
#----------------------------------------------------------------
@api_view(['GET', 'POST'])
def Categoria_api_view(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        categorias_serializer = CategoriaSerializer(categorias, many = True)
        return Response(categorias_serializer.data)
    
    elif request.method == 'POST':
        categoria_serializer = CategoriaSerializer(data = request.data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response(categoria_serializer.data)
        return Response(categoria_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Categoria_detail_view(request,pk=None):
    if request.method == 'GET':
        categoria = Categoria.objects.filter(id = pk).first()
        categoria_serializer = CategoriaSerializer(categoria)
        return Response(categoria_serializer.data)
    
    elif request.method == 'PUT':
        categoria = Categoria.objects.filter(id = pk).first()
        categoria_serializer = CategoriaSerializer(categoria,data = request.data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response(categoria_serializer.data)
        return Response(categoria_serializer.errors)
    
    elif request.method == 'DELETE':
        categoria = Categoria.objects.filter(id = pk).first()
        categoria.delete()
        return Response('Eliminado')

#----------------------------------------------------------------
# CRUD Usuario_Actividad
#----------------------------------------------------------------
@api_view(['GET', 'POST'])
def Usuario_Actividad_api_view(request):
    if request.method == 'GET':
        usuarios_Actividades = Usuario_Actividad.objects.all()
        usuarios_Actividades_serializer = Usuario_ActividadSerializer(usuarios_Actividades, many = True)
        return Response(usuarios_Actividades_serializer.data)
    
    elif request.method == 'POST':
        usuario_Actividad_serializer = Usuario_ActividadSerializer(data = request.data)
        if usuario_Actividad_serializer.is_valid():
            usuario_Actividad_serializer.save()
            return Response(usuario_Actividad_serializer.data)
        return Response(usuario_Actividad_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Usuario_Actividad_detail_view(request,pk=None):
    if request.method == 'GET':
        usuario_Actividad = Usuario_Actividad.objects.filter(id = pk).first()
        usuario_Actividad_serializer = Usuario_ActividadSerializer(usuario_Actividad)
        return Response(usuario_Actividad_serializer.data)
    
    elif request.method == 'PUT':
        usuario_Actividad = Usuario_Actividad.objects.filter(id = pk).first()
        usuario_Actividad_serializer = Usuario_ActividadSerializer(usuario_Actividad,data = request.data)
        if usuario_Actividad_serializer.is_valid():
            usuario_Actividad_serializer.save()
            return Response(usuario_Actividad_serializer.data)
        return Response(usuario_Actividad_serializer.errors)
    
    elif request.method == 'DELETE':
        usuario_Actividad = Usuario_Actividad.objects.filter(id = pk).first()
        usuario_Actividad.delete()
        return Response('Eliminado')