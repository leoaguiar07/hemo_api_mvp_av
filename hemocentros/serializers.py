from rest_framework import serializers

from hemocentros.models import Hemocentro


class HemocentroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hemocentro
        fields = '__all__'
