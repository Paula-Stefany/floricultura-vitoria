from django import forms


class RecoveryForm(forms.Form):
    email = forms.EmailField(required=True, label='Email para Recuperação de Senha', widget=forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'Email *', 'id': 'email'}))
