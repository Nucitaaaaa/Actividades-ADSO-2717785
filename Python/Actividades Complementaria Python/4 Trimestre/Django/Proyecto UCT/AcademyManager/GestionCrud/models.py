
from django.db import models

class Estudiante(models.Model):
    estNombre = models.CharField(max_length=30)
    estApellido = models.CharField(max_length=50)
    estEmail = models.EmailField()
    estTelefono = models.IntegerField(max_length=10)
    estFechaNacimiento = models.DateField()
    estFoto = models.ImageField()
    estFechaCreacion = models.DateTimeField(auto_now_add=True)
    estFechaActualizacion = models.DateTimeField(auto_now=True)
    estCarrera = models.CharField(max_length=50)

    class Meta:
        verbose_name="Estudiante"
        verbose_name_plural="Estudiantes"
        ordering=['id']

class Profesor(models.Model):
    profNombre = models.CharField(max_length=30)
    profApellido = models.CharField(max_length=50)
    profEmail = models.EmailField()
    profTelefono = models.IntegerField(max_length=10)
    profFechaNacimiento = models.DateField()
    profFoto = models.ImageField()
    profFechaCreacion = models.DateTimeField(auto_now_add=True)
    profFechaActualizacion = models.DateTimeField(auto_now=True)
    profCMaterias = models.CharField(max_length=50)

    class Meta:
        verbose_name="Profesor"
        verbose_name_plural="Profesores"
        ordering=['id']

class Carrera(models.Model):
    carNombre = models.CharField(max_length=50)
    carDuracion = models.CharField(max_length=50)
    carMaterias = models.CharField(max_length=50)

    class Meta:
        verbose_name="Carrera"
        verbose_name_plural="Carreras"
        ordering=['id']

class Materia(models.Model):
    matNombre = models.CharField(max_length=50)
    matDescripcion = models.TextField()
    matCreditos = models.IntegerField(max_length=5)
    matFechaCreacion = models.DateTimeField(auto_now_add=True)
    matFechaActualizacion = models.DateTimeField(auto_now=True)
    matCarrera = models.CharField(max_length=50)
    matProfesores = models.CharField(max_length=30)

    class Meta:
        verbose_name="Materia"
        verbose_name_plural="Materias"
        ordering=['id']


