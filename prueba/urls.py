from django.urls import path
from prueba.views import sala, indice, cambiar_estado, obtener_estado

urlpatterns = [
    path('sala/', sala, name='sala'),
    path('indice/', indice, name='indice'),
    path('cambiar_estado/', cambiar_estado, name='cambiar_estado'),
    path('obtener_estado/', obtener_estado, name='obtener_estado'),
]
