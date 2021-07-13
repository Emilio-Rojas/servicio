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
    path('agregar/', agregar_finanzas, name='agregar_finanzas'),
    path('pagar/<int:id>/', pagar_finanza_by_id, name='pagar_finanza_by_id'),
    path('eliminar/<int:id>/', eliminar_finanzas, name='eliminar_finanzas'),
  ])),

  path('toma-ramos/', include([
    path('', list_toma_ramos, name='list_toma_ramos'),
    path('<int:id>/', list_toma_ramos_by_id, name='list_toma_ramos_by_id'),
    path('agregar/', agregar_tomar_ramo, name='agregar_tomar_ramo'),
    #path('editar/<int:id>/', editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', eliminar_toma_ramo, name='eliminar_toma_ramo'),
  ])),

  path('reserva-libro/', include([
    path('', list_reserva_libros, name='list_reserva_libros'),
    path('<int:id>/', list_reserva_libros_by_id, name='list_reserva_libros_by_id'),
    path('agregar/', agregar_reserva_libro, name='agregar_reserva_libro'),
    #path('editar/<int:id>/', editar_alumno, name='editar_alumno'),
    path('eliminar/<int:id>/', eliminar_reserva_libro, name='eliminar_reserva_libro'),
  ])),

  
  path('send-email/', send_email, name='send_email'),
  path('estado-email/<str:estado>/', estado_mail, name='estado_mail'),
  


]