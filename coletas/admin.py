from django.contrib import admin
from coletas.models import Coleta

# Register your models here.

@admin.register(Coleta)
class ColetaAdmin(admin.ModelAdmin):
    list_display = ('id', 'origem_tipo', 'cpf', 'hemocentro', 'quantidade', 'data_hora', 'tipo_sanguineo', 'fator_rh', 'status', 'created_at')
