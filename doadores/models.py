from django.db import models

from auditlog.registry import auditlog

from app.utils.choices import TIPO_SANGUE_CHOICES, FATOR_RH_CHOICES, GENEROS_CHOICES


#TODO: Gênero não pode ser nulo, afeta validação de ultima doação
class Doador(models.Model):
    nome = models.CharField(max_length=300)
    genero =  models.CharField(
        max_length=20,
        choices=GENEROS_CHOICES,
        blank=True,
        null=True
        #TODO: INSERIR CAMPO DE GÊNERO NOS TESTES
        #TODO: colocar os campos de latitude e longitude com read_ony
    )
    cpf = models.CharField(max_length=20, unique=True)
    cep = models.IntegerField()
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    logradouro = models.CharField(max_length=300)
    bairro = models.CharField(max_length=300)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    localidade = models.CharField(max_length=300)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    nascimento = models.DateField()
    peso_aproximado = models.FloatField()
    tipo_sanguineo =  models.CharField(
        max_length=2,
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
    ultima_doacao = models.DateField(blank=True, null=True)
    login =  models.CharField(max_length=20, unique=True)
    senha = models.CharField(max_length=20)
    obs = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

auditlog.register(Doador)