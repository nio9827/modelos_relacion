# forms.py
from django import forms
from .models import Empleado, Direccion

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'email']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'ciudad', 'estado', 'codigo_postal']
