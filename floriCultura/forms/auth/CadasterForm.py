from typing import Any
from django import forms
from django.core.exceptions import ValidationError


class CadasterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Nome *'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'Email *'}))
    cpf = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
    'class': 'input-box', 'placeholder': 'CPF *'}))
    senha1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Senha *'}))
    senha2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme a Senha *'}))

    def clean(self):
        cleaned_data = super().clean()
        senha1 = self.cleaned_data.get('senha1')
        senha2 = self.cleaned_data.get('senha2')

        if senha1 and senha2 and senha1 != senha2:
            raise ValidationError('As senhas estão diferentes')
        return cleaned_data
