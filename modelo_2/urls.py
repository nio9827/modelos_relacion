# urls.py
from django.urls import path
from .views import crear_autor, crear_articulo, lista_autores

urlpatterns = [
    path('crearA', crear_autor, name='crear_autor'),
    path('crear1', crear_articulo, name='crear_articulo'),
    path('listar1', lista_autores, name='lista_autores'),
]
