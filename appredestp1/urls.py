from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.http import HttpResponse

from django.contrib.auth import views as auth_views

from . import views



# Vista de prueba para raíz
def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>API de Redes - TP1</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 2rem; }
            h1 { color: #333; }
            a { color: #007bff; text-decoration: none; margin-right: 1rem; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Bienvenido a la API</h1>
        <p>Endpoints principales:</p>
        <ul>
            <li><a href="/clientes/">Clientes</a></li>
            <li><a href="/facturas/">Facturas</a></li>
            <li><a href="/productos/">Productos</a></li>
            <li><a href="/proveedores/">Proveedores</a></li>
        </ul>

        <h2>Documentación API:</h2>
        <div style="margin-top: 1rem;">
            <a href="/swagger/" style="background: #85ea2d; color: white; padding: 0.5rem 1rem; border-radius: 4px;">
                Swagger UI
            </a>
            <a href="/redoc/" style="background: #2d6dea; color: white; padding: 0.5rem 1rem; border-radius: 4px;">
                ReDoc
            </a>
        </div>
    </body>
    </html>
    """, content_type="text/html")

schema_view = get_schema_view(
    openapi.Info(
        title="API de Redes - TP1",
        default_version='v1',
        description="Documentación de la API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    urlconf='appredestp1.urls',
)

urlpatterns = [
    path('', home, name='home'),  # Vista simple de prueba
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('facturas/', include('facturas.urls')),
    path('clientes/', include('clientes.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('productos/', include('productos.urls')),
    path('autenticarse', views.autenticarse, name='autenticarse'),
    path('registrarse', views.registrarse, name='registrarse'),
    
]