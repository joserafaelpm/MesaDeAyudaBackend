from rest_framework.response import Response
from rest_framework.decorators import api_view
from solicitudes.models import Estado, Rol_Estado, Solicitud
from solicitudes.api.serializers import (
    EstadoSerializer, 
    Rol_EstadoSerializer, 
    SolicitudSerializerList,
    SolicitudSerializerCreate,
    SolicitudSerializerBase
)

#----------------------------------------------------------------
# CRUD Estado
#----------------------------------------------------------------
@api_view(['GET', 'POST'])
def Estado_api_view(request):
    if request.method == 'GET':
        estados = Estado.objects.all()
        estados_serializer = EstadoSerializer(estados, many = True)
        return Response(estados_serializer.data)
    
    elif request.method == 'POST':
        estado_serializer = EstadoSerializer(data = request.data)
        if estado_serializer.is_valid():
            estado_serializer.save()
            return Response(estado_serializer.data)
        return Response(estado_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Estado_detail_view(request,pk=None):
    if request.method == 'GET':
        estado = Estado.objects.filter(id = pk).first()
        estado_serializer = EstadoSerializer(estado)
        return Response(estado_serializer.data)
    
    elif request.method == 'PUT':
        estado = Estado.objects.filter(id = pk).first()
        estado_serializer = EstadoSerializer(estado,data = request.data)
        if estado_serializer.is_valid():
            estado_serializer.save()
            return Response(estado_serializer.data)
        return Response(estado_serializer.errors)
    
    elif request.method == 'DELETE':
        estado = Estado.objects.filter(id = pk).first()
        estado.delete()
        return Response('Eliminado')
    
#----------------------------------------------------------------
# CRUD Rol_Estado
#----------------------------------------------------------------
@api_view(['GET', 'POST'])
def Rol_estado_api_view(request):
    if request.method == 'GET':
        roles_Estados = Rol_Estado.objects.all()
        roles_Estados_serializer = Rol_EstadoSerializer(roles_Estados, many = True)
        return Response(roles_Estados_serializer.data)
    
    elif request.method == 'POST':
        estado_serializer = Rol_EstadoSerializer(data = request.data)
        if estado_serializer.is_valid():
            estado_serializer.save()
            return Response(estado_serializer.data)
        return Response(estado_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Rol_estado_detail_view(request,pk=None):
    if request.method == 'GET':
        rol_Estado = Rol_Estado.objects.filter(id = pk).first()
        estado_serializer = Rol_EstadoSerializer(rol_Estado)
        return Response(estado_serializer.data)
    
    elif request.method == 'PUT':
        rol_Estado = Rol_Estado.objects.filter(id = pk).first()
        estado_serializer = Rol_EstadoSerializer(rol_Estado,data = request.data)
        if estado_serializer.is_valid():
            estado_serializer.save()
            return Response(estado_serializer.data)
        return Response(estado_serializer.errors)
    
    elif request.method == 'DELETE':
        rol_Estado = Rol_Estado.objects.filter(id = pk).first()
        rol_Estado.delete()
        return Response('Eliminado')

#----------------------------------------------------------------
# CRUD Solicitud
#----------------------------------------------------------------
@api_view(['GET', 'POST'])
def Solicitud_api_view(request):
    if request.method == 'GET':
        solicitudes = Solicitud.objects.all()
        solicitudes_serializer = SolicitudSerializerList(solicitudes, many = True)
        return Response(solicitudes_serializer.data)
    
    elif request.method == 'POST':
        solicitud_serializer = SolicitudSerializerCreate(data = request.data)
        if solicitud_serializer.is_valid():
            instance = solicitud_serializer.save()
            return Response(SolicitudSerializerList(instance).data)
        return Response(solicitud_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def Solicitud_detail_view(request,pk=None):
    if request.method == 'GET':
        solicitud = Solicitud.objects.filter(id = pk).first()
        solicitudes_serializer = SolicitudSerializerBase(solicitud)
        return Response(solicitudes_serializer.data)
    
    elif request.method == 'PUT':
        solicitud = Solicitud.objects.filter(id = pk).first()
        solicitudes_serializer = SolicitudSerializerBase(solicitud,data = request.data)
        if solicitudes_serializer.is_valid():
            solicitudes_serializer.save()
            return Response(solicitudes_serializer.data)
        return Response(solicitudes_serializer.errors)
    
    elif request.method == 'DELETE':
        solicitud = Solicitud.objects.filter(id = pk).first()
        solicitud.delete()
        return Response('Eliminado')