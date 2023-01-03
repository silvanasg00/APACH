
from django.db import models
from django.contrib.auth.models import User

class CategoriaEvento(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Categoria de Eventos"
        verbose_name_plural = "Categorias de Eventos"

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    detalle = models.CharField(max_length=200, default=' ')
    fecha_evento = models.DateTimeField(auto_now=False, auto_now_add=False)
    costo = models.DecimalField(max_digits=12, decimal_places=2)
    categoria = models.ForeignKey(CategoriaEvento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre
