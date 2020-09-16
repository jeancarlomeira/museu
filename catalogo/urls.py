"""museu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from .views import (materiais, material, colaboradores, colaborador, tipodeentrada,
                    tipodeartefato, ambientes, artistas)

app_name = 'catalogo'

urlpatterns = [
    path('artistas/', artistas, name='artistas'),
    path('ambientes/', ambientes, name='ambientes'),
    path('artefatos/', tipodeartefato, name='tipodeartefato'),
    path('entradas/', tipodeentrada, name='tipodeentrada'),
    path('colaboradores/', colaboradores, name='colaboradores'),
    path('colaborador/<slug:slug>/', colaborador, name='colaborador'),
    path('', materiais, name='materiais'),
    path('<slug:slug>/', material, name='material'),


]
