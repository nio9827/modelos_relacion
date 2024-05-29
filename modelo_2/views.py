# views.py
from django.shortcuts import render, redirect
from .models import Autor, Articulo
from .forms import AutorForm, ArticuloForm

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = AutorForm()
    return render(request, 'crearA.html', {'form': form})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor_id = request.POST['autor_id']
            articulo.save()
            return redirect('lista_autores')
    else:
        form = ArticuloForm()
    autores = Autor.objects.all()
    return render(request, 'crear1.html', {'form': form, 'autores': autores})

def lista_autores(request):
    autores = Autor.objects.all()
    articulos = Articulo.objects.all()
    return render(request, 'listar1.html', {'autores': autores,'articulos': articulos})



