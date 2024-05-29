# models.py
from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Raza(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='razas')
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.animal.nombre})"

class Casa(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    nombre_animal = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_animal} - {self.raza.nombre} ({self.animal.nombre})"
