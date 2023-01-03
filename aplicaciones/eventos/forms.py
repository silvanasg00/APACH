from django import forms
from . import models

class AgregarEvento(forms.ModelForm):
    class Meta:
        model = models.Evento
        fields = {'nombre', 'ubicacion', 'detalle', 'fecha_evento', 'costo', 'categoria'}
        widgets = {
            'fecha_evento': forms.TextInput(attrs={'type': 'datetime-local'}),
            'detalle': forms.Textarea(attrs={'rows': 3}),
        }

    field_order = ['nombre', 'ubicacion', 'detalle', 'fecha_evento', 'costo', 'categoria']