from django.db import models
from usuarios import models as usuarios
# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    usuario = models.ForeignKey(usuarios.Usuario, on_delete=models.CASCADE)

class Actividad(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=45)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Usuario_Actividad(models.Model):
    usuario = models.ForeignKey(usuarios.Usuario, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)