from rest_framework.test import APITestCase
from rest_framework import status

from hemocentros.models import Hemocentro


class HemocentroAPITestCase(APITestCase):

    def setUp(self):
        
        """
        The setUp function is called before each test function.
        It creates a Hemocentro object and saves it to the database.
        
        :param self: Represent the instance of the class
        :return: A hemocentro object
        :doc-author: Trelent
        """
        
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
        

    def test_list_hemocentro(self):     
       
        """
        The test_list_hemocentro function tests the list_hemocentro view.
        It does so by making a GET request to /api/v2/hemocentros/.
        The expected result is that the response status code will be 200 OK, and that there will be one hemocentro in the database. 
        
        
        :param self: Represent the instance of the class
        :return: The following error:
        :doc-author: Trelent
        """

        url = '/api/v1/hemocentros/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
        self.assertEqual(response.data[0]['nome'],'Hemo 1') 



    def test_detail_hemocentro(self):
         
        """
        The test_detail_hemocentro function tests the detail view of a Hemocentro.
        It does so by making a GET request to /api/v2/hemocentros/&lt;id&gt; and checks that the response is 200 OK.
        
        
        :param self: Represent the instance of the class
        :return: The name of the hemocentro, but it should return all the data from this hemocentro
        :doc-author: Trelent
        """
        
        url = f'/api/v1/hemocentros/{self.hemocentro_1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'],'Hemo 1') 

#TODO: ver erro teste na função abaixo 
    def test_create_hemocentro(self):
              
        """
        The test_create_hemocentro function tests the creation of a Hemocentro object.
        It does so by sending a POST request to the /api/v2/hemocentros endpoint with data for 
        a new Hemocentro object, and then checks that the response status code is 201 (CREATED) 
        and that there are now two objects in the database.
        
        :param self: Represent the instance of the class
        :return: A 201 status code, but the test fails
        :doc-author: Trelent
        """

        data = {
                'nome':'Hemo 2',
                'cep':12365478,
                'logradouro':'Rua 2',
                'bairro':'Bairro 2',
                'numero':'222',
                'complemento':'Loja C',
                'localidade':'Localidade 2',
                'uf':'SP',
                'telefone':'1234567890',
                'email':'teste2@email.com',
                'estoque_atual':80.36,
                'estoque_ideal':227.0
                }
        
        url = '/api/v1/hemocentros/'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hemocentro.objects.count(), 2)
    
    
    def test_patch_hemocentro(self):
       
        """
        The test_patch_hemocentro function tests the PATCH method for the Hemocentro model.
        It first creates a new_data dictionary with a key-value pair of 'nome':'Hemo 1 ALTER'.
        Then it uses this data to make a request to the API endpoint /api/v2/hemocentros/{self.hemocentro_id} using 
        the self.client object, which is an instance of APIClient from Django REST Framework (DRF). The response is then 
        stored in response and its status code is checked against HTTP 200 OK, meaning that everything went well and that 
        
        :param self: Represent the instance of the class
        :return: The following error:
        :doc-author: Trelent
        """
        
        new_data = {
                    'nome': 'Hemo 1 ALTER'
                   }
        
        url = f'/api/v1/hemocentros/{self.hemocentro_1.id}'
        response = self.client.patch(url , new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hemocentro.objects.get(id=self.hemocentro_1.id).nome, 'Hemo 1 ALTER')  


  
    def test_update_hemocentro(self):
        
        """
        The test_update_doador function tests the update of a Hemocentro object.
            It first creates a new Hemocentro object, then updates it with new data.
            The test checks that the status code is 200 OK and that the name has been updated.
        
        :param self: Represent the instance of the class
        :return: The following error:
        :doc-author: Trelent
        """
        
        new_data = {
                'nome':'Hemo 1 ALTER',
                'cep':12365478,
                'logradouro':'Rua 1',
                'bairro':'Bairro 1',
                'numero':'111',
                'complemento':'Loja B',
                'localidade':'Localidade 1',
                'uf':'SP',
                'telefone':'1234567890',
                'email':'teste1@email.com',
                'estoque_atual':80.36,
                'estoque_ideal':227.0
                   }
        
        url = f'/api/v1/hemocentros/{self.hemocentro_1.id}'
        response = self.client.put(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Hemocentro.objects.get(id=self.hemocentro_1.id).nome, 'Hemo 1 ALTER')



    def test_delete_hemocentro(self):
       
        """
        The test_delete_hemocentro function tests the DELETE method for the Hemocentro model.
        It first creates a hemocentro object, then it deletes it and checks if its status code is 204 (no content)
        and if there are no more objects in the database.
        
        :param self: Represent the instance of the class
        :return: A 204 status code and the number of objects in hemocentro is 0
        :doc-author: Trelent
        """
        
        url = f'/api/v1/hemocentros/{self.hemocentro_1.id}'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Hemocentro.objects.count(), 0) 




