# views.py
from django.shortcuts import render, redirect
from .models import Estudiante, Curso
from .forms import EstudianteForm, CursoForm

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'crear_estudiante.html', {'form': form})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'crear_curso.html', {'form': form})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantes': estudiantes})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'lista_cursos.html', {'cursos': cursos})
