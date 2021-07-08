from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from serviciosws.persistence.models import Aranceles
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework import status

scheme_add_arancel = { 
    "type" : "object",
    "properties": {
        "sede": {"type" : "string"},
        "direccion": {"type" : "string"},
        "comuna": {"type" : "string"},
    },
    "required": ["sede", "direccion", "comuna"],
    "propertiesOrder": ["sede", "direccion", "comuna"],
}


@api_view(['GET', 'POST'])
def arancel(request):
    if request.method == 'GET':
        return find_all(request)
    if request.method == 'POST':
        return add_arancel(request)

def add_arancel(request):
    print('method add_arancel')
    arancel = json.loads(request.body.decode('utf-8'))
    print('arancel -> {0}'.format(arancel))
    try:
        validate(instance=arancel, schema=scheme_add_arancel)
        new_arancel = Aranceles(
                            sede = arancel.get('sede'),
                            direccion = arancel.get('direccion'),
                            comuna = arancel.get('comuna'),
                        )
        new_arancel.save() 
        return JsonResponse(new_arancel.json(),  content_type="application/json", 
                        json_dumps_params={'ensure_ascii': False})
    except ValidationError as err:
        print(err)        
        response = HttpResponse('Error en esquema json, estructura no valida.\n {0}'.format(err.message)) 
        response.status_code = status.HTTP_409_CONFLICT
        return response        
    except Exception as err:
        print(err)
        response = HttpResponse('Error al crear el arancele en el sistema')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR    
        return response

def find_all(request):
    print('method find_all')
    try:
        arancels = Aranceles.objects.all().order_by('id').values()
        return JsonResponse(list(arancels), safe=False,
            content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al buscar los aranceles en la base de datos')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

@api_view(['GET', 'DELETE'])
def arancel_by_id(request, id):
    if request.method == 'GET':
        return find_by_id(request, id)
    if request.method == 'DELETE':
        return delete_by_id(request, id)

def find_by_id(request, id):
    print('find_by_id')
    try:
        arancel = Aranceles.objects.get(id = id)
        return JsonResponse(arancel.json(), content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except Aranceles.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Aranceles no encontrado. Error al buscar por id -> {0}'.format(id))
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
        arancel = Aranceles.objects.get(id = id)
        arancel.delete()
        response = HttpResponse('Aranceles eliminado -> {0}'.format(id))
        response.status_code = status.HTTP_200_OK
        return response
    except Aranceles.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Aranceles no encontrado. Error al borrando por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Error al borrar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response    