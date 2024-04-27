from rest_framework import response, status
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.utils.utils import get_geolocalizacao
from doadores.models import Doador





# escutando evento post_save da tabela Doador:
@receiver(post_save, sender=Doador)

def doador_post_save(sender, instance, ** kwargs):
    try:
        geo_data = get_geolocalizacao(instance.bairro, instance.localidade)
        if geo_data is not None:
            latitude, longitude = geo_data[0], geo_data[1]
            if not instance.latitude or not instance.longitude:
                instance.latitude = latitude
                instance.longitude = longitude
                instance.save(update_fields=['latitude', 'longitude'])

    except Exception as e:
            return response.Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

