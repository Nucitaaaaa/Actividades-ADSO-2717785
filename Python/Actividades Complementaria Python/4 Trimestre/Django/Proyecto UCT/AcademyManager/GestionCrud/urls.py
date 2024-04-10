
from django.urls import path
import GestionCrud.views

urlpatterns = [
    #?Rutas generales
    path('', GestionCrud.views.index, name='index'),
    path('registrarse/', GestionCrud.views.paginaRegistro, name='registrarse'),
    path('login/', GestionCrud.views.paginaLogin, name='login'),
    path('logout/', GestionCrud.views.paginaLogout, name='logout'),
    path('quienesSomos/', GestionCrud.views.quienesSomos, name='quienesSomos'),
    path('contactos/', GestionCrud.views.contactos, name='contactos'),
    path('academicManager/', GestionCrud.views.academicManager, name='academicManager'),

    #?Rutas clase Estudiante
    path('estudiantes/', GestionCrud.views.mostrarEstudiantes, name='mostrarEstudiantes'),
    path('estudiantes/<int:id>/', GestionCrud.views.mostrarEstudiante, name='mostrarEstudiante'),
    path('estudiantes/añadir/', GestionCrud.views.añadirEstudiante, name='añadirEstudiante'),
    path('estudiantes/modificar/<int:id>/', GestionCrud.views.modificarEstudiante, name='modificarEstudiante'),
    path('estudiantes/eliminar/<int:id>/', GestionCrud.views.eliminarEstudiante, name='eliminarEstudiante'),

    #?Rutas clase Profesor
    path('profesores/', GestionCrud.views.mostrarProfesores, name='mostrarProfesores'),
    path('profesores/<int:id>/', GestionCrud.views.mostrarProfesor, name='mostrarProfesor'),
    path('profesores/añadir/', GestionCrud.views.añadirProfesor, name='añadirProfesor'),
    path('profesores/modificar/<int:id>/', GestionCrud.views.modificarProfesor, name='modificarProfesor'),
    path('profesores/eliminar/<int:id>/', GestionCrud.views.eliminarProfesor, name='eliminarProfesor'),

    #?Rutas clase Carrera
    path('carreras/', GestionCrud.views.mostrarCarreras, name='mostrarCarreras'),
    path('carreras/<int:id>/', GestionCrud.views.mostrarCarrera, name='mostrarCarrera'),
    path('carreras/añadir/', GestionCrud.views.añadirCarrera, name='añadirCarrera'),
    path('carreras/modificar/<int:id>/', GestionCrud.views.modificarCarrera, name='modificarCarrera'),
    path('carreras/eliminar/<int:id>/', GestionCrud.views.eliminarCarrera, name='eliminarCarrera'),

    #?Rutas clase Materia
    path('materias/', GestionCrud.views.mostrarMaterias, name='mostrarMaterias'),
    path('materias/<int:id>/', GestionCrud.views.mostrarMateria, name='mostrarMateria'),
    path('materias/añadir/', GestionCrud.views.añadirMateria, name='añadirMateria'),
    path('materias/modificar/<int:id>/', GestionCrud.views.modificarMateria, name='modificarMateria'),
    path('materias/eliminar/<int:id>/', GestionCrud.views.eliminarMateria, name='eliminarMateria'),
]

