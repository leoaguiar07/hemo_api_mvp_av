from django.urls import path
from . import views


urlpatterns = [
    path('coletas/', views.ColetaCreateListView.as_view(), name='coletas-create-list'),
    path('coletas/<int:pk>', views.ColetaRetrieveUpdateDestroyAPIView.as_view(), name='coletas-retrieve-update-destroy'),
    path('coletas_estatisticas/', views.ColetaStatsView.as_view(),name='coleta-stats-view'),
    #path('coletas_proximos/<latitude>/<longitude>/<distancia>', views.DoadorProximosView.as_view(), name='doadores_proximos'),
]
