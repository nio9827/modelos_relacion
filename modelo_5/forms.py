# forms.py
from django import forms
from .models import Animal, Raza, Casa

class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        fields = ['animal', 'raza', 'nombre_animal']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['raza'].queryset = Raza.objects.none()

        if 'animal' in self.data:
            try:
                animal_id = int(self.data.get('animal'))
                self.fields['raza'].queryset = Raza.objects.filter(animal_id=animal_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['raza'].queryset = self.instance.animal.razas.order_by('nombre')


# forms.py
from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre']


# forms.py
from django import forms
from .models import Animal, Raza

class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = ['animal', 'nombre']
