from django.db import models

# Create your models here.

class Roles(models.Model):
    nombre_rol = models.CharField(max_length=80, null=False)

class Medicos(models.Model):
    id_medico = models.IntegerField(primary_key=True)
    nombre_medico = models.CharField(max_length=160, null=False)
    apellido_medico = models.CharField(max_length=160, null=False)
    fecha_nacimiento_medico = models.DateTimeField(null=False)
    correo_medico = models.CharField(max_length=80, null=False)
    telefono_medico = models.IntegerField()
    clave_medico = models.CharField(max_length=40, null=False)
    rol = models.ForeignKey(Roles, null=False, on_delete=models.CASCADE)

class GruposFamiliares(models.Model):
    medico = models.ForeignKey(Medicos, null=False, on_delete=models.CASCADE)

class Pacientes(models.Model):
    id_paciente = models.IntegerField(primary_key=True)
    nombre_paciente = models.CharField(max_length=160, null=False)
    apellido_paciente = models.CharField(max_length=160, null=False)
    fecha_nacimiento_paciente = models.DateTimeField(null=False)
    correo_paciente = models.CharField(max_length=80, null=False)
    telefono_paciente = models.IntegerField()
    clave_paciente = models.CharField(max_length=40, null=False)
    medico = models.ForeignKey(Medicos, null=False, on_delete=models.CASCADE)
    grupo_familiar = models.ForeignKey(GruposFamiliares, null=False, on_delete=models.CASCADE)

class Reportes(models.Model):
    fecha_reporte = models.DateTimeField(auto_now_add=True, null=False)
    descripcion_reporte = models.CharField(max_length=2000)
    paciente = models.ForeignKey(Pacientes, null=False, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, null=False, on_delete=models.CASCADE)

class HistoriaMedica(models.Model):
    paciente = models.ForeignKey(Pacientes, null=False, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, null=False, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(null=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True, null=False)
    descripcion = models.CharField(max_length=2000, null=False)