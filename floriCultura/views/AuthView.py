from floriCultura.forms.auth.CadasterForm import CadasterForm
from floriCultura.forms.address.AddressForm import AddressForm
from django.shortcuts import render


def cadaster_view(request):

    cadaster_form = CadasterForm()
    address_form = AddressForm()
    context = {
        'cadaster_form': cadaster_form,
        'address_form': address_form,
    }

    return render(request, template_name='Cadaster.html', context=context, status=200)


def login_view(request):
    pass 


def logout_view(request):
    pass


