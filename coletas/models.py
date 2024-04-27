from django.db import models

from auditlog.registry import auditlog

from doadores.models import Doador
from hemocentros.models import Hemocentro
from app.utils.choices import TIPO_SANGUE_CHOICES, FATOR_RH_CHOICES, ORIGEM_TIPO_CHOICES, STATUS_SANGUE_CHOICES


class Coleta(models.Model):
    
    origem_tipo = models.CharField(
        max_length=20,
        choices=ORIGEM_TIPO_CHOICES,
        blank=True,
        null=True
    )
    cpf = models.CharField(max_length=20, blank=True, null=True)
    hemocentro = models.IntegerField()
    unidade = models.IntegerField()
    quantidade = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)
    tipo_sanguineo =  models.CharField(
        max_length=20,
        choices=TIPO_SANGUE_CHOICES,
        blank=True,
        null=True
    )
    fator_rh =  models.CharField(
        max_length=1,
        choices=FATOR_RH_CHOICES,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_SANGUE_CHOICES)
    origem = models.CharField(max_length=100, blank=True, null=True)
    destino = models.CharField(max_length=100, blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


auditlog.register(Coleta)
    
   