from django import forms


class AlumnoForms(forms.Form):
    rut = forms.CharField()
    nombres = forms.CharField()
    apellidos = forms.CharField()
    email = forms.EmailField()
    direccion = forms.CharField()
    comuna = forms.CharField()
    carrera = forms.CharField()

class TomaRamosForms(forms.Form):
    id_alumno = forms.IntegerField()
    id_ramo = forms.IntegerField()
    seccion = forms.CharField()

class ReservaLibroForms(forms.Form):
    id_alumno = forms.IntegerField()
    id_libro = forms.IntegerField()

class FinanzasForms(forms.Form):
    id_alumno = forms.IntegerField()
    id_tipo_cuota = forms.IntegerField()
    num_cuota = forms.IntegerField()
    valor = forms.IntegerField()
    pagada = forms.CharField()
    fecha_vencimiento = forms.DateField(input_formats=['%Y-%m-%d'])

class ConsultarMorosidad(forms.Form):
    rut = forms.CharField(label="Ingresar Rut")