from django.shortcuts import render, redirect
from front_end.forms import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.http import Http404
import json
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

def pagar_finanza_by_id(request, id):
    print('find_by_id')
    url = 'http://127.0.0.1:9000/api/v1/finanzas/{0}'.format(id)
    if request.method == 'POST':
        try:
            headers ={'Authorization' : 'Token'}
            url_pagar_finanza = 'http://127.0.0.1:9000/api/v1/pagar_finanza_by_id/{0}'.format(id)
            response = requests.get(url_pagar_finanza, headers=headers)
            print('status_code: {0}'.format(response.status_code))
            finanzas = response.json()
            return redirect('/send-email/')   
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url_pagar_finanza,e )) 
    else:
        try:
            response = requests.get(url)
            print('status_code: {0}'.format(response.status_code))
            status = response.status_code

            if status == 200:
                finanzas = response.json()   
            print(finanzas)
            return render(request, 'finanzas/pagar_finanzas.html', {'finanzas': finanzas})       
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e ))

def send_email(request):
    if request.method == "POST":
        to = str(request.POST['to'])
        subject = request.POST['subject']
        contexto = { "mensaje": request.POST['contexto']}
        from_email = "kala.mail.testing@gmail.com"
        estado_email = enviar_correo(request, contexto, to, subject, from_email)
        return redirect('/estado-email/{0}/'.format(estado_email))
    else:    
        form = SendEmail()
        return render(request, 'email/body.html', {'form': form})

def estado_mail(request, estado):
    print(estado)
    return render(request, 'email/estado.html', {'estado': estado})

def enviar_correo(request,contexto,to,subject,from_email):
    try:
        template = get_template('email/plantilla.html')
        text_content = 'No responder este correo.'
        html_content = template.render(contexto)
        correos_a_usar = [to]

        msg = EmailMultiAlternatives(subject, text_content, from_email, correos_a_usar)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as identifier:
        print("Error enviando un email: {0}".format(identifier))
        raise Http404(identifier)
        return False

def agregar_finanzas(request):
    print('add_client')
    url = 'http://127.0.0.1:9000/api/v1/finanzas/'
    if request.method == "POST":
        try:
            print("Acaaa")
            print(request.POST['pagada'])
            finanzas_json = {
                'id_alumno': int(request.POST['id_alumno']),
                'id_tipo_cuota': int(request.POST['id_tipo_cuota']),
                'num_cuota': int(request.POST['num_cuota']),
                'valor': int(request.POST['valor']),
                'pagada': True if request.POST['pagada'] == "1" else False,      
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
        print (reserva_libros)
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
            reserva_libros = response.json()          

    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 

def agregar_reserva_libro(request):
    print('agregar_reserva_libro')
    url = 'http://127.0.0.1:9000/api/v1/reserva-libro/'
    url_libros = 'http://127.0.0.1:9000/api/v1/libros/'
    if request.method == "POST":
        try:
            try: 
                if (request.POST['rut']):
                    url_morosidad = 'http://127.0.0.1:9000/api/v1/morosidad/{0}'.format(request.POST['rut'])
                    response = requests.get(url_morosidad)
                    print('status_code: {0}'.format(response.status_code))
                    modulo = 'reserva_libro'
                    if response.status_code == 200:
                        value = response.json()
                        value_dumps = json.dumps(value)
                        alumno = json.loads(value_dumps)
                        print(alumno["id_alumno"])
                        regular = alumno["regular"]
                        rut = alumno["rut"]
                        id_alumno = alumno["id_alumno"]
                    return render(request, 'morosidad/regular.html', {'modulo': modulo, 'regular': regular, "rut": rut, 'id_alumno': id_alumno})
            except:
                if (request.POST['id_alumno']):
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
        form = ReservaLibroForms()
        form_morosidad = ConsultarMorosidad()
        try:
            headers ={'Authorization' : 'Token'}
            response = requests.get(url_libros, headers=headers)
            print('status_code: {0}'.format(response.status_code))
            libros = response.json()
            print (libros)
            return render(request, 'reserva_libros/agregar_reserva_libro.html', {'form': form, 'form_morosidad': form_morosidad, 'libros': libros})
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url_libros,e )) 


def eliminar_reserva_libro(request, id):
    print('delete_by_id')
    url = 'http://127.0.0.1:9000/api/v1/reserva-libro/{0}'.format(id)
    print(request.method)
    if request.method == 'POST':
        try:
            response = requests.delete(url)
            print('id: {0}'.format(response.status_code))
            print('messsage: {0}'.format(response.text))
            return redirect('/reserva-libro/')     
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
        print (toma_ramos)
        return render(request, 'toma_ramos/listar_toma_ramos.html', {'toma_ramos': toma_ramos})
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
            toma_ramos = response.json()          

    except Exception as e:
        print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 

def agregar_tomar_ramo(request):
    print('toma_ramos')
    url = 'http://127.0.0.1:9000/api/v1/toma-ramos/'
    url_ramos = 'http://127.0.0.1:9000/api/v1/ramos/'
    if request.method == "POST":
        try:
            try: 
                if (request.POST['rut']):
                    url_morosidad = 'http://127.0.0.1:9000/api/v1/morosidad/{0}'.format(request.POST['rut'])
                    response = requests.get(url_morosidad)
                    print('status_code: {0}'.format(response.status_code))
                    modulo = 'toma_ramos'
                    if response.status_code == 200:
                        value = response.json()
                        value_dumps = json.dumps(value)
                        alumno = json.loads(value_dumps)
                        regular = alumno["regular"]
                        rut = alumno["rut"]
                        id_alumno = alumno["id_alumno"]
                        return render(request, 'morosidad/regular.html', {'modulo': modulo, 'regular': regular, "rut": rut, 'id_alumno': id_alumno})
            except:
                if (request.POST['id_alumno']):
                    print("Acaaa")
                    tomar_ramo_json = {
                        'id_alumno': int(request.POST['id_alumno']),
                        'id_ramo': int(request.POST['id_ramo']),
                        'seccion': request.POST['seccion'],                                             
                    }
                    print (tomar_ramo_json)
                    response = requests.post(url, json=tomar_ramo_json)
                    print('status_code: {0}'.format(response.status_code))
                    tomar_ramos = response.json()
                    return redirect('/toma-ramos/')
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url,e )) 
    else:
        form = TomaRamosForms()
        form_morosidad = ConsultarMorosidad()
        try:
            headers ={'Authorization' : 'Token'}
            response = requests.get(url_ramos, headers=headers)
            print('status_code: {0}'.format(response.status_code))
            ramos = response.json()
            print (ramos)
            return render(request, 'toma_ramos/agregar_toma_ramo.html', {'form': form, 'form_morosidad': form_morosidad, 'ramos': ramos})
        except Exception as e:
            print('ERROR AL CONSUMIR EL SERVICIO {0}\n{1}'.format(url_ramos,e )) 


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
        return render(request, 'toma_ramos/eliminar_toma_ramo.html')