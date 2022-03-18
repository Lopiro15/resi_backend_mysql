"""Resi_mysql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import routers

from client.urls import router as clientrouter
from proprio.urls import router as propriorouter
from login import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.registry.extend(clientrouter.registry)

routerpro = routers.DefaultRouter()
routerpro.registry.extend(propriorouter.registry)

schema_view = get_schema_view(
   openapi.Info(
      title="Resi API",
      default_version='v1',
      description="ceci est la documentation du backend du projet RESI",
      contact=openapi.Contact(email="lopezkouakou15@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=False,
   permission_classes=[permissions.AllowAny],
)

#function test pour verifier que je peux capturer une erreur en production
def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', views.index),
    path('changepassword/client/', views.client_change_password),
    path('changepassword/proprio/', views.proprio_change_password),
    path('confirmation-commande/', views.confirmation_de_la_commande),
    path('admin/', admin.site.urls),
    path('client/', include(router.urls)),
    path('proprio/', include(routerpro.urls)),
    path('login/client/', views.client_login),
    path('login/proprio/', views.proprio_login),
    path('moyenneresi/', views.resi_note),
    path('historiquemoyenresi/', views.historique_annonce),
    path('disponibiliteresi/', views.disponibilite_resi),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


