from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from serviciosws.persistence.models import TomaRamos
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework import status

scheme_add_toma_ramos = { 
    "type" : "object",
    "properties": {
        "id_alumno":{"type" : "int"},
        "id_ramo":{"type" : "int"},
        "seccion":{"type" : "string"},
    },
    "required": ["id_alumno", "id_ramo", "seccion"],
    "propertiesOrder": ["id_alumno", "id_ramo", "seccion"],
}

@api_view(['GET', 'POST'])
def toma_ramos(request):
    if request.method == 'GET':
        return find_all(request)
    if request.method == 'POST':
        return add_toma_ramos(request)

def add_toma_ramos(request):
    print('method add_toma_ramos')
    toma_ramos = json.loads(request.body.decode('utf-8'))
    print('toma_ramos -> {0}'.format(toma_ramos))
    try:
        validate(instance=toma_ramos, schema=scheme_add_toma_ramos)
        new_toma_ramos = TomaRamos(
                            id_alumno = toma_ramos.get('id_alumno'),
                            id_ramo = toma_ramos.get('id_ramo'),
                            seccion = toma_ramos.get('seccion'),
                        )
        new_toma_ramos.save() 
        return JsonResponse(new_toma_ramos.json(),  content_type="application/json", 
                        json_dumps_params={'ensure_ascii': False})
    except ValidationError as err:
        print(err)        
        response = HttpResponse('Error en esquema json, estructura no valida.\n {0}'.format(err.message)) 
        response.status_code = status.HTTP_409_CONFLICT
        return response        
    except Exception as err:
        print(err)
        response = HttpResponse('Error al crear el TomaRamos en el sistema')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR    
        return response

def find_all(request):
    print('method find_all')
    try:
        toma_ramos = TomaRamos.objects.all().order_by('id').values()
        return JsonResponse(list(toma_ramos), safe=False,
            content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al buscar los TomaRamos en la base de datos')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

@api_view(['GET', 'DELETE'])
def toma_ramos_by_id(request, id):
    if request.method == 'GET':
        return find_by_id(request, id)
    if request.method == 'DELETE':
        return delete_by_id(request, id)

def find_by_id(request, id):
    print('find_by_id')
    try:
        toma_ramos = TomaRamos.objects.get(id = id)
        return JsonResponse(toma_ramos.json(), content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except TomaRamos.DoesNotExist as err: 
        print(err)
        response = HttpResponse('TomaRamos no encontrado. Error al buscar por id -> {0}'.format(id))
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
        toma_ramos = TomaRamos.objects.get(id = id)
        toma_ramos.delete()
        response = HttpResponse('TomaRamos eliminado -> {0}'.format(id))
        response.status_code = status.HTTP_200_OK
        return response
    except TomaRamos.DoesNotExist as err: 
        print(err)
        response = HttpResponse('TomaRamos no encontrado. Error al borrando por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Error al borrar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response    