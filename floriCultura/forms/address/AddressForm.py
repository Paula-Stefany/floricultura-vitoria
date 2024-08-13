from django import forms 
from ..form_validators import validate_cep, validate_city_state
from ...models.State import State
from ...models.City import City


class AddressForm(forms.Form):
    receiver = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Quem receberá a entrega?'}))
    street = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Rua *'}))
    neighborhood = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Bairro *'}))
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="* Cidade", widget=forms.Select(attrs={'class': 'input-box'}))
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=True, label="* Estado", widget=forms.Select(attrs={'class': 'input-box'}))
    number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Nº da casa/Apto *'}))
    complement = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'Complemento'}))
    cep = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-box', 'placeholder': 'CEP *'}))

    def clean_cep(self):
        cep = self.cleaned_data.get('cep')
        
        validate_cep(cep)
        return cep 
    
    def clean_city(self):
        city = self.cleaned_data.get('city')
        state = self.cleaned_data.get('state')

        validate_city_state(city, state)
        return city
