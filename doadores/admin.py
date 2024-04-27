from django.contrib import admin
from doadores.models import Doador



@admin.register(Doador)


class DoadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf','cep','latitude', 'longitude', 'logradouro', 'numero','complemento', 'bairro', 'localidade', 'uf', 'telefone', 'email', 'nascimento', 'peso_aproximado', 'ultima_doacao', 'login', 'created_at')


