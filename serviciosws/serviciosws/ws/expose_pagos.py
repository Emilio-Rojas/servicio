from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from serviciosws.persistence.models import Pagos
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework import status

scheme_add_pagos = { 
    "type" : "object",
    "properties": {
        "id_alumno":{"type" : "id_alumno"},
        "id_aranceles":{"type" : "id_aranceles"},
        "tipo_cuota":{"type" : "string"},
        "num_cuota":{"type" : "int"},
        "pagada":{"type" : "boolean"},
        "fecha_vencimiento":{"type" : "date"},
    },
    "required": ["id_alumno", "id_aranceles", "tipo_cuota", "num_cuota", "pagada", "fecha_vencimiento"],
    "propertiesOrder": ["id_alumno", "id_aranceles", "tipo_cuota", "num_cuota", "pagada", "fecha_vencimiento"],
}


@api_view(['GET', 'POST'])
def pagos(request):
    if request.method == 'GET':
        return find_all(request)
    if request.method == 'POST':
        return add_pagos(request)

def add_pagos(request):
    print('method add_pagos')
    pagos = json.loads(request.body.decode('utf-8'))
    print('pagos -> {0}'.format(pagos))
    try:
        validate(instance=pagos, schema=scheme_add_pagos)
        new_pagos = Pagos(
                            id_alumno = pagos.get('id_alumno'),
                            id_aranceles = pagos.get('id_aranceles'),
                            tipo_cuota = pagos.get('tipo_cuota'),
                            num_cuota = pagos.get('num_cuota'),
                            pagada = pagos.get('pagada'),
                            fecha_vencimiento = pagos.get('fecha_vencimiento'),
                        )
        new_pagos.save() 
        return JsonResponse(new_pagos.json(),  content_type="application/json", 
                        json_dumps_params={'ensure_ascii': False})
    except ValidationError as err:
        print(err)        
        response = HttpResponse('Error en esquema json, estructura no valida.\n {0}'.format(err.message)) 
        response.status_code = status.HTTP_409_CONFLICT
        return response        
    except Exception as err:
        print(err)
        response = HttpResponse('Error al crear el pagose en el sistema')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR    
        return response

def find_all(request):
    print('method find_all')
    try:
        pagoss = Pagos.objects.all().order_by('id').values()
        return JsonResponse(list(pagoss), safe=False,
            content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al buscar los pagoses en la base de datos')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

@api_view(['GET', 'DELETE'])
def pagos_by_id(request, id):
    if request.method == 'GET':
        return find_by_id(request, id)
    if request.method == 'DELETE':
        return delete_by_id(request, id)

def find_by_id(request, id):
    print('find_by_id')
    try:
        pagos = Pagos.objects.get(id = id)
        return JsonResponse(pagos.json(), content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except Pagos.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Pagos no encontrado. Error al buscar por id -> {0}'.format(id))
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
        pagos = Pagos.objects.get(id = id)
        pagos.delete()
        response = HttpResponse('Pagos eliminado -> {0}'.format(id))
        response.status_code = status.HTTP_200_OK
        return response
    except Pagos.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Pagos no encontrado. Error al borrando por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Error al borrar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response    