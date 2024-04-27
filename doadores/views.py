from django.db.models import Count
from datetime import datetime, timedelta
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated


from drf_yasg.utils import swagger_auto_schema

from app.utils.utils import get_mes_passado
from doadores.models import Doador
from coletas.models import Coleta
from doadores.serializers import DoadorSerializer
from app.utils.utils import get_distance
from app.utils.constants import IDADE_MINIMA, IDADE_MAXIMA, PESO_MINIMO



class DoadorCreateListView(generics.ListCreateAPIView):
    #permission_classes = (IsAuthenticated,)

    queryset = Doador.objects.all().order_by('uf','localidade')
    serializer_class = DoadorSerializer
    
    @swagger_auto_schema(operation_description="Lista todos os doadores.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Cria doadores.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    


class DoadorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)

    queryset = Doador.objects.all().order_by('uf','localidade')
    serializer_class = DoadorSerializer

    @swagger_auto_schema(operation_description="Lista doadores, filtrando por ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Atualiza doadores, filtrando por id.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Atualiza doadores, filtrando por ID e permitindo indicar só o campo usado para atualização.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    
    @swagger_auto_schema(operation_description="Deleta doadores, filtrando por ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)




class DoadorStatsView(views.APIView):
    #permission_classes = (IsAuthenticated,)

    queryset= Doador.objects.all()

    @swagger_auto_schema(operation_description="Mostra estatísticas dos doares como: total de possíveis doadores cadastrados por estado e possíveis doadores que preenchem os pré-requisitos agrupados por estado.")
    def get(self, request):  

        # Calcular a data de nascimento para a idade mínima
        data_minima = datetime.now() - timedelta(days=IDADE_MINIMA*365)
        print(data_minima)

        # Calcular a data de nascimento para a idade máxima 
        data_maxima = datetime.now() - timedelta(days=IDADE_MAXIMA*365)
        #print(data_maxima)
        
        #total doadores (não verificados)
        total_doadores= self.queryset.count()

        #total doadores (verificados)
        queryset_verificados = self.queryset.filter(peso_aproximado__gte=int(PESO_MINIMO), nascimento__range=(data_maxima, data_minima))
        #total_doadores= self.get_queryset().count()
        total_doadores_verificados = queryset_verificados.count()
        #self.get_queryset().count()
        #doadores_verificados_by_uf = self.get_queryset().filter(peso_aproximado__gte=int(PESO_MINIMO), nascimento__range=(data_maxima, data_minima)).values('uf').annotate(count=Count('id'))

        # total doadores mês passado
    
        mes_passado = get_mes_passado()
        #print(mes_passado)
        queryset_mes_passado = self.queryset.filter(created_at__month=mes_passado)
        queryset_verificados_mes_passado = queryset_verificados.filter(created_at__month=mes_passado)
        
        total_doadores_mes_passado = queryset_mes_passado.count()
        total_doadores_verificados_mes_passado = queryset_verificados_mes_passado.count()
        total_doadores_verificados_mes_passado_by_uf = queryset_verificados_mes_passado.values('uf').annotate(count=Count('id'))

        
        #total doadores mês atual (hoje)
        mes_atual = datetime.now().month
        queryset_mes_atual = self.queryset.filter(created_at__month=mes_atual)
        queryset_verificados_mes_atual = queryset_verificados.filter(created_at__month=mes_atual)

        total_doadores_mes_atual = queryset_mes_atual.count()
        total_doadores_verificados_mes_atual = queryset_verificados_mes_atual.count()
        total_doadores_verificados_mes_atual_by_uf = queryset_verificados_mes_atual.values('uf').annotate(count=Count('id'))
                
        # CALCULAR NUMERO DE DOARES CADASTRADOS QUE FIZERAM DOAÇÃO
        # Contar quantos registros na tabela Doadores têm o campo 'cpf' presente na tabela Coletas
        quantidade = Doador.objects.filter(cpf__in=Coleta.objects.values('cpf')).count()
        
        



        return response.Response(
            data={
              'total_doadores':total_doadores,
              'total_doadores_verificados': total_doadores_verificados,
              'total_doadores_em_coleta': quantidade,

              # Mês passado
              'total_doadores_mes_passado': total_doadores_mes_passado,
              'total_doadores_verificados_mes_passado': total_doadores_verificados_mes_passado,
              'total_doadores_verificados_mes_passado_by_uf': total_doadores_verificados_mes_passado_by_uf,

              # Mês Atual
              'total_doadores_mes_atual': total_doadores_mes_atual,
              'total_doadores_verificados_mes_atual': total_doadores_verificados_mes_atual,
              'total_doadores_verificados_mes_atual_by_uf':total_doadores_verificados_mes_atual_by_uf


               # 'doadores_verificados_by_uf': doadores_verificados_by_uf,
            }, status=status.HTTP_200_OK,
        )



class DoadorProximosView(views.APIView):
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Doador.objects.all()
    
    @swagger_auto_schema(operation_description="Mostra doadores dentro da distancia informada (distancia) a partir da geolocalização informada (latitude, longitude).")
    def get(self, request, latitude, longitude, distancia):

        doadores_proximos = []
        for doador in self.get_queryset():
            distancia_calculada = get_distance(latitude, longitude,doador.latitude,doador.longitude)
            
            if  float(distancia_calculada) < float(distancia):
                doadores_proximos.append(doador)

        # Serializa os objetos Doador
        serializer = DoadorSerializer(doadores_proximos, many=True)

        return response.Response(
                data=serializer.data, 
                status=status.HTTP_200_OK
            )