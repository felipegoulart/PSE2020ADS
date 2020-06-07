from django.forms import ModelForm
from django import forms
from .models import Arquivos

class ArquivosForm(ModelForm):
    user = forms.IntegerField(widget=forms.HiddenInput()) 

    class Meta:
        model = Arquivos
        fields = '__all__'