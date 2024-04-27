from rest_framework import response, status
from django.db.models.signals import post_save
from django.dispatch import receiver

from coletas.models import Coleta    
from doadores.models import Doador
from hemocentros.models import Hemocentro

# escutando evento post_save da tabela Coleta:
@receiver(post_save, sender=Coleta)
def atualiza_ultima_doacao(sender, instance, ** kwargs):
    

    """
    The atualiza_ultima_doacao function is used to update the last donation date of a donor.
        It receives as parameter an instance of the Donation model and updates the field ultima_doacao in Doador model.
    
    :param sender: Identify the model that is being saved
    :param instance: Get the instance of the object that is being saved
    :param ** kwargs: Pass keyworded, variable-length argument list
    :return: None
    :doc-author: Trelent
    """
    try:
        if instance.data_hora:
            
            doadores = Doador.objects.filter(cpf=instance.cpf)
    
            for doador in doadores:
               
                doador.ultima_doacao = instance.data_hora
                doador.save()

    except Exception as e:
            return response.Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



@receiver(post_save, sender=Coleta)
def atualiza_estoque_hemocentro(sender, instance, ** kwargs):
    
    try:
        if instance.quantidade:
        
            hemocentros = Hemocentro.objects.filter(id=instance.hemocentro)
                
            for hemocentro in hemocentros:
                # transformar p/ ml
                #qtde_ml = instance.quantidade/1000
                
                # Verificar se status é disponível ou recebido = SOMA
                if instance.status == 'disponivel' or instance.status == 'recebido': 
                    # SOMA com estoque              
                    hemocentro.estoque_atual += instance.unidade
                else:
                    # SUBTRAI do estoque              
                    hemocentro.estoque_atual -= instance.unidade

                print(hemocentro.estoque_atual)
                hemocentro.save()

    except Exception as e:
            return response.Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)