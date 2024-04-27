from rest_framework import serializers
from datetime import datetime

from coletas.models import Coleta


def validar_data_futura(value):
    
    """
    Verifica se a data fornecida é no futuro.
    """
    if value < datetime.now():
        raise serializers.ValidationError("A data deve estar no futuro.")


class ColetaSerializer(serializers.ModelSerializer):
   
    data_hora = serializers.DateTimeField(validators=[validar_data_futura])
    
    
    class Meta:
        model = Coleta
        fields = '__all__'
        

