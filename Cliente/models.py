from django.db import models
from Nacionalidad.models import Nacionalidad

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    sexo=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=70)
    edad=models.IntegerField()
    telefono=models.CharField(max_length=30)
    email=models.EmailField()
    domicilio=models.TextField()
    nacionalidad=models.ForeignKey(Nacionalidad, null=True, blank=True, on_delete=models.CASCADE)
