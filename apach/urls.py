from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', include('aplicaciones.noticias.urls')),
    path('registrar/',registrar,name="registrar"),
    path('ingresar/',ingresar,name="ingresar"),
    path('inicio',inicio,name='inicio'),
    path('cerrar_sesion',cerrar_sesion,name="cerrar_sesion"),
    path('contacto',contacto,name='contacto'),
    path('fundacion',fundacion,name="fundacion"),
    path('eventos/', include('aplicaciones.eventos.urls')),
    path('', inicio, name='inicio')
]















if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)