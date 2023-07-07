from django.shortcuts import render, redirect
from .forms import PersonaForm, AutoForm
from .models import Persona, Auto

def mostrar_datos(request):
    personas = Persona.objects.all()
    autos = Auto.objects.all()
    datos_combinados = zip(personas, autos)
    return render(request, 'mostrar_datos.html', {'datos_combinados': datos_combinados})

def formulario_persona_auto(request):
    if request.method == 'POST':
        persona_form = PersonaForm(request.POST)
        auto_form = AutoForm(request.POST)
        if persona_form.is_valid() and auto_form.is_valid():
            persona = persona_form.save()
            auto = auto_form.save(commit=False)
            auto.persona = persona
            auto.save()
            return redirect('mostrar_datos')
    else:
        persona_form = PersonaForm()
        auto_form = AutoForm()

    return render(request, 'formulario.html', {'persona_form': persona_form, 'auto_form': auto_form})