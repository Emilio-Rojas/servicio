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

    def json(self):
        return {
                'rut': self.rut,
                'nombres': self.nombres,
                'apellidos': self.apellidos,
                'email': self.email,
                'direccion': self.direccion,
                'comuna': self.comuna,
                'carrera': self.carrera,
                }


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

    def json(self):
        return {
                'id_alumno': self.id_alumno.json(),
                'id_tipo_cuota': self.id_tipo_cuota.json(),
                'num_cuota': self.num_cuota,
                'valor': self.valor,
                'pagada': self.pagada,
                'fecha_vencimiento': self.fecha_vencimiento,
                }


class Libro(models.Model):
    nombre = models.CharField(max_length=20)
    editorial = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'libro'

    def json(self):
        return {
                'nombre': self.nombre,
                'editorial': self.editorial,
                'autor': self.autor,
                }


class Ramos(models.Model):
    nombre = models.CharField(max_length=20)
    creditos = models.IntegerField()
    obligatorio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ramos'

    def json(self):
        return {
                'nombre': self.nombre,
                'creditos': self.creditos,
                'obligatorio': self.obligatorio,
                }


class ReservaLibro(models.Model):
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='id_alumno')
    id_libro = models.ForeignKey(Libro, models.DO_NOTHING, db_column='id_libro')

    class Meta:
        managed = False
        db_table = 'reserva_libro'

    def json(self):
        return {
                'id_alumno': self.id_alumno.json(),
                'id_libro': self.id_libro.json(),
                }


class TipoCuota(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_cuota'

    def json(self):
        return {
                'nombre': self.nombre,
                }


class TomaRamos(models.Model):
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='id_alumno')
    id_ramo = models.ForeignKey(Ramos, models.DO_NOTHING, db_column='id_ramo')
    seccion = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'toma_ramos'

    def json(self):
        return {
                'id_alumno': self.id_alumno.json(),
                'id_ramo': self.id_ramo.json(),
                'seccion': self.seccion,
                }
