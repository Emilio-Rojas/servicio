from django.shortcuts import render, redirect
from front_end.forms import *
import sys
import requests

# Create your views here.

def list_alumnos(request):
    print('find_all')
    url = 'http://127.0.0.1:9000/api/v1/alumno/'
    try:
        headers ={'Authorization' : 'Token'}
        response = requests.get(url, headers=headers)
        print('status_code: {0}'.format(response.status_code))
        alumnos = response.json()
        print (alumnos)
        return render(request, 'index.html', {'alumnos': alumnos})
    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e ))

def list_alumno_by_id(request, id):
    print('find_by_id')
    url = 'http://127.0.0.1:9000/api/v1/alumno/{0}'.format(id)
    try:
        response = requests.get(url)
        print('status_code: {0}'.format(response.status_code))
        status = response.status_code

        if status == 200:
            alumno = response.json()          

    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 

def agregar_alumno(request):
    print('add_client')
    url = 'http://127.0.0.1:9000/api/v1/alumno/'
    if request.method == "POST":
        try:
            alumno_json = {
                'rut': request.POST['rut'],
                'nombres': request.POST['nombres'],
                'apellido_paterno': request.POST['apellido_paterno'],
                'apellido_materno': request.POST['apellido_materno'], 
                'email': request.POST['email'],
                'direccion': request.POST['direccion'],
                'comuna': request.POST['comuna'],
                'matriculado': True if request.POST['matriculado'] == '1' else False ,
                'morocidad': True if request.POST['morocidad'] == '1' else False  ,       
                'is_regular': True if request.POST['is_regular'] == '1' else False ,   
                'telefono': request.POST['telefono'],                                                       
            }
            response = requests.post(url, json=alumno_json)
            print('status_code: {0}'.format(response.status_code))
            alumno = response.json()
            return redirect('/')
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        form = AlumnoForms()
        return render(request, 'alumno/agregar_alumno.html', {'form': form})

    

def editar_alumno(request, id):
    print('find_all')
    url = 'http://127.0.0.1:9000/api/v1/alumno/'
    try:
        headers ={'Authorization' : 'Token'}
        response = requests.get(url, headers=headers)
        print('status_code: {0}'.format(response.status_code))
        alumnos = response.json()
        print (alumnos)
        return render(request, 'index.html', {'alumnos': alumnos})
    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e ))

def eliminar_alumno(request, id):
    print('delete_by_id')
    url = 'http://127.0.0.1:9000/api/v1/alumno/{0}'.format(id)
    print(request.method)
    if request.method == 'POST':
        try:
            response = requests.delete(url)
            print('id: {0}'.format(response.status_code))
            print('messsage: {0}'.format(response.text))
            return redirect('/')     
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        return render(request, 'alumno/eliminar_alumno.html')
