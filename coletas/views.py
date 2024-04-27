from django.db.models import Count, Sum, F, Value
from django.db.models.functions import Concat, ExtractDay  
from datetime import date, datetime
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated

from app.utils.utils import get_mes_passado,get_dias_mes_passado

from drf_yasg.utils import swagger_auto_schema

from coletas.models import Coleta
from coletas.serializers import ColetaSerializer


class ColetaCreateListView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)

    queryset = Coleta.objects.all().order_by('data_hora')
    serializer_class = ColetaSerializer
    
    @swagger_auto_schema(operation_description="Lista todas as coletas.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Cria coletas.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    


class ColetaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)

    queryset = Coleta.objects.all().order_by('data_hora')
    serializer_class = ColetaSerializer

    @swagger_auto_schema(operation_description="Lista coletas, filtrando por ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Atualiza coletas, filtrando por id.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Atualiza coletas, filtrando por ID e permitindo indicar só o campo usado para atualização.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    
    @swagger_auto_schema(operation_description="Deleta coletas, filtrando por ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ColetaStatsView(views.APIView):
    #permission_classes = (IsAuthenticated,)

    queryset = Coleta.objects.all()
    #queryset = Coleta.objects.filter(data_hora__date=date.today(),origem_tipo='coleta')

    @swagger_auto_schema(operation_description="Mostra estatísticas de coletas como: total de doações hoje ...")
    def get(self, request):

        #queryset = Coleta.objects.all()
        #queryset_today (hoje)
        queryset_today = self.queryset.filter(data_hora__date=date.today(),origem_tipo='coleta')
                
        total_doacoes_tipos_hoje = queryset_today.values('tipo_sanguineo','fator_rh').annotate(count=Count('id'))
        total_doacoes_hoje = queryset_today.count()
        total_sangue_ml_hoje = queryset_today.aggregate(total_sangue_ml_hoje=Sum('quantidade'))['total_sangue_ml_hoje']
                   
        total_sangue_un_hoje = queryset_today.aggregate(total_sangue_un_hoje=Sum('unidade'))['total_sangue_un_hoje']       
        if total_sangue_un_hoje == None:
            total_sangue_un_hoje = 0
        
        #queryset_mes_atual (hoje)
        mes_atual = datetime.now().month
        
        queryset_mes_atual = self.queryset.filter(data_hora__month=mes_atual,origem_tipo='coleta')
                
        #total_doacoes_tipos_mes_atual = queryset_mes_atual.values('data_hora','tipo_sanguineo','fator_rh').annotate(count=Count('id'))
        
        #total_doacoes_tipos_mes_atual = queryset_mes_atual.annotate(tipo_e_rh=Concat('tipo_sanguineo', Value(''), 'fator_rh')).values('data_hora', 'tipo_e_rh').annotate(count=Count('id'))


        resultados = queryset_mes_atual.annotate(
                                        tipo_e_rh=Concat('tipo_sanguineo', Value(''), 'fator_rh'),
                                        dia=ExtractDay('data_hora')
                                        ).values('dia', 'tipo_e_rh').annotate(
                                        count=Count('id')
                                        )
        # Inicialize o dicionário para armazenar os resultados
        resultado_final = {}
        # Itere sobre os resultados e preencha o dicionário
        for resultado in resultados:
            dia = str(resultado['dia']).zfill(2)  # Formate o dia como '01', '02', etc.
            tipo_e_rh = resultado['tipo_e_rh']
            count = resultado['count']
            chave = f'dia:{dia}, {tipo_e_rh}'
            resultado_final[chave] = count
        total_doacoes_tipos_mes_atual = resultado_final






        total_doacoes_mes_atual = queryset_mes_atual.count()
        total_sangue_ml_mes_atual = queryset_mes_atual.aggregate(total_sangue_ml_mes_atual=Sum('quantidade'))['total_sangue_ml_mes_atual']
        total_sangue_un_mes_atual = queryset_mes_atual.aggregate(total_sangue_unidade_mes_atual=Sum('unidade'))['total_sangue_unidade_mes_atual']


        #queryset_ultimo_mes (ultimo_mes)
                
        mes_passado = get_mes_passado()
                
        queryset_mes_passado = self.queryset.filter(data_hora__month=mes_passado,origem_tipo='coleta')

        total_doacoes_tipos_mes_passado = queryset_mes_passado.values('tipo_sanguineo','fator_rh').annotate(count=Count('id'))
        total_doacoes_mes_passado = queryset_mes_passado.count()
        total_sangue_ml_mes_passado = queryset_mes_passado.aggregate(total_sangue_ml_mes_passado=Sum('quantidade'))['total_sangue_ml_mes_passado']
        total_sangue_un_mes_passado = queryset_mes_passado.aggregate(total_sangue_un_mes_passado=Sum('unidade'))['total_sangue_un_mes_passado']
        #media_diaria_doacoes_mes_passado = total_doacoes_mes_passado/dia[2]
        print(total_sangue_un_mes_passado)
        num_dias_mes_passado = get_dias_mes_passado()

        #verifica numero de doações do mês passado
        if total_sangue_un_mes_passado == None:
            media_diaria_un_mes_passado = 0
        else:
            media_diaria_un_mes_passado = total_sangue_un_mes_passado/num_dias_mes_passado                       
                
        # Count de doacoes por dia do mes atual agrupado por tipo
        #data: [{dia:'01',A-: 35,A+: 67,AB-: 15, AB+: 15,O-: 15,O+: 15},
        #       {dia:'02',A-: 35,A+: 67,AB-: 15, AB+: 15,O-: 15,O+: 15}]

        return response.Response(
            data={
                # Mês passado:
                'total_doacoes_mes_passado': total_doacoes_mes_passado,
                'total_sangue_ml_mes_passado': total_sangue_ml_mes_passado,
                'total_sangue_un_mes_passado': total_sangue_un_mes_passado,

                
                'media_diaria_un_mes_passado': media_diaria_un_mes_passado,
                'total_doacoes_tipos_mes_passado': total_doacoes_tipos_mes_passado,
                #'media_diaria_doacoes_mes_passado': media_diaria_doacoes_mes_passado,
                # Mês Atual:
                'total_doacoes_mes_atual': total_doacoes_mes_atual,
                'total_sangue_ml_mes_atual': total_sangue_ml_mes_atual,
                'total_sangue_un_mes_atual': total_sangue_un_mes_atual,
                'total_doacoes_tipos_mes_atual': total_doacoes_tipos_mes_atual,
                # Hoje:
                'total_doacoes_hoje': total_doacoes_hoje,
                'total_sangue_ml_hoje': total_sangue_ml_hoje,
                'total_sangue_un_hoje': total_sangue_un_hoje,                
                'total_doacoes_tipo_hoje': total_doacoes_tipos_hoje                
            }, status=status.HTTP_200_OK,
        )
