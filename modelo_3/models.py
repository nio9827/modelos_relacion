# models.py
from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    estudiantes = models.ManyToManyField(Estudiante, related_name='cursos')

    def __str__(self):
        return self.nombre
