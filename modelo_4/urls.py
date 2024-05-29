# urls.py
from django.urls import path
from .views import crear_articulo, crear_comentario, lista_articulos, detalle_articulo

urlpatterns = [
    path('crear_articulo/', crear_articulo, name='crear_articulo'),
    path('articulo/<int:articulo_id>/crear_comentario/', crear_comentario, name='crear_comentario'),
    path('', lista_articulos, name='lista_articulos'),
    path('articulo/<int:articulo_id>/', detalle_articulo, name='detalle_articulo'),
]
