from django import forms
from .models import Persona, Auto

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'edad', 'telefono', 'direccion']

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'modelo', 'placa', 'vencimiento_placa', 'año_carro']