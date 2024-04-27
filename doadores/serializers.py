from rest_framework import serializers
from doadores.models import Doador


class DoadorSerializer(serializers.ModelSerializer):
    #TODO: Fazer os teste dessas validações 
    #login = serializers.CharField(min_length=5, max_length=20)
    #senha = serializers.CharField(min_length=5, max_length=20)
       
    class Meta:
        model = Doador
        fields = '__all__'
        

