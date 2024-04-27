from django.db import models

from auditlog.registry import auditlog


class Hemocentro(models.Model):
    nome = models.CharField(max_length=300, unique=True)
    sigla = models.CharField(max_length=50, unique=True)
    cep = models.CharField(max_length=8)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    logradouro = models.CharField(max_length=300)
    bairro = models.CharField(max_length=300)
    numero = models.CharField(max_length=20, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    localidade = models.CharField(max_length=300)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    estoque_atual=models.FloatField()
    estoque_ideal=models.FloatField()
    obs = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    

    def __str__(self):
        return self.nome

auditlog.register(Hemocentro)