
from django.db import models

class Carrera(models.Model):
    carNombre = models.CharField(max_length=50, verbose_name='Nombre')
    carDuracion = models.CharField(max_length=50, verbose_name='Duración')
    carMaterias = models.ManyToManyField('Materia', verbose_name='Materias')

    class Meta:
        verbose_name="Carrera"
        verbose_name_plural="Carreras"
        ordering=['id']

    def __str__(self):
        return f"{self.carNombre}"
    

class Estudiante(models.Model):
    estNombre = models.CharField(max_length=30, verbose_name='Nombre')
    estApellido = models.CharField(max_length=50, verbose_name='Apellido')
    estEmail = models.EmailField(verbose_name='Email')
    estTelefono = models.IntegerField(verbose_name='Telefono')
    estFechaNacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    estFoto = models.ImageField(default='null', verbose_name='Foto', upload_to="estFotos")
    estFechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    estFechaActualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    estCarrera = models.ForeignKey(Carrera, verbose_name='Carrera', on_delete=models.CASCADE)

    class Meta:
        verbose_name="Estudiante"
        verbose_name_plural="Estudiantes"
        ordering=['id']

    def __str__(self):
        return f"{self.estNombre} {self.estApellido}"


class Materia(models.Model):
    matNombre = models.CharField(max_length=50, verbose_name='Nombre')
    matDescripcion = models.TextField(verbose_name='Descripcion')
    matCreditos = models.IntegerField(verbose_name='Creditos')
    matFechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    matFechaActualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    matCarrera = models.ManyToManyField(Carrera, verbose_name='Carrera')
    matProfesores = models.ForeignKey('Profesor', verbose_name='Profesor', on_delete=models.CASCADE)

    class Meta:
        verbose_name="Materia"
        verbose_name_plural="Materias"
        ordering=['id']
    
    def __str__(self):
        return f"{self.matNombre}"
    

class Profesor(models.Model):
    profNombre = models.CharField(max_length=30, verbose_name='Nombre')
    profApellido = models.CharField(max_length=50, verbose_name='Apellido')
    profEmail = models.EmailField(verbose_name='Email')
    profTelefono = models.IntegerField(verbose_name='Telefono')
    profFechaNacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    profFoto = models.ImageField(upload_to="profFotos",  verbose_name='Foto')
    profFechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    profFechaActualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    profMaterias = models.ManyToManyField(Materia, verbose_name='Materias')

    class Meta:
        verbose_name="Profesor"
        verbose_name_plural="Profesores"
        ordering=['id']

    def __str__(self):
        return f"{self.profNombre} {self.profApellido}"

    

