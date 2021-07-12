from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from serviciosws.persistence.models import Alumno, Finanzas
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework import status


@api_view(['GET'])
def morosidad_by_rut(request, rut):
    if request.method == 'GET':
        return find_by_rut(request, rut)

def find_by_rut(request, rut):
    print('find_by_rut')
    print(rut)
    try:
        alumno = Alumno.objects.get(rut= rut)
        finanzas = Finanzas.objects.filter(id_alumno = alumno.id)
        regular = True
        for fin in finanzas:
            print(fin)
            if (fin.pagada == False):
                regular = False

        response = {
            "regular": regular,
            "id_alumno": alumno.id,
            "rut": alumno.rut
        }
        print(response)
        return JsonResponse(response, content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except Finanzas.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Finanzas no encontrado. Error al buscar por rut -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Problemas en la base de datos. Error al buscar por rut -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response