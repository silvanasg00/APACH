from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Evento,CategoriaEvento
from . import forms

@login_required(login_url='ingresar')
def agregar(request):
    if request.method == 'POST':
        form = forms.AgregarEvento(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user
            evento.save()
            return redirect('inicio')
    else:
        form = forms.AgregarEvento()
    return render(request, 'eventos/agregar.html', {'form':form})

def listado(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/listado.html', {'eventos':eventos})

@login_required(login_url='ingresar')
def listado_de_categoria_e(request, id):
    categoria = CategoriaEvento.objects.get(id = id)
    eventos = Evento.objects.filter(categoria = categoria)
    return render(request, 'eventos/listado.html', {'eventos':eventos, 'categoria':categoria})

