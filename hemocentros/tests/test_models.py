from rest_framework.test import APITestCase
from rest_framework import status

from hemocentros.models import Hemocentro


class HemocentroAPITestCase(APITestCase):

    def setUp(self):
        self.hemocentro_1 = Hemocentro.objects.create(id = 1,
                                                      nome='Hemo 1',
                                                      cep=12365478,
                                                      logradouro='Rua 1',
                                                      bairro='Bairro 1',
                                                      numero='111',
                                                      complemento='Loja B',
                                                      localidade='Localidade 1',
                                                      uf='RJ',
                                                      telefone='1234567890',
                                                      email='teste1@email.com',
                                                      estoque_atual=80.36,
                                                      estoque_ideal=227.0
                                                      )
        
    
    def test_fields_required(self):
        
        data = {}
        
        url = '/api/v1/hemocentros/'     
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['nome'][0], "This field is required.")
        self.assertEqual(response.data['cep'][0], "This field is required.")
        self.assertEqual(response.data['logradouro'][0], "This field is required.")
        self.assertEqual(response.data['bairro'][0], "This field is required.")
        self.assertEqual(response.data['localidade'][0], "This field is required.")
        self.assertEqual(response.data['uf'][0], "This field is required.")
        self.assertEqual(response.data['estoque_atual'][0], "This field is required.")
        self.assertEqual(response.data['estoque_ideal'][0], "This field is required.")
        
    
    def test_invalid_fields_doador(self):

        data = {
                'nome':'Hemo 2',
                'cep':'12365478AA',
                'logradouro':'Rua 2',
                'bairro':'Bairro 2',
                'numero':'222',
                'complemento':'Loja C',
                'localidade':'Localidade 2',
                'uf':'SP',
                'telefone':'1234567890',
                'email':'teste1emailcom',
                'estoque_atual':80.36,
                'estoque_ideal':227.0,

                }
        
        url = '/api/v1/hemocentros/'     
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['cep'][0], "A valid integer is required.")
        self.assertEqual(response.data['email'][0], "Enter a valid email address.")
        

    def test_fields_unique(self):

        data =  { 
                'nome':'Hemo 1',
                'cep':12365478,
                'logradouro':'Rua 2',
                'bairro':'Bairro 2',
                'numero':'222',
                'complemento':'Loja C',
                'localidade':'Localidade 2',
                'uf':'SP',
                'telefone':'1234567890',
                'email':'teste1@email.com'
                 }
        
        url = '/api/v1/hemocentros/'     
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['nome'][0], "hemocentro with this nome already exists.")
        
        


