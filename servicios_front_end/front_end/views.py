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



# Para los servicios de aranceles
def list_aranceles(request):
    print('find_all')
    url = 'http://127.0.0.1:9000/api/v1/aranceles/'
    try:
        headers ={'Authorization' : 'Token'}
        response = requests.get(url, headers=headers)
        print('status_code: {0}'.format(response.status_code))
        aranceles = response.json()
        print (aranceles)
        return render(request, 'aranceles/listar_aranceles.html', {'aranceles': aranceles})
    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e ))

def list_aranceles_by_id(request, id):
    print('find_by_id')
    url = 'http://127.0.0.1:9000/api/v1/aranceles/{0}'.format(id)
    try:
        response = requests.get(url)
        print('status_code: {0}'.format(response.status_code))
        status = response.status_code

        if status == 200:
            alumno = response.json()          

    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 

def agregar_aranceles(request):
    print('add_client')
    url = 'http://127.0.0.1:9000/api/v1/aranceles/'
    if request.method == "POST":
        try:
            aranceles_json = {
                'sede': request.POST['sede'],
                'direccion': request.POST['direccion'],
                'comuna': request.POST['comuna'],                                                    
            }
            response = requests.post(url, json=aranceles_json)
            print('status_code: {0}'.format(response.status_code))
            aranceles = response.json()
            return redirect('/aranceles/')
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        form = ArancelesForms()
        return render(request, 'aranceles/agregar_aranceles.html', {'form': form})


def eliminar_aranceles(request, id):
    print('delete_by_id')
    url = 'http://127.0.0.1:9000/api/v1/aranceles/{0}'.format(id)
    print(request.method)
    if request.method == 'POST':
        try:
            response = requests.delete(url)
            print('id: {0}'.format(response.status_code))
            print('messsage: {0}'.format(response.text))
            return redirect('/aranceles/')     
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        return render(request, 'aranceles/eliminar_aranceles.html')


# Para los servicios de finanzas
def list_finanzas(request):
    print('find_all')
    url = 'http://127.0.0.1:9000/api/v1/finanzas/'
    try:
        headers ={'Authorization' : 'Token'}
        response = requests.get(url, headers=headers)
        print('status_code: {0}'.format(response.status_code))
        finanzas = response.json()
        print (finanzas)
        return render(request, 'finanzas/listar_finanzas.html', {'finanzas': finanzas})
    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e ))

def list_finanzas_by_id(request, id):
    print('find_by_id')
    url = 'http://127.0.0.1:9000/api/v1/finanzas/{0}'.format(id)
    try:
        response = requests.get(url)
        print('status_code: {0}'.format(response.status_code))
        status = response.status_code

        if status == 200:
            finanzas = response.json()          

    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 

def agregar_finanzas(request):
    print('add_client')
    url = 'http://127.0.0.1:9000/api/v1/finanzas/'
    if request.method == "POST":
        try:
            print("Acaaa")
            print(request.POST['tipo_cuota'])
            finanzas_json = {
                'id_alumno': request.POST['id_alumno'],
                'id_aranceles': request.POST['id_aranceles'],
                'tipo_cuota': request.POST['tipo_cuota'],  
                'num_cuota': request.POST['num_cuota'],  
                'pagada': True if request.POST['pagada'] == '1' else False,      
                'fecha_vencimiento': request.POST['fecha_vencimiento'],                                                
            }
            print (finanzas_json)
            response = requests.post(url, json=finanzas_json)
            print('status_code: {0}'.format(response.status_code))
            finanzas = response.json()
            return redirect('/finanzas/')
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        form = FinanzasForms()
        return render(request, 'finanzas/agregar_finanzas.html', {'form': form})


def eliminar_finanzas(request, id):
    print('delete_by_id')
    url = 'http://127.0.0.1:9000/api/v1/finanzas/{0}'.format(id)
    print(request.method)
    if request.method == 'POST':
        try:
            response = requests.delete(url)
            print('id: {0}'.format(response.status_code))
            print('messsage: {0}'.format(response.text))
            return redirect('/finanzas/')     
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        return render(request, 'finanzas/eliminar_finanzas.html')