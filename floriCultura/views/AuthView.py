from floriCultura.forms.auth.CadasterForm import CadasterForm
from floriCultura.forms.auth.LoginForm import LoginForm
from floriCultura.forms.address.AddressForm import AddressForm
from floriCultura.forms.auth.RecoveryForm import RecoveryForm
from floriCultura.forms.auth.PasswordChangeForm import PasswordChangeForm
from django.shortcuts import render


def cadaster_view(request):

    cadaster_form = CadasterForm()
    address_form = AddressForm()

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        cpf = request.POST['cpf']
        senha = request.POST['senha2']

        cadaster_form = CadasterForm(request.POST)
        if cadaster_form.is_valid():
            print('oi')
            print(f'Username: {username} - Email: {email} - CPF: {cpf} - Senha: {senha}')
        else:
            print('Erro')

    context = {
        'cadaster_form': cadaster_form,
        'address_form': address_form,
    }

    return render(request, template_name='Cadaster.html', context=context, status=200)


def login_view(request):
    
    login_form = LoginForm()
    context = {
        'login_form' : login_form,
    }

    return render(request, template_name='Login.html', context=context, status=200)


def logout_view(request):
    pass


def recovery_view(request):
    
    recovery_form = RecoveryForm()
    context = {
        'recovery_form' : recovery_form,
    }

    return render(request, template_name='Recovery.html', context=context, status=200)


def password_change_view(request):
    
    password_change_form = PasswordChangeForm()
    context = {
        'password_change_form' : password_change_form,
    }

    return render(request, template_name='PasswordChange.html', context=context, status=200)
