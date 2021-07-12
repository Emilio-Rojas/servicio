from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from serviciosws.persistence.models import ReservaLibro, Libro, Alumno
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework import status

scheme_add_reserva_libros = { 
    "type" : "object",
    "properties": {
        "id_alumno":{"type" : "integer"},
        "id_libro":{"type" : "integer"},
    },
    "required": ["id_alumno", "id_libro"],
    "propertiesOrder": ["id_alumno", "id_libro"],
}

@api_view(['GET', 'POST'])
def reserva_libro(request):
    if request.method == 'GET':
        return find_all(request)
    if request.method == 'POST':
        return add_reserva_libros(request)

def add_reserva_libros(request):
    print('method add_reserva_libros')
    reserva_libros = json.loads(request.body.decode('utf-8'))
    print('reserva_libros -> {0}'.format(reserva_libros))
    try:
        validate(instance=reserva_libros, schema=scheme_add_reserva_libros)
        new_reserva_libros = ReservaLibro(
                            id_alumno = Alumno.objects.get(id=reserva_libros.get('id_alumno')),
                            id_libro = Libro.objects.get(id=reserva_libros.get('id_libro')),
                        )
        new_reserva_libros.save() 
        return JsonResponse(new_reserva_libros.json(),  content_type="application/json", 
                        json_dumps_params={'ensure_ascii': False})
    except ValidationError as err:
        print(err)        
        response = HttpResponse('Error en esquema json, estructura no valida.\n {0}'.format(err.message)) 
        response.status_code = status.HTTP_409_CONFLICT
        return response        
    except Exception as err:
        print(err)
        response = HttpResponse('Error al crear el Reserva Libro en el sistema')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR    
        return response

def find_all(request):
    print('method find_all')
    try:
        reserva_libros = ReservaLibro.objects.all().order_by('id').values()
        return JsonResponse(list(reserva_libros), safe=False,
            content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al buscar los ReservaLibro en la base de datos')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

@api_view(['GET', 'DELETE'])
def reserva_libro_by_id(request, id):
    if request.method == 'GET':
        return find_by_id(request, id)
    if request.method == 'DELETE':
        return delete_by_id(request, id)

def find_by_id(request, id):
    print('find_by_id')
    try:
        reserva_libros = ReservaLibro.objects.get(id = id)
        return JsonResponse(reserva_libros.json(), content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except ReservaLibro.DoesNotExist as err: 
        print(err)
        response = HttpResponse('ReservaLibro no encontrado. Error al buscar por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Problemas en la base de datos. Error al buscar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

def delete_by_id(request, id):
    print('find_by_id')
    try:
        reserva_libros = ReservaLibro.objects.get(id = id)
        reserva_libros.delete()
        response = HttpResponse('ReservaLibro eliminado -> {0}'.format(id))
        response.status_code = status.HTTP_200_OK
        return response
    except ReservaLibro.DoesNotExist as err: 
        print(err)
        response = HttpResponse('ReservaLibro no encontrado. Error al borrando por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Error al borrar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response



@api_view(['GET', 'POST'])
def libros(request):
    if request.method == 'GET':
        return find_all_libros(request)

def find_all_libros(request):
    print('method find_all_libros')
    try:
        libros = Libro.objects.all().order_by('id').values()
        return JsonResponse(list(libros), safe=False,
            content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al buscar los Libro en la base de datos')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response