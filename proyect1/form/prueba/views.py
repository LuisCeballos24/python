from django.shortcuts import render
from .forms import PersonaAutoForm

def formulario_persona_auto(request):
    if request.method == 'POST':
        form = PersonaAutoForm(request.POST)
        if form.is_valid():
            form.save()
            # Realizar cualquier otra acción necesaria
    else:
        form = PersonaAutoForm()

    return render(request, 'formulario.html', {'form': form})