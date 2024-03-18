
from django.contrib import admin
from .models import Estudiante, Profesor, Carrera, Materia

# Register your models here.
class EstudianteAdmin(admin.ModelAdmin):
    readonly_fields=('estFechaCreacion', 'estFechaActualizacion')
    admin.site.register(Estudiante) #EstudianteAdmin
    admin.site.register(Profesor) 
    admin.site.register(Carrera) 
    admin.site.register(Materia) 
