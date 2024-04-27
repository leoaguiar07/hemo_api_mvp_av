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
                                                      peso_aproximado=89,
                                                      ultima_doacao='2021-01-11',
                                                      login='login1',
                                                      senha='senha1'
                                                      )
        
    
    def test_list_doador(self):     

        """
        The test_list_doadores function tests the list_doadores view.
        It checks that the response status code is 200, and that there are two doadores in the database.
        
        
        :param self: Represent the instance of the class
        :return: A list of donors, but i don't know how to test the return
        :doc-author: Trelent
        """
        
        url = '/api/v1/doadores/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
        self.assertEqual(response.data[0]['nome'],'Doador 1') 

    
    def test_detail_doador(self):
              
        """
        The test_detail_doadores function tests the detail_doadores function in views.py
        
        :param self: Represent the instance of the class
        :return: The following error:
        :doc-author: Trelent
        """

        url = f'/api/v1/doadores/{self.doador_1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'],'Doador 1') 


    def test_create_doador(self):
        
        """
        The test_create_doadores function tests the creation of a new doador object.
        It does so by sending a POST request to the /api/v2/doadores endpoint with valid data, and then checks that 
        the response status code is 201 (CREATED), and that there are now two objects in the database.
        
        :param self: Represent the instance of the class
        :return: The following error:
        :doc-author: Trelent
        """

        data = { 
                'nome':'Doador 2',
                'genero':'Homem cisgênero',
                'cpf':12345678902,
                'cep':12365478,
                'logradouro':'Rua 2',
                'bairro':'Bairro 2',
                'numero':'222',
                'complemento':'apto 222',
                'localidade':'Localidade 2',
                'uf':'RJ',
                'telefone':'1234567890',
                'email':'email2@email.com',
                'nascimento':'1992-12-02',
                'peso_aproximado':89,
                'ultima_doacao':'2022-02-12',
                'login':'login2',
                'senha':'senha2'
                 }
        
        url = '/api/v1/doadores/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Doador.objects.count(), 2)


    
    def test_patch_doador(self):
                
        """
        The test_patch_doador function tests the PATCH method on the doador endpoint.
        It first creates a new Doador object, then it makes a PATCH request to update that object's name.
        Finally, it asserts that the response status code is 200 OK and that the updated Doador's name is 'Doador 1 ALTERADO'.
        
        :param self: Represent the instance of the class
        :return: A 200 ok response, but the test fails
        :doc-author: Trelent
        """

        new_data = {
                    'nome': 'Doador 1 ALTER'
                   }
        
        url = f'/api/v1/doadores/{self.doador_1.id}'
        response = self.client.patch(url , new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Doador.objects.get(id=self.doador_1.id).nome, 'Doador 1 ALTER')  


    
    def test_update_doador(self):
        
        """
        The test_update_doador function tests the update of a doador.
            It does so by first creating a new Doador object, then updating it with new data.
            The test checks that the response status code is 200 OK and that the updated Doador's name is 'Doador 1 ALTER'.
        
        :param self: Represent the instance of the class
        :return: The following error
        :doc-author: Trelent
        """

        new_data = {
                    'nome':'Doador 1 ALTER',
                    'genero':'Homem cisgênero',
                    'cpf':'12345678901',
                    'cep':'12365478',
                    'logradouro':'Rua 1',
                    'bairro':'Bairro  1',
                    'numero':'111',
                    'complemento ': 'apto 111',
                    'localidade':'Localidade 1',
                    'uf':'RJ',
                    'telefone':'1234567890',
                    'email':'email1@email.com',
                    'nascimento':'1991-11-01',
                    'peso_aproximado':89,
                    'ultima_doacao':'2021-01-11',
                    'login':'login1',
                    'senha':'senha1'
                    }
        
        url = f'/api/v1/doadores/{self.doador_1.id}'
        response = self.client.put(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Doador.objects.get(id=self.doador_1.id).nome, 'Doador 1 ALTER')


    
    def test_delete_doador(self):
        
        """
        The test_delete_doador function tests the DELETE method for a single doador.
        It first creates a new Doador object, then it makes an HTTP request to delete that object.
        The test asserts that the response status code is 204 (no content), and also asserts that there are no more Doador objects in the database.
        
        :param self: Represent the instance of the class
        :return: A 204 status code, which means that the server successfully processed the request and is not returning any content
        :doc-author: Trelent
        """

        url = f'/api/v1/doadores/{self.doador_1.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Doador.objects.count(), 0) 






