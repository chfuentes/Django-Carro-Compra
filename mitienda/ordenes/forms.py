from django import forms
from .models import Orden


class FormCrearOrden(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['nombres', 'apellidos', 'email', 'direccion', 'ciudad']
