# views.py
from django.shortcuts import render, redirect
from .models import Empleado, Direccion
from .forms import EmpleadoForm, DireccionForm

def crear_empleado(request):
    if request.method == 'POST':
        empleado_form = EmpleadoForm(request.POST)
        direccion_form = DireccionForm(request.POST)
        if empleado_form.is_valid() and direccion_form.is_valid():
            empleado = empleado_form.save()
            direccion = direccion_form.save(commit=False)
            direccion.empleado = empleado
            direccion.save()
            return redirect('')
    else:
        empleado_form = EmpleadoForm()
        direccion_form = DireccionForm()
    
    return render(request, 'crear.html', {
        'empleado_form': empleado_form,
        'direccion_form': direccion_form
    })

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista.html', {'empleados': empleados})
