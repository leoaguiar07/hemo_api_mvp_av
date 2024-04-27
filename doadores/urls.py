from django.urls import path
from . import views


urlpatterns = [
    path('doadores/', views.DoadorCreateListView.as_view(), name='doadores-create-list'),
    path('doadores/<int:pk>', views.DoadorRetrieveUpdateDestroyAPIView.as_view(), name='doadores-retrieve-update-destroy'),
    path('doadores_estatisticas/', views.DoadorStatsView.as_view(),name='movie-stats-view'),
    path('doadores_proximos/<latitude>/<longitude>/<distancia>', views.DoadorProximosView.as_view(), name='doadores_proximos'),
]
