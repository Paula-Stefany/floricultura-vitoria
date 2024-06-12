from django.forms import ModelForm 
from django import forms 
from floriCultura.models.Client import Client


class ClientForm(ModelForm):

    class Meta:
        model = Client 
        fields = ['username', 'email', 'cpf']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-box'}),
            'email': forms.EmailInput(attrs={'class': 'input-box'}),
            'cpf': forms.TextInput(attrs={'class': 'input-box'})
        }

    
