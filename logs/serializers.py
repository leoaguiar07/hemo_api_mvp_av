from rest_framework import serializers

from logs.models import AuditLogLogentry


class LogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AuditLogLogentry
        fields = '__all__'
