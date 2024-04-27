from rest_framework.test import APITestCase
from rest_framework import status

from hemocentros.models import Hemocentro


class HemocentroAPITestCase(APITestCase):

    def setUp(self):
        """
        The setUp function is called before each test function.
        It creates a Hemocentro object for use in the tests.
        
        :param self: Represent the instance of the class
        :return: A tuple of the created objects
        :doc-author: Trelent
        """
        self.hemocentro_1 = Hemocentro.objects.create(id = 1,
                                                      nome='Hemo Teste 1',
                                                      cep='12365478',
                                                      logradouro='Rua Teste 1',
                                                      bairro='Bairro Teste 1',
                                                      numero='111',
                                                      localidade='Localidade Teste 1',
                                                      uf='TS',
                                                      telefone='1234567890',
                                                      email='teste1@email.com'
                                                      )
        
        self.hemocentro_2 = Hemocentro.objects.create(id=2,
                                                      nome='Hemo Teste 2',
                                                      cep='87654321',
                                                      logradouro='Rua Teste 2',
                                                      bairro='Bairro Teste 2',
                                                      numero='222',
                                                      localidade='Localidade Teste 2',
                                                      uf='TS',
                                                      telefone='0987654321',
                                                      email='teste2@email.com')

    
    
    def test_list_hemocentro(self):
        """
        The test_list_hemocentro function tests the list_hemocentro view.
        It does so by making a GET request to /api/v2/hemocentros/. It then asserts that the response has an HTTP status code of 200 OK,
        and that there are two hemocentros in the database.
        
        :param self: Represent the instance of the class
        :return: The status code 200 (ok) and the length of the response data is 2, which means that it has two hemocenters
        :doc-author: Trelent
        """
        response = self.client.get('/api/v1/hemocentros/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  


    def test_detail_hemocentro(self):
        """
        The test_detail_hemocentro function tests the detail view of the Hemocentro model.
        It checks if it returns a 200 OK status code, and if its data is correct.
        
        :param self: Represent the instance of the class
        :return: The following error:
        :doc-author: Trelent
        """
        response = self.client.get(f'/api/v1/hemocentros/{self.hemocentro_1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Hemo Teste 1')
        self.assertEqual(response.data['cep'], '12365478')  
        self.assertEqual(response.data['logradouro'], 'Rua Teste 1')


    def test_create_hemocentro(self):
        """
        The test_create_hemocentro function creates a new Hemocentro object and then checks that the response is 201 Created.
        
        
        :param self: Represent the instance of the class
        :return: A 201 status code
        :doc-author: Trelent
        """
        novo_dado = { 'nome': 'Hemo Teste 154',
                      'cep': '12365478',
                      'logradouro': 'Rua Teste 1',
                      'bairro': 'Bairro Teste 1',
                      'numero': '111',
                      'localidade': 'Localidade Teste 1',
                      'uf': 'TS',
                      'telefone': '1234567890',
                      'email': 'teste1@email.com' 
                      }
        response = self.client.post('/api/v1/hemocentros/', novo_dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_update_hemocentro(self):
        """
        The test_update_hemocentro function tests the update of a Hemocentro object.
        It first creates a Hemocentro object, then it updates its name and checks if the new name is correct.
        
        :param self: Represent the instance of the class
        :return: A 200 status code, but the test fails
        :doc-author: Trelent
        """
        dados_atualizados = {
                      'nome': 'Hemo Teste 1 ALTERADO',
                      'cep': '12365478',
                      'logradouro': 'Rua Teste 1',
                      'bairro': 'Bairro Teste 1',
                      'numero': '111',
                      'localidade': 'Localidade Teste 1',
                      'uf': 'TS',
                      'telefone': '1234567890',
                      'email': 'teste1@email.com' 
                      }
        response = self.client.put(f'/api/v1/hemocentros/{self.hemocentro_1.id}', dados_atualizados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hemocentro.objects.get(id=self.hemocentro_1.id).nome, 'Hemo Teste 1 ALTERADO')  # Verifica se o campo1 foi atualizado


    def test_patch_hemocentro(self):
        """
        The test_patch_hemocentro function tests the PATCH method for a Hemocentro object.
        It first creates a Hemocentro object, then it uses the Django REST Framework's client to make an HTTP request to update that object.
        The test asserts that the response status code is 200 OK and also asserts that the name of our updated hemocentro is 'Hemo Teste 1 ALTERADO'.
        
        :param self: Represent the instance of the class
        :return: A 200 status code and the name of the hemocentro is changed to 'hemo teste 1 alterado'
        :doc-author: Trelent
        """
        dados_parciais_atualizados = {'nome': 'Hemo Teste 1 ALTERADO'}
        response = self.client.patch(f'/api/v1/hemocentros/{self.hemocentro_1.id}', dados_parciais_atualizados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hemocentro.objects.get(id=self.hemocentro_1.id).nome, 'Hemo Teste 1 ALTERADO')  # Verifica se o campo1 foi atualizado


    def test_delete_hemocentro(self):
        """
        The test_delete_hemocentro function tests the DELETE method on the Hemocentro endpoint.
        It first creates a Hemocentro object, then it makes a DELETE request to /api/v2/hemocentros/{id} and checks if
        the response status code is 204 NO CONTENT. It also asserts that there's only one object in the database.
        
        :param self: Represent the instance of the class
        :return: A 204 status code
        :doc-author: Trelent
        """
        response = self.client.delete(f'/api/v1/hemocentros/{self.hemocentro_1.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Hemocentro.objects.count(), 1)  # Verifica se apenas um objeto foi excluído


    def test_create_hemocentro_empty_nome(self):
        """
        The test_create_hemocentro_empty_nome function tests the creation of a new Hemocentro object with an empty nome field.
        The test should return a 400 BAD REQUEST status code, since the nome field is required.
        
        :param self: Represent the instance of the class
        :return: 400
        :doc-author: Trelent
        """
        novo_dado = { 'cep': '12365478',
                      'logradouro': 'Rua Teste 1',
                      'bairro': 'Bairro Teste 1',
                      'numero': '111',
                      'localidade': 'Localidade Teste 1',
                      'uf': 'TS',
                      }
        response = self.client.post('/api/v1/hemocentros/', novo_dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    

    def test_create_hemocentro_empty_cep(self):
     
        novo_dado = { 'nome': 'Hemo Teste 1 ALTERADO', 
                      'logradouro': 'Rua Teste 1',
                      'bairro': 'Bairro Teste 1',
                      'numero': '111',
                      'localidade': 'Localidade Teste 1',
                      'uf': 'TS',
                      }
        response = self.client.post('/api/v1/hemocentros/', novo_dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 

    def test_create_hemocentro_empty_logradouro(self):
     
        novo_dado = { 'nome': 'Hemo Teste 1 ALTERADO', 
                      'cep': '12365478',
                      'bairro': 'Bairro Teste 1',
                      'numero': '111',
                      'localidade': 'Localidade Teste 1',
                      'uf': 'TS',
                      }
        response = self.client.post('/api/v1/hemocentros/', novo_dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    

    def test_create_hemocentro_empty_bairro(self):
     
        novo_dado = { 'nome': 'Hemo Teste 1 ALTERADO', 
                      'cep': '12365478',
                      'logradouro': 'Rua Teste 1',
                      'numero': '111',
                      'localidade': 'Localidade Teste 1',
                      'uf': 'TS',
                      }
        response = self.client.post('/api/v1/hemocentros/', novo_dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_hemocentro_empty_numero(self):
     
        novo_dado = { 'nome': 'Hemo Teste 1 ALTERADO', 
                      'cep': '12365478',
                      'logradouro': 'Rua Teste 1',
                      'numero': '111',
                      'localidade': 'Localidade Teste 1',
                      'uf': 'TS',
                      }
        response = self.client.post('/api/v1/hemocentros/', novo_dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    

    def test_create_hemocentro_empty_localidade(self):
     
        novo_dado = { 'nome': 'Hemo Teste 1 ALTERADO', 
                      'cep': '12365478',
                      'logradouro': 'Rua Teste 1',
                      'bairro': 'Bairro Teste 1',
                      'numero': '111',
                      'uf': 'TS',
                      }
        response = self.client.post('/api/v1/hemocentros/', novo_dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    

    def test_create_hemocentro_empty_uf(self):
     
        novo_dado = { 'nome': 'Hemo Teste 1 ALTERADO', 
                      'cep': '12365478',
                      'logradouro': 'Rua Teste 1',
                      'bairro': 'Bairro Teste 1',
                      'numero': '111',
                      'localidade': 'Localidade Teste 1',
                      }
        response = self.client.post('/api/v1/hemocentros/', novo_dado, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)








        
