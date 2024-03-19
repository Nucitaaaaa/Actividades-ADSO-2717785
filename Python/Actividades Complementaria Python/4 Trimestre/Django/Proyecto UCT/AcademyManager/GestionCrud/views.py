
from django.shortcuts import render, HttpResponse, redirect
from django.db import connection
from GestionCrud.models import Estudiante, Profesor, Materia, Carrera

def index(request):
    return render(request, "layout.html")

#?Vistas clase Estudiantes 

def mostrarEstudiantes(request):
    estudiantes = Estudiante.objects.raw("SELECT id, estNombre, estApellido, estCarrera FROM GestionCrud_estudiante")

    return render(request, 'estudiante.html', {
        'estudiantes' : estudiantes,
    })

def mostrarEstudiante(request):
    return HttpResponse('Hi')

def añadirEstudiante(request):
    estudiante = Estudiante(
        estNombre='juan',
        estApellido='nose',
        estEmail = 'juanprueba@gmail.com',
        estTelefono =  '098765432',
        estFechaNacimiento = '1999-02-02',
        estCarrera = 'Economia'
    )

    estudiante.save()
    return HttpResponse('Articulo creado')

def modificarEstudiante(request):
    return HttpResponse('Hi')

def eliminarEstudiante(request):
    return HttpResponse('Hi')



#?Vistas clase Profesor

def mostrarProfesores(request):
    profesores = Profesor.objects.raw("SELECT id, profNombre, profApellido, profEmail FROM GestionCrud_profesor")

    return render(request, "profesor.html", {
        'profesores' : profesores,
    })

def mostrarProfesor(request):
    return HttpResponse('Hi')

def añadirProfesor(request):
    return HttpResponse('Hi')

def modificarProfesor(request):
    return HttpResponse('Hi')

def eliminarProfesor(request):
    return HttpResponse('Hi')



#?Vistas clase Carrera

def mostrarCarreras(request):
    carreras = Carrera.objects.raw("SELECT id, carNombre FROM GestionCrud_carrera")

    return render(request, "carrera.html", {
        'carreras' : carreras,
    })

def mostrarCarrera(request):
    return HttpResponse('Hi')

def añadirCarrera(request):
    return HttpResponse('Hi')

def modificarCarrera(request):
    return HttpResponse('Hi')

def eliminarCarrera(request):
    return HttpResponse('Hi')



#?Vistas clase Materia

def mostrarMaterias(request):
    materias = Materia.objects.raw("SELECT id, matNombre FROM GestionCrud_materia")

    return render(request, "materia.html", {
        'materias' : materias,
    })

def mostrarMateria(request):
    return HttpResponse('Hi')

def añadirMateria(request):
    return HttpResponse('Hi')

def modificarMateria(request):
    return HttpResponse('Hi')

def eliminarMateria(request):
    return HttpResponse('Hi')