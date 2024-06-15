from django.forms import ModelForm 
from django import forms 
from floriCultura.models.Client import Client
from ..form_validators import validate_cpf


class ClientForm(ModelForm):

    class Meta:
        model = Client 
        fields = ['username', 'email', 'cpf']

        labels = {
            'username': 'Nome',
            'email': 'E-mail',
            'cpf': 'CPF'
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-box'}),
            'email': forms.EmailInput(attrs={'class': 'input-box'}),
            'cpf': forms.TextInput(attrs={'class': 'input-box'})
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        validate_cpf(cpf)

        return cpf
    