from django.db import models
from usuarios import models as usuarios
from actividades import models as actividades

# Create your models here.

class Estado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)

class Rol_Estado(models.Model):
    rol = models.ForeignKey(usuarios.Rol, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=250)
    fecha_inicio = models.DateTimeField(null=True)
    fecha_entrega = models.DateTimeField(null=True)
    fecha_cierre = models.DateTimeField(null=True)
    observacion = models.CharField(max_length=250, null=True)
    actividad = models.ForeignKey(actividades.Actividad, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    usuario_solicitante = models.ForeignKey(usuarios.Usuario, on_delete=models.CASCADE, related_name='solicitudes_solicitante')
    usuario_tecnico = models.ForeignKey(usuarios.Usuario, on_delete=models.CASCADE, null=True, related_name='solicitudes_tecnico')


