from rest_framework import serializers
from solicitudes.models import Estado, Rol_Estado, Solicitud
from actividades.api.serializers import ActividadSerializerList
from usuarios.api.serializers import UsuarioSerializer

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class Rol_EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol_Estado
        fields = '__all__'

class SolicitudSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'

class SolicitudSerializerCreate(SolicitudSerializerBase):
    class Meta:
        model = Solicitud
        exclude = ['id']

class SolicitudSerializerList(SolicitudSerializerBase):
    actividad = serializers.SerializerMethodField(method_name='getActividad')
    estado = serializers.SerializerMethodField(method_name='getEstado')
    usuario_solicitante = serializers.SerializerMethodField(method_name='getUsuarioSolicitante')
    usuario_tecnico = serializers.SerializerMethodField(method_name='getUsuarioTecnico')

    def getActividad(self, solicitud: Solicitud):
        return ActividadSerializerList(solicitud.actividad).data
    
    def getEstado(self, solicitud: Solicitud):
        return EstadoSerializer(solicitud.estado).data
    
    def getUsuarioSolicitante(self, solicitud: Solicitud):
        return UsuarioSerializer(solicitud.usuario_solicitante).data
    
    def getUsuarioTecnico(self, solicitud: Solicitud):
        return UsuarioSerializer(solicitud.usuario_tecnico).data

    class Meta:
        model = Solicitud
        fields = '__all__'