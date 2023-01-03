from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class CategoriaNoticia(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Categoria de Noticias"
        verbose_name_plural = "Categorias de Noticias"

    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    texto = models.TextField()
    imagen = models.ImageField(null=True, blank=True, upload_to='noticia')
    categoria = models.ForeignKey(CategoriaNoticia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    texto = models.CharField(max_length=255)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return self.texto