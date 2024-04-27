from django.contrib import admin
from hemocentros.models import Hemocentro


@admin.register(Hemocentro)
class HemocentroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cep', 'logradouro', 'numero', 'bairro', 'localidade', 'uf', 'telefone', 'email', 'estoque_atual', 'estoque_ideal', 'created_at')
