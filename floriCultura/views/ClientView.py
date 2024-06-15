from django.shortcuts import render
from floriCultura.forms.client.ClientAddressForm import ClientAddressForm
from floriCultura.forms.client.ClientForm import ClientForm


def client_profile_view(request, id=None):
  pass


def edit_client_view(request):
    client_form = ClientForm()

    context = {
       'client_form': client_form,
    }

    return render(request, template_name='EditClient.html', context=context, status=200)


def edit_client_address_view(request):
    address_form = ClientAddressForm()

    context = {
     'address_form': address_form,
    }

    return render(request, template_name='EditAddress.html', context=context, status=200)
