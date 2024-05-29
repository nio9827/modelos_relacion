# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo, Comentario
from .forms import ArticuloForm, ComentarioForm

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'crear_articulo.html', {'form': form})

def crear_comentario(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.save()
            return redirect('detalle_articulo', articulo_id=articulo.id)
    else:
        form = ComentarioForm()
    return render(request, 'crear_comentario.html', {'form': form, 'articulo': articulo})

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'lista_articulos.html', {'articulos': articulos})

def detalle_articulo(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    comentarios = articulo.comentarios.all()
    return render(request, 'detalle_articulo.html', {'articulo': articulo, 'comentarios': comentarios})
