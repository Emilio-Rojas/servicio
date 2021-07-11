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
                'apellidos': request.POST['apellidos'],
                'email': request.POST['email'],
                'direccion': request.POST['direccion'],
                'comuna': request.POST['comuna'],   
                'carrera': request.POST['carrera'],                                                       
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
                'id_alumno': int(request.POST['id_alumno']),
                'id_tipo_cuota': int(request.POST['id_tipo_cuota']),
                'num_cuota': int(request.POST['num_cuota']),
                'valor': request.POST['valor'],
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


# Para los servicios de reserva de libros
def list_reserva_libros(request):
    print('find_all')
    url = 'http://127.0.0.1:9000/api/v1/reserva-libro/'
    try:
        headers ={'Authorization' : 'Token'}
        response = requests.get(url, headers=headers)
        print('status_code: {0}'.format(response.status_code))
        reserva_libros = response.json()
        print (finanzas)
        return render(request, 'reserva_libros/listar_reserva_libro.html', {'reserva_libros': reserva_libros})
    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e ))

def list_reserva_libros_by_id(request, id):
    print('find_by_id')
    url = 'http://127.0.0.1:9000/api/v1/reserva-libro/{0}'.format(id)
    try:
        response = requests.get(url)
        print('status_code: {0}'.format(response.status_code))
        status = response.status_code

        if status == 200:
            finanzas = response.json()          

    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 

def agregar_reserva_libro(request):
    print('add_client')
    url = 'http://127.0.0.1:9000/api/v1/reserva-libro/'
    if request.method == "POST":
        try:
            print("Acaaa")
            reserva_libro_json = {
                'id_alumno': int(request.POST['id_alumno']),
                'id_libro': int(request.POST['id_libro']),                                               
            }
            print (reserva_libro_json)
            response = requests.post(url, json=reserva_libro_json)
            print('status_code: {0}'.format(response.status_code))
            reserva_libros = response.json()
            return redirect('/reserva-libro/')
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        form = FinanzasForms()
        return render(request, 'reserva_libros/agregar_reserva_libro.html', {'form': form})


def eliminar_reserva_libro(request, id):
    print('delete_by_id')
    url = 'http://127.0.0.1:9000/api/v1/toma-ramos/{0}'.format(id)
    print(request.method)
    if request.method == 'POST':
        try:
            response = requests.delete(url)
            print('id: {0}'.format(response.status_code))
            print('messsage: {0}'.format(response.text))
            return redirect('/toma-ramos/')     
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        return render(request, 'reserva_libros/eliminar_reserva_libro.html')



# Para los servicios de toma de ramos
def list_toma_ramos(request):
    print('find_all')
    url = 'http://127.0.0.1:9000/api/v1/toma-ramos/'
    try:
        headers ={'Authorization' : 'Token'}
        response = requests.get(url, headers=headers)
        print('status_code: {0}'.format(response.status_code))
        toma_ramos = response.json()
        print (finanzas)
        return render(request, 'tomar_ramos/listar_tomar_ramos.html', {'toma_ramos': toma_ramos})
    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e ))

def list_toma_ramos_by_id(request, id):
    print('find_by_id')
    url = 'http://127.0.0.1:9000/api/v1/toma-ramos/{0}'.format(id)
    try:
        response = requests.get(url)
        print('status_code: {0}'.format(response.status_code))
        status = response.status_code

        if status == 200:
            finanzas = response.json()          

    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 

def agregar_tomar_ramo(request):
    print('add_client')
    url = 'http://127.0.0.1:9000/api/v1/toma-ramos/'
    if request.method == "POST":
        try:
            print("Acaaa")
            print(request.POST['tipo_cuota'])
            tomar_ramo_json = {
                'id_alumno': int(request.POST['id_alumno']),
                'id_ramo': int(request.POST['id_ramo']),
                'seccion': request.POST['seccion'],                                             
            }
            print (tomar_ramo)
            response = requests.post(url, json=tomar_ramo)
            print('status_code: {0}'.format(response.status_code))
            tomar_ramo = response.json()
            return redirect('/toma-ramos/')
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        form = FinanzasForms()
        return render(request, 'tomar_ramos/agregar_tomar_ramo.html', {'form': form})


def eliminar_toma_ramo(request, id):
    print('delete_by_id')
    url = 'http://127.0.0.1:9000/api/v1/toma-ramos/{0}'.format(id)
    print(request.method)
    if request.method == 'POST':
        try:
            response = requests.delete(url)
            print('id: {0}'.format(response.status_code))
            print('messsage: {0}'.format(response.text))
            return redirect('/toma-ramos/')     
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        return render(request, 'tomar_ramos/eliminar_tomar_ramo.html')