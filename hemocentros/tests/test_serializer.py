from datetime import datetime
from rest_framework.test import APITestCase
from hemocentros.models import Hemocentro
from hemocentros.serializers import HemocentroSerializer


class HemocentroSerializerTestCase(APITestCase):

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
        

    def test_serializer_data(self):
        
        serializer = HemocentroSerializer(self.hemocentro_1)
        
        serializer_data = {
                'id': self.hemocentro_1.id,
                'nome':'Hemo 1',
                'cep':12365478,
                'logradouro':'Rua 1',
                'bairro':'Bairro 1',
                'numero':'111',
                'complemento':'Loja B',
                'localidade':'Localidade 1',
                'uf':'RJ',
                'telefone':'1234567890',
                'email':'teste1@email.com',
                'estoque_atual':80.36,
                'estoque_ideal':227.0,
                'created_at': datetime.strftime(self.hemocentro_1.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            }
        self.assertEqual(serializer.data, serializer_data)