from django import forms


class AlumnoForms(forms.Form):
    rut = forms.CharField()
    nombres = forms.CharField()
    apellidos = forms.CharField()
    email = forms.EmailField()
    direccion = forms.CharField()
    comuna = forms.CharField()
    carrera = forms.CharField()

class TomaRamos(forms.Form):
    id_alumno = forms.IntegerField()
    id_ramo = forms.IntegerField()
    seccion = forms.CharField()

class ReservaLibro(forms.Form):
    nombre = forms.IntegerField()
    autor = forms.IntegerField()

class FinanzasForms(forms.Form):
    id_alumno = forms.IntegerField()
    id_tipo_cuota = forms.IntegerField()
    tipo_cuota = forms.IntegerField()
    num_cuota = forms.IntegerField()
    pagada = forms.CharField()
    fecha_vencimiento = forms.DateField()