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
    apellidos = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)
    carrera = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'alumno'


class Finanzas(models.Model):
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='id_alumno')
    id_tipo_cuota = models.ForeignKey('TipoCuota', models.DO_NOTHING, db_column='id_tipo_cuota')
    num_cuota = models.IntegerField()
    valor = models.IntegerField()
    pagada = models.IntegerField(blank=True, null=True)
    fecha_vencimiento = models.DateField()

    class Meta:
        managed = False
        db_table = 'finanzas'


class Libro(models.Model):
    nombre = models.CharField(max_length=20)
    editorial = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'libro'


class Ramos(models.Model):
    nombre = models.CharField(max_length=20)
    creditos = models.IntegerField()
    obligatorio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ramos'


class ReservaLibro(models.Model):
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='id_alumno')
    id_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='id_libro')

    class Meta:
        managed = False
        db_table = 'reserva_libro'


class TipoCuota(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_cuota'


class TomaRamos(models.Model):
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='id_alumno')
    id_ramo = models.ForeignKey(Ramos, models.DO_NOTHING, db_column='id_ramo')
    seccion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'toma_ramos'
