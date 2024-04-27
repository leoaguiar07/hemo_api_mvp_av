from django.db.utils import IntegrityError
from rest_framework.test import APITestCase
from rest_framework import status

from doadores.models import Doador


class DoadorAPITestCase(APITestCase):

    def setUp(self):
        
        self.doador_1 = Doador.objects.create(    
                                                      id = 1,
                                                      nome='Doador Teste 1',
                                                      cpf='12345678901',
                                                      cep='12365478',
                                                      logradouro='Rua Teste 1',
                                                      bairro='Bairro Teste 1',
                                                      numero='111',
                                                      complemento = 'apto d:321',
                                                      localidade='Localidade Teste 1',
                                                      uf='TS',
                                                      telefone='1234567890',
                                                      email='teste1@email.com',
                                                      nascimento='1979-06-07',
                                                      ultima_doacao='2011-10-19',
                                                      login='login1',
                                                      senha='senha1'
                                                      )
        
        self.doador_2 = Doador.objects.create(
                                                      id = 2,
                                                      nome='Doador Teste 2',
                                                      cpf='12345678902',
                                                      cep='12365478',
                                                      logradouro='Rua Teste 2',
                                                      bairro='Bairro Teste 2',
                                                      numero='111',
                                                      complemento = 'apto d:322',
                                                      localidade='Localidade Teste 2',
                                                      uf='TS',
                                                      telefone='1234567800',
                                                      email='teste2@email.com',
                                                      nascimento='1979-06-07',
                                                      ultima_doacao='2011-10-19',
                                                      login='login2',
                                                      senha='senha2'
                                                    )

    def test_list_doadores(self):
        
        response = self.client.get('/api/v1/doadores/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    
    def test_detail_doadores(self):
       
        response = self.client.get(f'/api/v1/doadores/{self.doador_1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Doador Teste 1')
        self.assertEqual(response.data['cep'], 12365478)  
        self.assertEqual(response.data['logradouro'], 'Rua Teste 1')


    def test_create_doadores(self):
        
        dados = { 
                       'nome':'Doador Teste 1',
                        'cpf':'11111111111',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'complemento':'apto d:321',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'telefone':'1234567890',
                        'email':'teste1@email.com',
                        'nascimento':'1979-06-07',
                        'ultima_doacao':'2011-10-19',
                        'login':'11111',
                        'senha':'senha1'
                      }
        response = self.client.post('/api/v1/doadores/',dados,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    
    def test_update_doadores(self):
        
        dados_atualizados = {
                      'nome':'Doador Teste 1 ALTERADO',
                        'cpf':'12345678901',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'complemento':'apto d:321',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'telefone':'1234567890',
                        'email':'teste1@email.com',
                        'nascimento':'1979-06-07',
                        'ultima_doacao':'2011-10-19',
                        'login':'login1',
                        'senha':'senha1' 
                      }
        response = self.client.put(f'/api/v1/doadores/{self.doador_1.id}', dados_atualizados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Doador.objects.get(id=self.doador_1.id).nome, 'Doador Teste 1 ALTERADO')


    def test_patch_doador(self):
        
        dados_parciais_atualizados = {'nome': 'Doador Teste 1 ALTERADO'}
        response = self.client.patch(f'/api/v1/doadores/{self.doador_1.id}', dados_parciais_atualizados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Doador.objects.get(id=self.doador_1.id).nome, 'Doador Teste 1 ALTERADO')  


    def test_delete_hemocentro(self):
        
        response = self.client.delete(f'/api/v1/doadores/{self.doador_1.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Doador.objects.count(), 1) 

    
    
    def test_login_unique(self):
             
        dados = { 
                       'nome':'Doador Teste 1',
                        'cpf':'11111111111',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'complemento':'apto d:321',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'telefone':'1234567890',
                        'email':'teste1@email.com',
                        'nascimento':'1979-06-07',
                        'ultima_doacao':'2011-10-19',
                        'login':'login1',
                        'senha':'senha1'
                      }
        response = self.client.post('/api/v1/doadores/',dados,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(IntegrityError)
        

    def test_cpf_unique(self):
             
        dados = { 
                       'nome':'Doador Teste 1',
                        'cpf':'12345678901',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'complemento':'apto d:321',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'telefone':'1234567890',
                        'email':'teste1@email.com',
                        'nascimento':'1979-06-07',
                        'ultima_doacao':'2011-10-19',
                        'login':'11111',
                        'senha':'senha1'
                      }
        response = self.client.post('/api/v1/doadores/',dados,format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(IntegrityError)


    def test_invalid_email_doador(self):

        #'email':'teste1emailcom'
        dado = { 
                       'nome':'Doador Teste 1',
                        'cpf':'12345678901',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'complemento':'apto d:321',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'telefone':'1234567890',
                        'email':'teste1emailcom',
                        'nascimento':'1979-06-07',
                        'ultima_doacao':'2011-10-19',
                        'login':'login1',
                        'senha':'senha1'
                      }
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_invalid_email_doador_2(self):

        #'email':'teste1@emailcom'
        dado = { 
                       'nome':'Doador Teste 1',
                        'cpf':'12345678901',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'complemento':'apto d:321',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'telefone':'1234567890',
                        'email':'teste1@emailcom',
                        'nascimento':'1979-06-07',
                        'ultima_doacao':'2011-10-19',
                        'login':'login1',
                        'senha':'senha1'
                      }
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_invalid_email_doador_3(self):

        #'email':'teste1email.com
        dado = { 
                       'nome':'Doador Teste 1',
                        'cpf':'12345678901',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'complemento':'apto d:321',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'telefone':'1234567890',
                        'email':'teste1email.com',
                        'nascimento':'1979-06-07',
                        'ultima_doacao':'2011-10-19',
                        'login':'login1',
                        'senha':'senha1'
                      }
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
      


    
    def test_create_doador_empty_nome(self):
        
        dado = { 
                        'cpf':'12345678901',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'nascimento':'1979-06-07',
                        'login':'login1',
                        'senha':'senha1'
                      }
        
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    
    def test_create_doador_empty_cpf(self):
        
        dado = { 
                        'nome':'Doador Teste 1',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'nascimento':'1979-06-07',
                        'login':'login1',
                        'senha':'senha1'
                      }
        
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    
    def test_create_doador_empty_cep(self):
        
        dado = { 
                        'nome':'Doador Teste 1',
                        'cpf':'12345678901',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'nascimento':'1979-06-07',
                        'login':'login1',
                        'senha':'senha1'
                      }
        
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    
    def test_create_doador_empty_logradouro(self):
        
        dado = { 
                        'nome':'Doador Teste 1',
                        'cpf':'12345678901',
                        'cep':'12365478',
                        'bairro':'Bairro Teste 1',
                        'numero':'111',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'nascimento':'1979-06-07',
                        'login':'login1',
                        'senha':'senha1'
                      }
        
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    
    def test_create_doador_empty_bairro(self):
        
        dado = { 
                        'nome':'Doador Teste 1',
                        'cpf':'12345678901',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'numero':'111',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'nascimento':'1979-06-07',
                        'login':'login1',
                        'senha':'senha1'
                      }
        
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    
    def test_create_doador_empty_numero(self):
        
        dado = { 
                        'nome':'Doador Teste 1',
                        'cpf':'12345678901',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 1',
                        'bairro':'Bairro Teste 1',
                        'localidade':'Localidade Teste 1',
                        'uf':'TS',
                        'nascimento':'1979-06-07',
                        'login':'login1',
                        'senha':'senha1'
                      }
        
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_doador_empty_localidade(self):
        
        dado = { 
                       'nome':'Doador Teste 2',
                        'cpf':'12345678902',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 2',
                        'bairro':'Bairro Teste 2',
                        'numero':'111',
                        'uf':'TS',
                        'nascimento':'1979-06-07',
                        'login':'login_teste',
                        'senha':'senha2'
                      }
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_doador_empty_uf(self):
        
        dado = { 
                       'nome':'Doador Teste 2',
                        'cpf':'12345678902',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 2',
                        'bairro':'Bairro Teste 2',
                        'numero':'111',
                        'localidade':'Localidade Teste 2',
                        'nascimento':'1979-06-07',
                        'login':'login_teste',
                        'senha':'senha2'
                      }
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_doador_empty_nascimento(self):
        
        dado = { 
                       'nome':'Doador Teste 2',
                        'cpf':'12345678902',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 2',
                        'bairro':'Bairro Teste 2',
                        'numero':'111',
                        'localidade':'Localidade Teste 2',
                        'uf':'TS',
                        'login':'login_teste',
                        'senha':'senha2'
                      }
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_doador_empty_login(self):
        
        dado = { 
                       'nome':'Doador Teste 2',
                        'cpf':'12345678902',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 2',
                        'bairro':'Bairro Teste 2',
                        'numero':'111',
                        'localidade':'Localidade Teste 2',
                        'uf':'TS',
                        'nascimento':'1979-06-07',
                        'senha':'senha2'
                      }
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_doador_empty_senha(self):
        
        dado = { 
                       'nome':'Doador Teste 2',
                        'cpf':'12345678902',
                        'cep':'12365478',
                        'logradouro':'Rua Teste 2',
                        'bairro':'Bairro Teste 2',
                        'numero':'111',
                        'localidade':'Localidade Teste 2',
                        'uf':'TS',
                        'nascimento':'1979-06-07',
                        'login':'login_teste'
                      }
        response = self.client.post('/api/v1/doadores/', dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
















    