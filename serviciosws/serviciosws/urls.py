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
from serviciosws.ws.expose_finanzas import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/alumno/', alumno, name='alumno'),  
    path('api/v1/alumno/<int:id>/', alumno_by_id, name='alumno_by_id'),

    path('api/v1/toma-ramos/', toma_ramos, name='toma-ramos'),
    path('api/v1/toma-ramos/<int:id>/', toma_ramos_by_id, name='toma_ramos_by_id'), 

    path('api/v1/finanzas/', finanzas, name='finanzas'),
    path('api/v1/finanzas/<int:id>/', finanzas_by_id, name='finanzas_by_id'), 

    path('api/v1/reserva-libro/', reserva_libro, name='reserva_libro'),
    path('api/v1/reserva-libro/<int:id>/', reserva_libro_by_id, name='reserva_libro_by_id'), 
]
