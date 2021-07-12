from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from serviciosws.persistence.models import Finanzas, Alumno, TipoCuota
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework import status

scheme_add_finanzas = { 
    "type" : "object",
    "properties": {
        "id_alumno":{"type" : "integer"},
        "id_tipo_cuota":{"type" : "integer"},
        "num_cuota":{"type" : "integer"},
        "valor":{"type" : "integer"},
        "pagada":{"type" : "boolean"},
        "fecha_vencimiento":{"type" : "string"},
    },
    "required": ["id_alumno", "id_tipo_cuota", "num_cuota", "valor", "pagada", "fecha_vencimiento"],
    "propertiesOrder": ["id_alumno", "id_tipo_cuota", "num_cuota", "valor", "pagada", "fecha_vencimiento"],
}


@api_view(['GET', 'POST'])
def finanzas(request):
    if request.method == 'GET':
        return find_all(request)
    if request.method == 'POST':
        return add_finanzas(request)

def add_finanzas(request):
    print('method add_finanzas')
    finanzas = json.loads(request.body.decode('utf-8'))
    print('finanzas -> {0}'.format(finanzas))
    try:
        validate(instance=finanzas, schema=scheme_add_finanzas)
        new_finanzas = Finanzas(
                            id_alumno = Alumno.objects.get(id=finanzas.get('id_alumno')),
                            id_tipo_cuota = TipoCuota.objects.get(id=finanzas.get('id_tipo_cuota')),
                            num_cuota = finanzas.get('num_cuota'),
                            valor = finanzas.get('valor'),
                            pagada = finanzas.get('pagada'),
                            fecha_vencimiento = finanzas.get('fecha_vencimiento'),
                        )
        new_finanzas.save() 
        return JsonResponse(new_finanzas.json(),  content_type="application/json", 
                        json_dumps_params={'ensure_ascii': False})
    except ValidationError as err:
        print(err)        
        response = HttpResponse('Error en esquema json, estructura no valida.\n {0}'.format(err.message)) 
        response.status_code = status.HTTP_409_CONFLICT
        return response        
    except Exception as err:
        print(err)
        response = HttpResponse('Error al crear el Finanzas en el sistema')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR    
        return response

def find_all(request):
    print('method find_all')
    try:
        finanzas = Finanzas.objects.all().order_by('id').values()
        return JsonResponse(list(finanzas), safe=False,
            content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al buscar los Finanzas en la base de datos')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

@api_view(['GET', 'DELETE'])
def finanzas_by_id(request, id):
    if request.method == 'GET':
        return find_by_id(request, id)
    if request.method == 'DELETE':
        return delete_by_id(request, id)

def find_by_id(request, id):
    print('find_by_id')
    try:
        finanzas = Finanzas.objects.get(id = id)
        return JsonResponse(finanzas.json(), content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except Finanzas.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Finanzas no encontrado. Error al buscar por id -> {0}'.format(id))
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
        finanzas = Finanzas.objects.get(id = id)
        finanzas.delete()
        response = HttpResponse('Finanzas eliminado -> {0}'.format(id))
        response.status_code = status.HTTP_200_OK
        return response
    except Finanzas.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Finanzas no encontrado. Error al borrando por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Error al borrar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response    


@api_view(['GET'])
def pagar_finanza_by_id(request, id):
    if request.method == 'GET':
        return pagar_finanza_by_id(request, id)

def pagar_finanza_by_id(request, id):
    print('pagar_finanza_by_id')
    try:
        finanzas = Finanzas.objects.get(id = id)
        print(finanzas)
        finanzas.pagada = True
        finanzas.save() 
        return JsonResponse(finanzas.json(), content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except Finanzas.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Finanzas no encontrado. Error al buscar por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Problemas en la base de datos. Error al buscar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response