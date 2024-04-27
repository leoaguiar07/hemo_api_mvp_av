from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from logs.models import AuditLogLogentry
from logs.serializers import LogSerializer


class LogListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = AuditLogLogentry.objects.all()
    serializer_class = LogSerializer
    
    @swagger_auto_schema(operation_description="Lista todos os Logs.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    