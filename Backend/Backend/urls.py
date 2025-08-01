from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ⬇️ Önce schema_view tanımlanmalı
schema_view = get_schema_view(
   openapi.Info(
      title="Restoran ERP API",
      default_version='v1',
      description="Sipariş, menü ve masa yönetimi API dökümantasyonu",
      contact=openapi.Contact(email="destek@restoran.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('table/', include('table.urls')),
    path('order/', include('order.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
