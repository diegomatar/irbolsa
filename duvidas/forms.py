from django import forms
from .models import Duvida

class DuvidaForm(forms.ModelForm):
    class Meta:
        model = Duvida
        fields = ['autor', 'titulo', 'pergunta', 'categorias']