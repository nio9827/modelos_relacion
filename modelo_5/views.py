# views.py
from django.shortcuts import render, redirect
from .models import Animal, Raza, Casa
from .forms import CasaForm,AnimalForm,RazaForm

def crear_casa(request):
    if request.method == 'POST':
        form = CasaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_casas')
    else:
        form = CasaForm()
    return render(request, 'crear_casa.html', {'form': form})

def cargar_razas(request):
    animal_id = request.GET.get('animal_id')
    razas = Raza.objects.filter(animal_id=animal_id).order_by('nombre')
    return render(request, 'razas_dropdown_list_options.html', {'razas': razas})

def lista_casas(request):
    casas = Casa.objects.all()
    return render(request, 'lista_casas.html', {'casas': casas})


def crear_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_animales')
    else:
        form = AnimalForm()
    return render(request, 'crear_animal.html', {'form': form})

def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'lista_animales.html', {'animales': animales})


def crear_raza(request):
    if request.method == 'POST':
        form = RazaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_razas')
    else:
        form = RazaForm()
    return render(request, 'crear_raza.html', {'form': form})

def lista_razas(request):
    razas = Raza.objects.all()
    return render(request, 'lista_razas.html', {'razas': razas})