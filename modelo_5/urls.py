# urls.py
from django.urls import path
from .views import crear_animal, lista_animales, crear_raza, lista_razas, crear_casa, cargar_razas, lista_casas

urlpatterns = [
    path('crear_animal/', crear_animal, name='crear_animal'),
    path('animales/', lista_animales, name='lista_animales'),
    path('crear_raza/', crear_raza, name='crear_raza'),
    path('razas/', lista_razas, name='lista_razas'),
    path('crear_casa/', crear_casa, name='crear_casa'),
    path('cargar_razas/', cargar_razas, name='cargar_razas'),
    path('', lista_casas, name='lista_casas'),
]
