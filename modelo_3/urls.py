# urls.py
from django.urls import path
from .views import crear_estudiante, crear_curso, lista_estudiantes, lista_cursos

urlpatterns = [
    path('crear_estudiante/', crear_estudiante, name='crear_estudiante'),
    path('crear_curso/', crear_curso, name='crear_curso'),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('cursos/', lista_cursos, name='lista_cursos'),
]
