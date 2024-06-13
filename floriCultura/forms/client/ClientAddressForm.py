from typing import Any
from django.forms import ModelForm
from django import forms
from floriCultura.models.Address import Address
from ..form_validators import validate_cep


class ClientAddressForm(ModelForm):

    class Meta:
        model = Address
        fields = ['state', 'city', 'neighborhood', 'street', 'number', 'receiver', 'cep', 'complement']

        widgets = {
            'state': forms.TextInput(attrs={'class': 'input-box'}),
            'city': forms.TextInput(attrs={'class': 'input-box'}),
            'neighborhood': forms.TextInput(attrs={'class': 'input-box'}),
            'street': forms.TextInput(attrs={'class': 'input-box'}),
            'number': forms.TextInput(attrs={'class': 'input-box'}),
            'receiver': forms.TextInput(attrs={'class': 'input-box'}),
            'cep': forms.TextInput(attrs={'class': 'input-box'})
        }

    def clean_cep(self):
        cep = self.cleaned_data.get(cep)

        validate_cep(cep)
        return cep
