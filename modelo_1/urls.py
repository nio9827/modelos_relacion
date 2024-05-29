# urls.py
from django.urls import path
from .views import crear_empleado, lista_empleados

urlpatterns = [
    path('crear/', crear_empleado, name='crear_empleado'),
    path('', lista_empleados, name='lista_empleados'),
]
