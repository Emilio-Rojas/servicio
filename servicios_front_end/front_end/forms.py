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