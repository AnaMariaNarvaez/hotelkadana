from django.db import models

# Create your models here.
class Nacionalidad(models.Model):
    Pais=models.CharField(max_length=40)
    Provincia=models.CharField(max_length=70)
    Codigo=models.IntegerField()
    def  __str__ (self):
        return '{}'.format(self.Pais)