
from django.contrib import admin
from django.urls import path, include
#from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="HEMO API",
      default_version='v1',
      description="Descrição da API DRF",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="leorodriguesaguiar@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # OPENAPI 3
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),

    path("api/v1/", include('authentication.urls')),
    path("api/v1/", include('hemocentros.urls')),
    path("api/v1/", include('doadores.urls')),
    path("api/v1/", include('coletas.urls')),
    path("api/v1/", include('logs.urls')),
 
]
