from django import forms


class AlumnoForms(forms.Form):
    rut = forms.CharField()
    nombres = forms.CharField()
    apellido_paterno = forms.CharField()
    apellido_materno = forms.CharField()
    email = forms.EmailField()
    direccion = forms.CharField()
    comuna = forms.CharField()
    matriculado = forms.CharField()
    morocidad = forms.CharField()
    is_regular = forms.CharField()
    telefono = forms.CharField()

class ArancelesForms(forms.Form):
    sede = forms.CharField()
    direccion = forms.CharField()
    comuna = forms.CharField()

class BibliotecaForms(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    comuna = forms.CharField()

class LibroForms(forms.Form):
    nombre = forms.CharField()
    autor = forms.CharField()
    en_biblioteca = forms.CharField()

class FinanzasForms(forms.Form):
    id_alumno = forms.IntegerField()
    id_aranceles = forms.IntegerField()
    tipo_cuota = forms.CharField()
    num_cuota = forms.IntegerField()
    pagada = forms.CharField()
    fecha_vencimiento = forms.CharField()