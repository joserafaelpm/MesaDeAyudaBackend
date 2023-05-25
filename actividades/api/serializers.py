from rest_framework import serializers
from actividades.models import Actividad, Categoria, Usuario_Actividad

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class Usuario_ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Actividad
        fields = '__all__'

class ActividadSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = [
            'id', 
            'descripcion', 
            'categoria', 
        ]

class ActividadSerializerCreate(ActividadSerializerBase):
    class Meta:
        model = Actividad
        exclude = ['id']

class ActividadSerializerList(ActividadSerializerBase):
    categoria = serializers.SerializerMethodField(method_name='getCategory')

    def getCategory(self, actividad: Actividad):
        return CategoriaSerializer(actividad.categoria).data

    class Meta:
        model = Actividad
        fields = '__all__'