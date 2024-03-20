
from django.contrib import admin
from GestionCrud.models import Estudiante, Profesor, Carrera, Materia

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    readonly_fields = ('estFechaCreacion', 'estFechaActualizacion')

admin.site.register(Estudiante, EstudianteAdmin)


class ProfesorAdmin(admin.ModelAdmin):
    readonly_fields = ('profFechaCreacion', 'profFechaActualizacion')

admin.site.register(Profesor, ProfesorAdmin) 


class MateriaAdmin(admin.ModelAdmin):
    readonly_fields = ('matFechaCreacion', 'matFechaActualizacion')

admin.site.register(Materia, MateriaAdmin) 


admin.site.register(Carrera)


title = "Gestion DB UCT"
admin.site.site_header = title
admin.site.site_title= title
admin.site.index_title = "Panel de gestión"
