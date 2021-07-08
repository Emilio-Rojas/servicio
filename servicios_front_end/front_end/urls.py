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

  path('arancel/', include([
    path('<int:id>/', list_alumno_by_id, name='list_alumno_by_id'),
    path('agregar/', agregar_alumno, name='agregar_alumno'),
    #path('editar/<int:id>/', editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', eliminar_alumno, name='eliminar_alumno'),
  ])),

  path('pagos/', include([
    path('<int:id>/', list_alumno_by_id, name='list_alumno_by_id'),
    path('agregar/', agregar_alumno, name='agregar_alumno'),
    #path('editar/<int:id>/', editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', eliminar_alumno, name='eliminar_alumno'),
  ])),
  


]