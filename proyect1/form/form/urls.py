from django.contrib import admin
from django.urls import path
from prueba.views import formulario_persona_auto
from prueba.views import mostrar_datos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario/', formulario_persona_auto, name='formulario'),
    path('', formulario_persona_auto),
    path('mostrar_datos/', mostrar_datos, name='mostrar_datos'),  # Agregar esta línea para la ruta raíz
]