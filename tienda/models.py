from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=500)

