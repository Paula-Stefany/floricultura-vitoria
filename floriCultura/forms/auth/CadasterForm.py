from typing import Any
from django import forms
from django.core.exceptions import ValidationError


class CadasterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Nome *'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'Email *'}))
    cpf = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
    'class': 'input-box', 'placeholder': 'CPF *'}))
    password1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Senha *'}))
    password2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme a Senha *'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('senha1')
        password2 = self.cleaned_data.get('senha2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('As senhas não coicidem')
        return password2
