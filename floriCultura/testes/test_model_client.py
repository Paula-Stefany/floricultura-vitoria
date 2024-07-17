from floriCultura.models.Client import Client
from django.test import TestCase
from ..models.Address import Address
from ..models.State import State 
from ..models.City import City
from ..models.Neighborhood import Neighborhood


class ClientModelTest(TestCase):
    def setUp(self):

        state = State.objects.create(name='Pernambuco')
        city = City.objects.create(name='Recife')
        neighborhood = Neighborhood.objects.create(name='Madalena')
        address = Address.objects.create(state=state, city=city, neighborhood=neighborhood, street='Rua jujuba', number='76', complement='Perto de pizzaria Valenza', cep='55577788')

        # Criando um usuário dentro do ambiente de teste
        Client.objects.create(username='fofinha', email='Juju@gmail.com', cpf='55566677788',password='JUJU7777*', address=address)

    def test_client_exist(self):
        # procurando um usuário dentro da base de dados criada para o teste
        client = Client.objects.first()
        self.assertIsNotNone(client)
        self.assertEqual(client.username, 'fofinha')
        self.assertEqual(client.email, 'Juju@gmail.com')
