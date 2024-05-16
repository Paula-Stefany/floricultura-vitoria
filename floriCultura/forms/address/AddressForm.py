from django import forms 


class AddressForm(forms.Form):
    receiver = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Quem receberá a entrega?'}))
    street = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Rua *'}))
    neighborhood = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Bairro *'}))
    city = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Cidade *'}))
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Estado *'}))
    number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Nº da casa/Apto *'}))
    complement = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Complemento'}))
    cep = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'CEP *'}))
