from django.urls import path
from . import views


urlpatterns = [
    path('hemocentros/', views.HemocentroCreateListView.as_view(), name='hemocentro-create-list'),
    path('hemocentros/<int:pk>', views.HemocentroRetrieveUpdateDestroyAPIView.as_view(), name='hemocentro-retrieve-update-destroy'),
    path('hemocentros_estatisticas/', views.HemocentroStatsView.as_view(),name='movie-stats-view'),
]
