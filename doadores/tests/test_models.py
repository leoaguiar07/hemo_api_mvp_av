from rest_framework.test import APITestCase
from rest_framework import status

from doadores.models import Doador


class DoadorAPITestCase(APITestCase):

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
                                                      bairro='Bairro  1',
                                                      numero='111',
                                                      complemento = 'apto 111',
                                                      localidade='Localidade 1',
                                                      uf='RJ',
                                                      telefone='1234567890',
                                                      email='email1@email.com',
                                                      nascimento='1991-11-01',
                                                      peso_aproximado =89,
                                                      tipo_sanguineo="AB",
                                                      fator_rh ="+",
                                                      ultima_doacao='2021-01-11',
                                                      login='login1',
                                                      senha='senha1'
                                                      )
        
    
    def test_fields_required(self):

        """
        The test_fields_required function tests that the required fields are indeed required.
        It does this by sending a POST request to the /api/v2/doadores endpoint with an empty dictionary as data, and then asserts that each of the fields is in fact required.
        
        :param self: Represent the instance of the class
        :return: The following error:
        :doc-author: Trelent
        """
        
        data = {}
        
        url = '/api/v1/doadores/'     
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['nome'][0], "This field is required.")
        self.assertEqual(response.data['cpf'][0], "This field is required.")
        self.assertEqual(response.data['cep'][0], "This field is required.")
        self.assertEqual(response.data['logradouro'][0], "This field is required.")
        self.assertEqual(response.data['bairro'][0], "This field is required.")
        self.assertEqual(response.data['numero'][0], "This field is required.")
        self.assertEqual(response.data['localidade'][0], "This field is required.")
        self.assertEqual(response.data['uf'][0], "This field is required.")
        self.assertEqual(response.data['nascimento'][0], "This field is required.")
        self.assertEqual(response.data['peso_aproximado'][0], "This field is required.")
        self.assertEqual(response.data['login'][0], "This field is required.")
        self.assertEqual(response.data['senha'][0], "This field is required.")

    
    def test_invalid_fields_doador(self):

        """
        The test_invalid_fields_doador function tests the creation of a new Doador object with invalid fields.
            The test_invalid_fields_doador function is expected to return an HTTP 400 BAD REQUEST response, 
            and assert that the email field contains &quot;Enter a valid email address.&quot;, 
            that the tipo_sanguineo field contains &quot;\&quot;AO\&quot; is not a valid choice.&quot; and 
            that the fator_rh field contains &quot;\&quot;=\&quot; is not a valid choice.&quot;. 
        
        :param self: Represent the instance of the class
        :return: The error message &quot;\&quot;ao\&quot; is not a valid choice
        :doc-author: Trelent
        """

        data = { 
                'nome':'Doador 2',
                'genero':'Homem cisgênero',
                'cpf':'123456789AA',
                'cep':'1236547A',
                'logradouro':'Rua 2',
                'bairro':'Bairro 2',
                'numero':'222',
                'complemento':'apto 222',
                'localidade':'Localidade 2',
                'uf':'RJ',
                'telefone':'1234567890',
                'email':'email2emailcom',
                'nascimento':'1992-12-02',
                'peso_aproximado':'5A',
                'tipo_sanguineo':'AO',
                'fator_rh':'=',
                'ultima_doacao':'2022-02-12',
                'login':'login2',
                'senha':'senha2'
                 }
        
        url = '/api/v1/doadores/'     
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['cpf'][0], "A valid integer is required.")
        self.assertEqual(response.data['cep'][0], "A valid integer is required.")
        self.assertEqual(response.data['email'][0], "Enter a valid email address.")
        self.assertEqual(response.data['peso_aproximado'][0], "A valid integer is required.")
        self.assertEqual(response.data['tipo_sanguineo'][0], "\"AO\" is not a valid choice.")
        self.assertEqual(response.data['fator_rh'][0], "\"=\" is not a valid choice.")


    def test_fields_unique(self):

        """
        The test_fields_unique function tests the uniqueness of the fields cpf and login.
            The test_fields_unique function is a unit test that checks if the Doador model 
            has unique fields cpf and login. If it does not, then an error message will be displayed.
        
        :param self: Represent the instance of the object that calls this method
        :return: The error message &quot;doador with this cpf already exists
        :doc-author: Trelent
        """

        data =  { 
                'nome':'Doador 2',
                'genero':'Homem cisgênero',
                'cpf':'12345678901',
                'cep':'12365478',
                'logradouro':'Rua 2',
                'bairro':'Bairro 2',
                'numero':'222',
                'complemento':'apto 222',
                'localidade':'Localidade 2',
                'uf':'RJ',
                'telefone':'1234567890',
                'email':'email2email.com',
                'nascimento':'1992-12-02',
                'peso_aproximado':89,
                'ultima_doacao':'2022-02-12',
                'login':'login1',
                'senha':'senha2'
                 }
        
        url = '/api/v1/doadores/'     
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['cpf'][0], "doador with this cpf already exists.")
        self.assertEqual(response.data['login'][0], "doador with this login already exists.")
        


