from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Rol(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30)

class Usuario(AbstractUser):
    documento = models.CharField(max_length=20)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)