from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# ADD SWAGGER
schema_view = get_schema_view(
   openapi.Info(
      title="Backend DRF Assignment",
      default_version='v1',
      description="Developed By Abdelrahman Ibrahem Abdelkader",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path('admin/', admin.site.urls),
   path('auth/', include('rest_framework.urls')),
   path('auth/', include('dj_rest_auth.urls')),
   path('auth/register/', include('dj_rest_auth.registration.urls')),
   path('api/tasks/', include('tasks.urls')),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
