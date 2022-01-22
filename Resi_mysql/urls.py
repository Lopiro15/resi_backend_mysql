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
from django.urls import path, include

from rest_framework import routers

from client.urls import router as clientrouter
from proprio.urls import router as propriorouter
from login import views

router = routers.DefaultRouter()
router.registry.extend(clientrouter.registry)

routerpro = routers.DefaultRouter()
routerpro.registry.extend(propriorouter.registry)



urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('client/', include(router.urls)),
    path('proprio/', include(routerpro.urls)),
    path('login/client/', views.client_login),
    path('login/proprio/', views.client_login),
    path('moyenneresi/', views.resi_note),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]


