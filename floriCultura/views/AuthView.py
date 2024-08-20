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
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags 
import hashlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def cadaster_view(request):

    cadaster_form = CadasterForm()
    address_form = AddressForm()
    link_href = '/login'
    message = None 

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        

        cadaster_form = CadasterForm(request.POST)
        address_form = AddressForm(request.POST)


        if cadaster_form.is_valid() and address_form.is_valid():

            username = cadaster_form.cleaned_data['username']
            email = cadaster_form.cleaned_data['email']
            cpf = cadaster_form.cleaned_data['cpf']
            password = cadaster_form.cleaned_data['password2']
            city = address_form.cleaned_data['city']
            neighborhood_name = address_form.cleaned_data['neighborhood']
            street = address_form.cleaned_data['street']
            number = address_form.cleaned_data['number']
            receiver = address_form.cleaned_data['receiver']
            cep = address_form.cleaned_data['cep']
            complement = address_form.cleaned_data['complement']

            verifyEmail = User.objects.filter(email=email).first()
            if verifyEmail is not None:
                message = {'type': 'danger', 'text': '* Já existe um usuário com esse e-mail!'}
                print('Este email já existe')
            else:
                client_created = None
                try:
                    with transaction.atomic():
                        neighborhood, created = Neighborhood.objects.get_or_create(name=neighborhood_name)

                        address_created = Address.objects.create(city=city, neighborhood=neighborhood, street=street, number=number, receiver=receiver, cep=cep, complement=complement)

                        user_created = User.objects.create_user(username=username, email=email, password=password)

                        client_created = Client.objects.create(user=user_created, address=address_created, cpf=cpf)
                        
                except Exception as e:
                    print(e)
                    message = {'type': 'danger', 'text': '* Ocorreu um erro durante a criação do usuário'}

                if client_created is not None:
                    user = authenticate(email=email, password=password)
                    print(user)
                    if user:
                        try:
                            login(request, user)
                            return redirect('/')
                        except Exception as e:
                            message = {'type': 'danger', 'text': '* Erro ao logar o usuário'}
                            print(e)
                    else:
                        message = {'type': 'danger', 'text': '* Erro ao autenticar o usuário'}
                else:
                    message = {'type': 'danger', 'text': '* Um erro ocorreu ao tentar criar o usuário.'}
        else:
            message = {'type': 'danger', 'text': '* Dados do formulário inválidos'}

    context = {
        'cadaster_form': cadaster_form,
        'address_form': address_form,
        'message': message,
        'link_href': link_href
    }

    return render(request, template_name='Cadaster.html', context=context, status=200)


def login_view(request):
    
    login_form = LoginForm()
    link_href_recovery = '/recovery'
    link_href_cadaster = '/cadaster'
    message = None

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':

        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = authenticate(email=email,
            password = password)
            if user:
                try:
                    login(request, user)
                    return redirect('/')
                except Exception as e:
                    message = {'type': 'danger', 'text': '* Erro ao logar o usuário'}
                    print(e)
            else:
                message = {'type': 'danger', 'text': '* Dados inválidos'}
        
    context = {
        'login_form' : login_form,
        'message' : message,
        'link_href_recovery': link_href_recovery,
        'link_href_cadaster': link_href_cadaster
    }

    return render(request, template_name='Login.html', context=context, status=200)


def logout_view(request):
    pass


def recovery_view(request):
    
    recovery_form = RecoveryForm()
    message = None

    if request.method == 'POST':
        recovery_form = RecoveryForm(request.POST)

        if recovery_form.is_valid():
            email = recovery_form.cleaned_data['email']
            client = Client.objects.filter(user__email=email).first()

            if client is not None:
                try:
                    send_email(client)
                    message = {
                        'type': 'success',
                        'text': 'Um e-mail foi enviado para sua caixa de entrada.'
                    }
                except:
                    message = {'type': 'danger', 'text': 'Erro no envio do email.'}
            else:
                message = {'type': 'danger', 'text': 'E-mail inexistente'}
        else:
            message = {'type': 'danger', 'text': 'Formulário inválido'}

    context = {
        'recovery_form': recovery_form,
        'message': message,
        'title': 'Recuperar senha',
        'button_text': 'Recuperar',
        'link_href': '/login'
    }

    return render(request, template_name='Recovery.html', context=context, status=200)



def password_change_view(request, token):
    
    client = Client.objects.filter(token=token).first()
    change_password_form = PasswordChangeForm()
    message = None 
    link_href = '/login'

    if client is not None:
        if request.method == 'POST':
            change_password_form = PasswordChangeForm(request.POST)
            if change_password_form.is_valid():
                client.user.set_password(request.POST['password2'])
                client.token = None
                client.user.save()
                client.save()
                message = {'type': 'success', 'text': 'Senha alterada com sucesso!!!'}
            else:
                message = {'type': 'danger', 'text': 'Formulário inválido.'}
    else:
        message = {'type': 'danger', 'text': 'Token inválido. Solicite novamente.'}

    context = {
        'change_password_form': change_password_form,
        'message': message,
        'link_href': link_href
    }

    return render(request, template_name='PasswordChange.html', context=context, status=200)


def send_email(client):
    try:

        client.token = hashlib.sha256().hexdigest()
        client.save()

        html_message = render_to_string('EmailRecovery.html', {'token': client.token})
        plain_message = strip_tags(html_message)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'Recuperação de senha'
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = client.user.email

        msg.attach(MIMEText(plain_message, 'plain'))
        msg.attach(MIMEText(html_message, 'html'))

        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(settings.EMAIL_HOST_USER, client.user.email, msg.as_string())
            print('Email enviado com sucesso!')

            server.quit()
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
