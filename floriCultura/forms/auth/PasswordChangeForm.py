from django import forms 
from django.core.exceptions import ValidationError


class PasswordChangeForm(forms.Form):

    password1 = forms.CharField(required=True, label='Criação de Nova Senha', widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Nova Senha *', 'id': 'password1'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme a Senha *'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError('As senhas não coincidem')
        return password2
    