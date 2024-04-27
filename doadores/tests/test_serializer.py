from datetime import datetime
from rest_framework.test import APITestCase

from doadores.models import Doador
from doadores.serializers import DoadorSerializer


class DoadorSerializerTestCase(APITestCase):

    def setUp(self):
                
        """
        The setUp function is called before each test function.
        It creates a new Doador object and saves it to the database.
               
        :param self: Represent the instance of the class
        :return: A doador object
        :doc-author: Trelent
        """

        self.doador_1 = Doador.objects.create(    
                                                      id = 1,
                                                      nome='Doador 1',
                                                      genero='Homem cisgênero',
                                                      cpf=12345678901,
                                                      cep=12365478,
                                                      logradouro='Rua 1',
                                                      bairro='Bairro 1',
                                                      numero='111',
                                                      complemento = 'apto 111',
                                                      localidade='Localidade 1',
                                                      uf='RJ',
                                                      telefone='1234567890',
                                                      email='email1@email.com',
                                                      nascimento='1991-11-01',
                                                      peso_aproximado= 89,
                                                      tipo_sanguineo='AB',
                                                      fator_rh ='+',
                                                      ultima_doacao='2021-01-11',
                                                      login='login1',
                                                      senha='senha1'
                                                      )
        

    def test_serializer_data(self):
         
        """
        The test_serializer_data function tests the serializer data.
            It asserts that the serializer data is equal to a dictionary containing all of the doador_2's attributes.
        
        :param self: Represent the instance of the class
        :return: The serializer data of the doador_2 object
        :doc-author: Trelent
        """
        
        serializer = DoadorSerializer(self.doador_1)
        
        serializer_data = {
            'id': self.doador_1.id,
            'nome': 'Doador 1',
            'genero':'Homem cisgênero',
            'cpf': 12345678901,
            'cep': 12365478,
            'logradouro': 'Rua 1',
            'bairro': 'Bairro 1',
            'numero': '111',
            'complemento': 'apto 111',
            'localidade': 'Localidade 1',
            'uf': 'RJ',
            'telefone':'1234567890',
            'email': 'email1@email.com',
            'nascimento':'1991-11-01',
            'peso_aproximado':89,
            'tipo_sanguineo': 'AB',
            'fator_rh':'+',
            'ultima_doacao':'2021-01-11',
            'login': 'login1',
            'senha': 'senha1',
            'created_at': datetime.strftime(self.doador_1.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            }
        self.assertEqual(serializer.data, serializer_data)