# models.py
from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Direccion(models.Model):
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE, primary_key=True)
    calle = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.calle}, {self.ciudad}, {self.estado}, {self.codigo_postal}"



