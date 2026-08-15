
from django.contrib import admin

from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API de Mensajes",
        default_version='v1',
        description="Ejemplo de Swagger con drf_yasg sin base de datos",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
  
    path('api/', include('productos.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),

]
