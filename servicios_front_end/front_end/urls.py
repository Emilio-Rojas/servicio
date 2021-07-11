from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from .views import *


urlpatterns = [
  path('', list_alumnos, name='list_alumnos'),

  path('alumno/', include([
    path('<int:id>/', list_alumno_by_id, name='list_alumno_by_id'),
    path('agregar/', agregar_alumno, name='agregar_alumno'),
    #path('editar/<int:id>/', editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', eliminar_alumno, name='eliminar_alumno'),
  ])),

  path('finanzas/', include([
    path('', list_finanzas, name='list_finanzas'),
    path('<int:id>/', list_finanzas_by_id, name='list_finanzas_by_id'),
    path('agregar/', agregar_finanzas, name='agregar_finanzas'),
    #path('editar/<int:id>/', editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', eliminar_finanzas, name='eliminar_finanzas'),
  ])),

  path('toma-ramos/', include([
    path('', list_finanzas, name='list_finanzas'),
    path('<int:id>/', list_finanzas_by_id, name='list_finanzas_by_id'),
    path('agregar/', agregar_finanzas, name='agregar_finanzas'),
    #path('editar/<int:id>/', editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', eliminar_finanzas, name='eliminar_finanzas'),
  ])),

  path('reserva-libro/', include([
    path('', list_finanzas, name='list_finanzas'),
    path('<int:id>/', list_finanzas_by_id, name='list_finanzas_by_id'),
    path('agregar/', agregar_finanzas, name='agregar_finanzas'),
    #path('editar/<int:id>/', editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', eliminar_finanzas, name='eliminar_finanzas'),
  ])),
  


]