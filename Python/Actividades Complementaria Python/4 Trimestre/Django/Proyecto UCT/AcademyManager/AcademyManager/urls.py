"""
URL configuration for AcademyManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
import GestionCrud.views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GestionCrud.views.index, name='index'),

    #?Rutas clase Estudiante
    path('estudiantes/', GestionCrud.views.mostrarEstudiantes, name='mostrarEstudiantes'),
    path('estudiantes/<int:id>/', GestionCrud.views.mostrarEstudiante, name='mostrarEstudiante'),
    path('estudiantes/añadir/', GestionCrud.views.añadirEstudiante, name='añadirEstudiante'),
    path('estudiantes/añadirForm/', GestionCrud.views.añadirEstudianteForm, name='añadirEstudianteForm'),
    path('estudiantes/<int:id>/modificar/', GestionCrud.views.modificarEstudiante, name='modificarEstudiante'),
    path('estudiantes/<int:id>/eliminar/', GestionCrud.views.eliminarEstudiante, name='eliminarEstudiante'),

    #?Rutas clase Profesor
    path('profesores/', GestionCrud.views.mostrarProfesores, name='mostrarProfesores'),
    path('profesores/<int:id>/', GestionCrud.views.mostrarProfesor, name='mostrarProfesor'),
    path('profesores/añadir/', GestionCrud.views.añadirProfesor, name='añadirProfesor'),
    path('profesores/añadirForm/', GestionCrud.views.añadirProfesorForm, name='añadirProfesorForm'),
    path('profesores/<int:id>/modificar/', GestionCrud.views.modificarProfesor, name='modificarProfesor'),
    path('profesores/<int:id>/eliminar/', GestionCrud.views.eliminarProfesor, name='eliminarProfesor'),

    #?Rutas clase Carrera
    path('carreras/', GestionCrud.views.mostrarCarreras, name='mostrarCarreras'),
    path('carreras/<int:id>/', GestionCrud.views.mostrarCarrera, name='mostrarCarrera'),
    path('carreras/añadir/', GestionCrud.views.añadirCarrera, name='añadirCarrera'),
    path('carreras/añadirForm/', GestionCrud.views.añadirCarreraForm, name='añadirCarreraForm'),
    path('carreras/<int:id>/modificar/', GestionCrud.views.modificarCarrera, name='modificarCarrera'),
    path('carreras/<int:id>/eliminar/', GestionCrud.views.eliminarCarrera, name='eliminarCarrera'),

    #?Rutas clase Materia
    path('materias/', GestionCrud.views.mostrarMaterias, name='mostrarMaterias'),
    path('materias/<int:id>/', GestionCrud.views.mostrarMateria, name='mostrarMateria'),
    path('materias/añadir/', GestionCrud.views.añadirMateria, name='añadirMateria'),
    path('materias/añadirForm/', GestionCrud.views.añadirMateriaForm, name='añadirMateriaForm'),
    path('materias/<int:id>/modificar/', GestionCrud.views.modificarMateria, name='modificarMateria'),
    path('materias/<int:id>/eliminar/', GestionCrud.views.eliminarMateria, name='eliminarMateria'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    
