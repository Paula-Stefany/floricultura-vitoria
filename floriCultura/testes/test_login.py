from django.test import TestCase
from django.test import Client as ClientImaginary
from ..models.Client import Client
from ..models.Address import Address
from ..models.State import State 
from ..models.City import City
from ..models.Neighborhood import Neighborhood
from django.urls import reverse

# Falta ajustar a view de login

class LoginTest(TestCase):

    def setUp(self):
        state = State.objects.create(name='Pernambuco')
        city = City.objects.create(name='Recife')
        neighborhood = Neighborhood.objects.create(name='Madalena')
        address = Address.objects.create(state=state, city=city, neighborhood=neighborhood, street='Rua jujuba', number='76', complement='Perto de pizzaria Valenza', cep='55577788')

        # Criando um usuário dentro do ambiente de teste
        Client.objects.create(username='fofinha', email='Juju@gmail.com', cpf='55566677788',password='JUJU7777*', address=address)

        self.client_imaginary = ClientImaginary()

    def test_valid_login(self):
        url = reverse('login')
        response = self.client_imaginary.post(url, {'email': 'Juju@gmail.com', 'password': 'JUJU7777*'}, **{'Content-Type': 'application/x-www-form-urlencoded'})
        self.assertEqual(response.status_code, 302)

    def test_invalid_login(self):
        url = reverse('login')
        response = self.client_imaginary.post(url, {'email': 'Juju@gmail.com', 'password': 'wrongpassword'}, **{'Content-Type': 'application/x-www-form-urlencoded'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dados de usuário incorretos')
