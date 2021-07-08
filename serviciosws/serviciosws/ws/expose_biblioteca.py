from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from serviciosws.persistence.models import Biblioteca
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework import status

scheme_add_biblioteca = { 
    "type" : "object",
    "properties": {
        "nombre":{"type" : "string"},
        "direccion":{"type" : "string"},
        "comuna":{"type" : "string"},
    },
    "required": ["nombre", "direccion", "comuna"],
    "propertiesOrder": ["nombre", "direccion", "comuna"],
}


@api_view(['GET', 'POST'])
def biblioteca(request):
    if request.method == 'GET':
        return find_all(request)
    if request.method == 'POST':
        return add_biblioteca(request)

def add_biblioteca(request):
    print('method add_biblioteca')
    biblioteca = json.loads(request.body.decode('utf-8'))
    print('biblioteca -> {0}'.format(biblioteca))
    try:
        validate(instance=biblioteca, schema=scheme_add_biblioteca)
        new_biblioteca = Biblioteca(
                            nombre = biblioteca.get('nombre'),
                            direccion = biblioteca.get('direccion'),
                            comuna = biblioteca.get('comuna'),
                        )
        new_biblioteca.save() 
        return JsonResponse(new_biblioteca.json(),  content_type="application/json", 
                        json_dumps_params={'ensure_ascii': False})
    except ValidationError as err:
        print(err)        
        response = HttpResponse('Error en esquema json, estructura no valida.\n {0}'.format(err.message)) 
        response.status_code = status.HTTP_409_CONFLICT
        return response        
    except Exception as err:
        print(err)
        response = HttpResponse('Error al crear el bibliotecae en el sistema')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR    
        return response

def find_all(request):
    print('method find_all')
    try:
        bibliotecas = Biblioteca.objects.all().order_by('id').values()
        return JsonResponse(list(bibliotecas), safe=False,
            content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al buscar los bibliotecaes en la base de datos')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

@api_view(['GET', 'DELETE'])
def biblioteca_by_id(request, id):
    if request.method == 'GET':
        return find_by_id(request, id)
    if request.method == 'DELETE':
        return delete_by_id(request, id)

def find_by_id(request, id):
    print('find_by_id')
    try:
        biblioteca = Biblioteca.objects.get(id = id)
        return JsonResponse(biblioteca.json(), content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except Biblioteca.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Biblioteca no encontrado. Error al buscar por id -> {0}'.format(id))
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
        biblioteca = Biblioteca.objects.get(id = id)
        biblioteca.delete()
        response = HttpResponse('Biblioteca eliminado -> {0}'.format(id))
        response.status_code = status.HTTP_200_OK
        return response
    except Biblioteca.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Biblioteca no encontrado. Error al borrando por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Error al borrar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response    