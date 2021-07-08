"""serviciosws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from serviciosws.ws.expose_alumno import *
from serviciosws.ws.expose_arancel import *
from serviciosws.ws.expose_biblioteca import *
from serviciosws.ws.expose_libro import *
from serviciosws.ws.expose_pagos import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/estudiante/', alumno, name='alumno'),  
    path('api/v1/estudiante/<int:id>/', alumno_by_id, name='alumno_by_id'),

    path('api/v1/arancel/', arancel, name='arancel'),
    path('api/v1/arancel/<int:id>/', arancel_by_id, name='arancel_by_id'), 

    path('api/v1/biblioteca/', biblioteca, name='biblioteca'),
    path('api/v1/biblioteca/<int:id>/', biblioteca_by_id, name='biblioteca_by_id'),

    path('api/v1/libro/', libro, name='libro'),
    path('api/v1/libro/<int:id>/', libro_by_id, name='libro_by_id'), 

    path('api/v1/pagos/', pagos, name='pagos'),
    path('api/v1/pagos/<int:id>/', pagos_by_id, name='pagos_by_id'), 
]
