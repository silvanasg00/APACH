from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from . import forms

@login_required(login_url='ingresar')
def agregar(request):
    if request.method == 'POST':
        form = forms.AgregarNoticia(request.POST,request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.usuario = request.user
            noticia.save()
            return redirect('inicio')
    else:
        form = forms.AgregarNoticia()
    return render(request, 'noticias/agregar.html', {'form':form})

def listado(request):
    categorias = CategoriaNoticia.objects.all()
    noticias = Noticia.objects.all()
    return render(request, 'noticias/listado.html', {'noticias':noticias, 'categorias':categorias})

@login_required(login_url='ingresar')
def noticia(request, slug):
    noticia = Noticia.objects.get(slug = slug)
    comentarios = Comentario.objects.filter(noticia = noticia)
    if request.method == 'POST':
        form = forms.AgregarComentario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.noticia = noticia
            comentario.save()
            return redirect('noticia', slug)
    else:
        form = forms.AgregarComentario()
    return render(request, 'noticias/noticia.html', {'noticia':noticia, 'comentarios':comentarios, 'form':form})

@login_required(login_url='ingresar')
def listado_de_categoria(request, id):
    categoria = CategoriaNoticia.objects.get(id = id)
    noticias = Noticia.objects.filter(categoria = categoria)
    return render(request, 'noticias/listado.html', {'noticias':noticias, 'categoria':categoria})