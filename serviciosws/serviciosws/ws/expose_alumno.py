from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from serviciosws.persistence.models import Alumno
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from rest_framework import status

scheme_add_alumno = { 
    "type" : "object",
    "properties": {
        "rut":{"type" : "string"},
        "nombres":{"type" : "string"},
        "apellidos":{"type" : "string"},
        "email":{"type" : "string"},
        "direccion":{"type" : "string"},
        "comuna":{"type" : "string"},
        "carrera":{"type" : "string"},
    },
    "required": ["rut", "nombres", "apellidos", "email", "direccion", "comuna", "carrera"],
    "propertiesOrder": ["rut", "nombres", "apellidos", "email", "direccion", "comuna", "carrera"],
}


@api_view(['GET', 'POST'])
def alumno(request):
    print('method alumno')
    if request.method == 'GET':
        return find_all(request)
    if request.method == 'POST':
        return add_alumno(request)

def add_alumno(request):
    print('method add_alumno')
    alumno = json.loads(request.body.decode('utf-8'))
    print('alumno -> {0}'.format(alumno))
    try:
        validate(instance=alumno, schema=scheme_add_alumno)
        new_alumno = Alumno(
            rut = alumno.get('rut'),
            nombres = alumno.get('nombres'),
            apellido_paterno = alumno.get('apellido_paterno'),
            apellido_materno = alumno.get('apellido_materno'),
            email = alumno.get('email'),
            direccion = alumno.get('direccion'),
            comuna = alumno.get('comuna'),
            matriculado = alumno.get('matriculado'),
            morocidad = alumno.get('morocidad'),
            is_regular = alumno.get('is_regular'),
            telefono = alumno.get('telefono'),
        )
        new_alumno.save()
        return JsonResponse(new_alumno.json(),  content_type="application/json", 
                        json_dumps_params={'ensure_ascii': False})
    except ValidationError as err:
        print(err)        
        response = HttpResponse('Error en esquema json, estructura no valida.\n {0}'.format(err.message)) 
        response.status_code = status.HTTP_409_CONFLICT
        return response        
    except Exception as err:
        print(err)
        response = HttpResponse('Error al crear el alumno en el sistema')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR    
        return response

def find_all(request):
    print('method find_all')
    try:
        alumnos = Alumno.objects.all().order_by('id').values()
        return JsonResponse(list(alumnos), safe=False,
            content_type="application/json", json_dumps_params={'ensure_ascii': False})
    except Exception as err:
        print(err)
        response = HttpResponse('Error al buscar los alumnoes en la base de datos')
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response

@api_view(['GET', 'DELETE'])
def alumno_by_id(request, id):
    if request.method == 'GET':
        return find_by_id(request, id)
    if request.method == 'DELETE':
        return delete_by_id(request, id)

def find_by_id(request, id):
    print('find_by_id')
    try:
        alumno = Alumno.objects.get(id = id)
        return JsonResponse(alumno.json(), content_type="application/json", 
                json_dumps_params={'ensure_ascii': False})
    except Alumno.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Alumno no encontrado. Error al buscar por id -> {0}'.format(id))
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
        alumno = Alumno.objects.get(id = id)
        alumno.delete()
        response = HttpResponse('Alumno eliminado -> {0}'.format(id))
        response.status_code = status.HTTP_200_OK
        return response
    except Alumno.DoesNotExist as err: 
        print(err)
        response = HttpResponse('Alumno no encontrado. Error al borrando por id -> {0}'.format(id))
        response.status_code = status.HTTP_404_NOT_FOUND
        return response
    except Exception as err:
        print(err)
        response = HttpResponse('Error al borrar por id -> {0}'.format(id))
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response    