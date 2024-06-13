from django import forms
from ..form_validators import validate_password_equal, validate_password_strength, validate_cpf


class CadasterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Nome *'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'Email *'}))
    cpf = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
    'class': 'input-box', 'placeholder': 'CPF *'}))
    password1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Senha *'}))
    password2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme a Senha *'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        validate_password_equal(password1, password2)
        validate_password_strength(password1)

        return password2
    
    def clean_cpf(self):
        cpf  = self.cleaned_data.get('cpf')

        validate_cpf(cpf)
        return cpf
