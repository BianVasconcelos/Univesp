from django import forms
from .models import Pizza

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = (
            'nome',
            'valor_p',
            'valor_m',
            'valor_g',
            'descricao',
            'imagem'
        )
        widgets = {
            'imagem': forms.ClearableFileInput(attrs={'multiple': True})
        }           
        