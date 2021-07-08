from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from serviciosws.persistence.models import Libro
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework import status

scheme_add_libro = { 
    "type" : "object",
    "properties": {
        "nombre":{"type" : "string"},
        "autor":{"type" : "string"},
        "en_biblioteca":{"type" : "string"},
    },
    "required": ["nombre", "autor", "en_biblioteca"],
    "propertiesOrder": ["nombre", "autor", "en_biblioteca"],
}


@api_view(['GET', 'POST'])
def libro(request):
    if request.method == 'GET':
        return find_all(request)
    if request.method == 'POST':
        return add_libro(request)

def add_libro(request):
    print('method add_libro')
    libro = json.loads(request.body.decode('utf-8'))
    print('libro -> {0}'.format(libro))
    try:
        validate(instance=libro, schema=scheme_add_libro)
        new_libro = Libro(
                            nombre = libro.get('nombre'),
                            autor = libro.get('autor'),
                            en_biblioteca = libro.get('en_biblioteca'),
                        )
        new_libro.save() 
        return JsonResponse(new_libro.json(),  content_type="application/json", 
                        json_dumps_params={'ensure_ascii': False})
    except ValidationError as err:
        print(err)        
        response = HttpResponse('Error en esquema json, estructura no valida.\n {0}'.format(err.message)) 
        response.status_code = status.HTTP_409_CONFLICT
        return response        
    except Exception as err:
        print(err)
        response = HttpResponse('Error al crear el libroe en el sistema')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR    
        return response

def find_all(request):
    print('method find_all')
    try:
        libros = Libro.objects.all().order_by('id').values()
        return JsonResponse(list(libros), safe=False,
            content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al buscar los libroes en la base de datos')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

@api_view(['GET', 'DELETE'])
def libro_by_id(request, id):
    if request.method == 'GET':
        return find_by_id(request, id)
    if request.method == 'DELETE':
        return delete_by_id(request, id)

def find_by_id(request, id):
    print('find_by_id')
    try:
        libro = Libro.objects.get(id = id)
        return JsonResponse(libro.json(), content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except Libro.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Libro no encontrado. Error al buscar por id -> {0}'.format(id))
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
        libro = Libro.objects.get(id = id)
        libro.delete()
        response = HttpResponse('Libro eliminado -> {0}'.format(id))
        response.status_code = status.HTTP_200_OK
        return response
    except Libro.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Libro no encontrado. Error al borrando por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Error al borrar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response    