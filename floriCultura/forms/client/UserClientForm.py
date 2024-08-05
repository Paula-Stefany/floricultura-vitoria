from django.forms import ModelForm 
from django import forms 
from floriCultura.models.Client import Client
from ..form_validators import validate_cpf
from django.contrib.auth.models import User


class ClientForm(ModelForm):

    class Meta:
        model = Client 
        fields = [ 'cpf']

        labels = {
            'cpf': 'CPF'
        }

        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'input-box'})
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        validate_cpf(cpf)

        return cpf
    

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-box'}),
            'email': forms.EmailInput(attrs={'class': 'input-box'})
        }
