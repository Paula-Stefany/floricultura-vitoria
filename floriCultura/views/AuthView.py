from floriCultura.forms.auth.CadasterForm import CadasterForm
from floriCultura.forms.auth.LoginForm import LoginForm
from floriCultura.forms.address.AddressForm import AddressForm
from floriCultura.forms.auth.RecoveryForm import RecoveryForm
from floriCultura.forms.auth.PasswordChangeForm import PasswordChangeForm
from django.shortcuts import render, redirect
from floriCultura.models.Client import Client
from floriCultura.models.State import State
from floriCultura.models.City import City
from floriCultura.models.Neighborhood import Neighborhood
from floriCultura.models.Address import Address
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import transaction


def cadaster_view(request):

    cadaster_form = CadasterForm()
    address_form = AddressForm()
    message = None 

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        cpf = request.POST['cpf']
        password = request.POST['password2']
        id_state = request.POST['state']
        id_city = request.POST['city']
        neighborhood = request.POST['neighborhood']
        street = request.POST['street']
        number = request.POST['number']
        receiver = request.POST['receiver']
        cep = request.POST['cep']
        complement = request.POST['complement']
        
        print(username, email, cpf, password)

        cadaster_form = CadasterForm(request.POST)
        address_form = AddressForm(request.POST)


        if cadaster_form.is_valid() and address_form.is_valid():
            verifyEmail = User.objects.filter(email=email).first()

            if verifyEmail is not None:
                message = {'type': 'danger', 'text': 'Já existe um usuário com esse e-mail!'}
                print('Este email já esiste')
            else:
                try:
                    with transaction.atomic():
                        city = City.objects.get(id=id_city)
                        neighborhood_created = Neighborhood.objects.create(name=neighborhood)

                        address_created = Address.objects.create(city=city, neighborhood=neighborhood_created, street=street, number=number, receiver=receiver, cep=cep, complement=complement)

                        user_created = User.objects.create_user(username=username, email=email, password=password)

                        client_created = Client.objects.create(user=user_created, address=address_created, cpf=cpf)
                        
                except Exception as e:
                    print(e)
                    message = {'type': 'danger', 'text': 'Ocorreu um erro durante a criação do usuário'}

                if client_created is not None:
                    user = authenticate(email=email, password=password)
                    print(user)
                    if user:
                        try:
                            login(request, user)
                            return redirect('/')
                        except Exception as e:
                            message = {'type': 'danger', 'text': 'Erro ao logar o usuário'}
                            print(e)
                    else:
                        message = {'type': 'danger', 'text': 'Erro ao autenticar o usuário'}
                else:
                    message = {'type': 'danger', 'text': 'Um erro ocorreu ao tentar criar o usuário.'}
        else:
            message = {'type': 'danger', 'text': 'Dados do formulário inválidos'}

    context = {
        'cadaster_form': cadaster_form,
        'address_form': address_form,
        'message': message 
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
