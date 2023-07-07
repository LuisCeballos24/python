from django.contrib import admin
from django.urls import path
from prueba.views import formulario_persona_auto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario/', formulario_persona_auto, name='formulario'),
    path('', formulario_persona_auto),  # Agregar esta línea para la ruta raíz
]