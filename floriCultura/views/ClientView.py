from django.shortcuts import render
from floriCultura.forms.client.ClientAddressForm import ClientAddressForm
from floriCultura.forms.client.ClientForm import ClientForm


def client_profile_view(request, id=None):
  pass


def edit_client_view(request):
    pass


def edit_client_address_view(request):
    address_form = ClientAddressForm()

    context = {
     'address_form': address_form,
    }

    return render(request, template_name='Address.html', context=context, status=200)

