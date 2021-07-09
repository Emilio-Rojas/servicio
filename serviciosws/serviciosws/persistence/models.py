# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumno(models.Model):
    rut = models.CharField(max_length=20)
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    matriculado = models.IntegerField()
    morocidad = models.IntegerField()
    is_regular = models.IntegerField()
    telefono = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alumno'


class Aranceles(models.Model):
    sede = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'aranceles'


class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'biblioteca'


class Finanzas(models.Model):
    id_alumno = models.CharField(max_length=10)
    id_aranceles = models.CharField(max_length=10)
    tipo_cuota = models.CharField(max_length=50, blank=True, null=True)
    num_cuota = models.CharField(max_length=10)
    pagada = models.IntegerField(blank=True, null=True)
    fecha_vencimiento = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'finanzas'


class Libro(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    autor = models.CharField(max_length=50, blank=True, null=True)
    en_biblioteca = models.ForeignKey(Biblioteca, models.DO_NOTHING, db_column='en_biblioteca')

    class Meta:
        managed = False
        db_table = 'libro'
