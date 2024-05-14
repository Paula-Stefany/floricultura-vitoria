from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Nome *'}))
    email = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'input--box', 'placeholder': 'Email *'}))
    cpf = forms.CharField(max_length=8, required=True, widget=forms.TextInput(attrs={
    'class': 'input-box', 'placeholder': 'CPF *'}))
    senha1 = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Senha *'}))
    senha2 = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Confirme a Senha *'}))
