from django import forms
from . import models

class AgregarNoticia(forms.ModelForm):
    class Meta:
        model = models.Noticia
        fields = {'titulo', 'subtitulo', 'slug', 'texto', 'imagen', 'categoria'}
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 5}),
        }

    field_order = ['titulo', 'subtitulo', 'slug', 'texto', 'imagen', 'categoria']

class AgregarComentario(forms.ModelForm):
    texto = forms.CharField(label='', required=False)
    class Meta:
        model = models.Comentario
        fields = {'texto'}
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 5}),
        }