from django import forms
from .models import Persona, Auto

class PersonaAutoForm(forms.ModelForm):
    telefono = forms.CharField(max_length=255)
    direccion = forms.CharField(max_length=255)
    marca = forms.CharField(max_length=255)
    modelo = forms.CharField(max_length=255)
    placa = forms.CharField(max_length=255)
    vencimiento_placa = forms.DateField()
    año_carro = forms.IntegerField()

    class Meta:
        model = Persona
        fields = ['nombre', 'edad', 'telefono', 'direccion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['marca'].widget.attrs.update({'placeholder': 'Ingrese la marca del carro'})
        self.fields['modelo'].widget.attrs.update({'placeholder': 'Ingrese el modelo del carro'})
        self.fields['placa'].widget.attrs.update({'placeholder': 'Ingrese la placa del carro'})
        self.fields['vencimiento_placa'].widget.attrs.update({'placeholder': 'Ingrese la fecha de vencimiento de la placa'})
        self.fields['año_carro'].widget.attrs.update({'placeholder': 'Ingrese el año del carro'})