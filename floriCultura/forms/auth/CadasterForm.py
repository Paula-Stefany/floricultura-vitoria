from django import forms


class CadasterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Nome *'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailFieldInput(attrs={'class': 'input-box', 'placeholder': 'Email *'}))
    cpf = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={
    'class': 'input-box', 'placeholder': 'CPF *'}))
    senha1 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Senha *'}))
    senha2 = forms.CharField(max_length=20, required=True, widget=forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Confirme a Senha *'}))
