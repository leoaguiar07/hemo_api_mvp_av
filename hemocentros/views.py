from django.db.models import Count,Sum
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated

from hemocentros.models import Hemocentro
from hemocentros.serializers import HemocentroSerializer

from drf_yasg.utils import swagger_auto_schema


class HemocentroCreateListView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Hemocentro.objects.all().order_by('uf','localidade')
    serializer_class = HemocentroSerializer
    
     
    @swagger_auto_schema(operation_description="Lista todos os hemocentros.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Cria hemocentros.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

class HemocentroRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Hemocentro.objects.all().order_by('uf','localidade')
    serializer_class = HemocentroSerializer

    @swagger_auto_schema(operation_description="Lista hemocentros, filtrando por ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Atualiza hemocentros, filtrando por id.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Atualiza hemocentros, filtrando por ID e permitindo indicar só o campo usado para atualização.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    
    @swagger_auto_schema(operation_description="Deleta hemocentros, filtrando por ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)



class HemocentroStatsView(views.APIView):
    #permission_classes = (IsAuthenticated,)

    queryset = Hemocentro.objects.all()
    
    @swagger_auto_schema(operation_description="Mostra estatísticas dos hemocentros como: total de hemocentros por estado.")
    def get(self, request):
        estoque_ideal = self.queryset.aggregate(estoque_ideal=Sum('estoque_ideal'))['estoque_ideal']
        
        #self.queryset.annotate(hemocentros=Count('id')).annotate(estoque_ideal_litros=Sum('estoque_ideal'))
        estoque_atual = self.queryset.aggregate(estoque_atual=Sum('estoque_atual'))['estoque_atual']
        #self.queryset.annotate(hemocentros=Count('id')).annotate(estoque_total_litros=Sum('estoque_atual'))
        total_hemocentros = self.queryset.count()
        hemocentros_by_uf = self.queryset.values('uf').annotate(hemocentros=Count('id')).annotate(estoque_total_unidades=Sum('estoque_atual')).annotate(estoque_ideal_unidades=Sum('estoque_ideal'))
       
        return response.Response(
            data={
                'estoque_ideal_unidades': estoque_ideal,
                'estoque_atual_unidades': estoque_atual,
                'total_hemocentros': total_hemocentros,
                'hemocentros_by_uf': hemocentros_by_uf,
            }, status=status.HTTP_200_OK,
        )

