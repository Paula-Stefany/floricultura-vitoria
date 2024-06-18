from django import forms


class RecoveryForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'Email *', 'id': 'email'}))
