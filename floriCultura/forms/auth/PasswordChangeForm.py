from django import forms 


class PasswordChangeForm(forms.Form):
    password1 = forms.CharField(required=True, label='Criação de Nova Senha', widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Nova Senha *', 'id': 'password1'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme a Senha *'}))

