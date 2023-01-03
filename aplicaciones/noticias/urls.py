from django.urls import path
from .views import *

urlpatterns = [
    path('agregar/', agregar, name='agregar_noticia'),
    path('listado/', listado, name='listado_noticias'),
    path('<slug:slug>', noticia, name='noticia'),
    path('categoria/<int:id>', listado_de_categoria, name='listado_de_categoria'),
    
]