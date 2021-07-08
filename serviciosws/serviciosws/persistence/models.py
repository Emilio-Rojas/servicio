# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
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

    def json(self):
        return {
                'rut': self.rut,
                'nombres': self.nombres,
                'apellido_paterno': self.apellido_paterno,
                'apellido_materno': self.apellido_materno,
                'email': self.email,
                'direccion': self.direccion,
                'comuna': self.comuna,
                'matriculado': self.matriculado,
                'morocidad': self.morocidad,
                'is_regular': self.is_regular,
                'telefono': self.telefono,
                }


class Aranceles(models.Model):
    id = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'aranceles'

    def json(self):
        return {
                'sede': self.sede,
                'direccion': self.direccion,
                'comuna': self.comuna,
                }


class Biblioteca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    comuna = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'biblioteca'

    def json(self):
        return {
                'nombre': self.nombre,
                'direccion': self.direccion,
                'comuna': self.comuna,
                }

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    autor = models.CharField(max_length=50, blank=True, null=True)
    en_biblioteca = models.ForeignKey(Biblioteca, models.DO_NOTHING, db_column='en_biblioteca')

    class Meta:
        managed = False
        db_table = 'libro'
    
    def json(self):
        return {
                'nombre': self.nombre,
                'autor': self.autor,
                'en_biblioteca': self.en_biblioteca.json(),
                }


class Pagos(models.Model):
    id = models.AutoField(primary_key=True)
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='id_alumno')
    id_aranceles = models.ForeignKey(Aranceles, models.DO_NOTHING, db_column='id_aranceles')
    tipo_cuota = models.CharField(max_length=50, blank=True, null=True)
    num_cuota = models.IntegerField()
    pagada = models.IntegerField(blank=True, null=True)
    fecha_vencimiento = models.DateField()

    class Meta:
        managed = False
        db_table = 'pagos'

    def json(self):
        return {
                'id_alumno': self.id_alumno.json(),
                'id_aranceles': self.id_aranceles.json(),
                'tipo_cuota': self.email,
                'num_cuota': self.telefono,
                'pagada': self.pagada,
                'fecha_vencimiento': self.fecha_vencimiento,
                }
