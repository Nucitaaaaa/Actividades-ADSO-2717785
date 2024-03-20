
from django.shortcuts import render, HttpResponse, redirect
from django.db import connection
from GestionCrud.models import Estudiante, Profesor, Materia, Carrera
from GestionCrud.forms import FormEstudiante, FormProfesor, FormCarrera, FormMateria
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request, "layout.html")

#?Vistas clase Estudiantes 

def mostrarEstudiantes(request):
    estudiantes = Estudiante.objects.raw("SELECT id, estNombre, estApellido, estCarrera FROM GestionCrud_estudiante")

    return render(request, 'estudiante.html', {
        'estudiantes' : estudiantes,
    })

def mostrarEstudiante(request, id):
    estudiantes = Estudiante.objects.raw("SELECT * FROM GestionCrud_estudiante WHERE id = %s", [id])

    return render(request, 'estudianteDetalles.html', {
        'estudiantes' : estudiantes,
    })

def añadirEstudiante(request):
    if request.method == 'POST': 

        formulario = FormEstudiante(request.POST) 

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            estNombre = data_form.get('nombre')
            estApellido = data_form.get('apellido')
            estEmail = data_form.get('email')
            estTelefono = data_form.get('telefono')
            estFechaNacimiento = data_form.get('fechaNacimiento')
            estFoto = data_form.get('foto')
            estCarrera = data_form.get('carrera')

            estudiante = Estudiante( 
                estNombre = estNombre,
                estApellido = estApellido,
                estEmail = estEmail,
                estTelefono = estTelefono,
                estFechaNacimiento = estFechaNacimiento,
                estFoto = estFoto,
                estCarrera = estCarrera
            )

            estudiante.save()

            return redirect('mostrarEstudiantes')
            
        else:
            return render(request, 'estudianteAñadir.html', {
                'formulario': formulario
            })
        
    else:
        return render(request, 'estudianteAñadir.html', {
                'formulario': formulario
            })

def añadirEstudianteForm(request):
    formulario = FormEstudiante()

    return render(request, 'estudianteAñadir.html', {
        'formulario': formulario
    })

def modificarEstudiante(request):
    return HttpResponse('Hi')

def eliminarEstudiante(request, id):
    # try:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM GestionCrud_estudiante WHERE id = %s", [id])
        
    return redirect('mostrarEstudiantes')
    
    # except ObjectDoesNotExist:

    #     return HttpResponse ("<strong>Articulo no encontrado</strong>", redirect())


#?Vistas clase Profesor

def mostrarProfesores(request):
    profesores = Profesor.objects.raw("SELECT id, profNombre, profApellido, profEmail FROM GestionCrud_profesor")

    return render(request, "profesor.html", {
        'profesores' : profesores,
    })

def mostrarProfesor(request, id):
    profesores = Profesor.objects.raw("SELECT * FROM GestionCrud_profesor WHERE id = %s", [id])

    return render(request, "profesorDetalles.html", {
        'profesores' : profesores,
    })

def añadirProfesor(request):
    if request.method == 'POST': 

        formulario = FormProfesor(request.POST) 

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            profNombre = data_form.get('nombre')
            profApellido = data_form.get('apellido')
            profEmail = data_form.get('email')
            profTelefono = data_form.get('telefono')
            profFechaNacimiento = data_form.get('fechaNacimiento')
            profFoto = data_form.get('foto')
            profCMaterias = data_form.get('materias')

            profesor = Profesor( 
                profNombre = profNombre,
                profApellido = profApellido,
                profEmail = profEmail,
                profTelefono = profTelefono,
                profFechaNacimiento = profFechaNacimiento,
                profFoto = profFoto,
                profCMaterias = profCMaterias
            )

            profesor.save()

            return redirect('mostrarProfesores')
            
        else:
            return render(request, 'profesorAñadir.html', {
                'formulario': formulario
            })
        
    else:
        return render(request, 'profesorAñadir.html', {
                'formulario': formulario
            })

def añadirProfesorForm(request):
    formulario = FormProfesor()

    return render(request, 'profesorAñadir.html', {
        'formulario': formulario
    })

def modificarProfesor(request):
    return HttpResponse('Hi')

def eliminarProfesor(request, id):
    # try:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM GestionCrud_profesor WHERE id = %s", [id])
        
    return redirect('mostrarProfesores')



#?Vistas clase Carrera

def mostrarCarreras(request):
    carreras = Carrera.objects.raw("SELECT id, carNombre FROM GestionCrud_carrera")

    return render(request, "carrera.html", {
        'carreras' : carreras,
    })

def mostrarCarrera(request, id):
    carreras = Carrera.objects.raw("SELECT * FROM GestionCrud_profesor WHERE id = %s", [id])

    return render(request, "carreraDetalles.html", {
        'carreras' : carreras,
    })

def añadirCarrera(request):
    if request.method == 'POST': 

        formulario = FormCarrera(request.POST) 

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            carNombre = data_form.get('nombre')
            carDuracion = data_form.get('duracion')
            carMaterias = data_form.get('materias')

            carrera = Carrera( 
                carNombre = carNombre,
                carDuracion = carDuracion,
                carMaterias = carMaterias,
            )

            carrera.save()

            return redirect('mostrarCarreras')
            
        else:
            return render(request, 'carreraAñadir.html', {
                'formulario': formulario
            })
        
    else:
        return render(request, 'carreraAñadir.html', {
                'formulario': formulario
            })

def añadirCarreraForm(request):
    formulario = FormCarrera()

    return render(request, 'carreraAñadir.html', {
        'formulario': formulario
    })

def modificarCarrera(request):
    return HttpResponse('Hi')

def eliminarCarrera(request, id):
    # try:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM GestionCrud_carrera WHERE id = %s", [id])
        
    return redirect('mostrarCarreras')



#?Vistas clase Materia

def mostrarMaterias(request):
    materias = Materia.objects.raw("SELECT id, matNombre FROM GestionCrud_materia")

    return render(request, "materia.html", {
        'materias' : materias,
    })

def mostrarMateria(request, id):
    materias = Materia.objects.raw("SELECT * FROM GestionCrud_profesor WHERE id = %s", [id])

    return render(request, "materiaDetalles.html", {
        'materias' : materias,
    })

def añadirMateria(request):
    if request.method == 'POST': 

        formulario = FormMateria(request.POST) 

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            matNombre = data_form.get('nombre')
            matDescripcion = data_form.get('descripcion')
            matCreditos = data_form.get('creditos')
            matCarrera = data_form.get('carrera')
            matProfesores = data_form.get('profesor')
            

            materia = Materia( 
                matNombre = matNombre,
                matDescripcion = matDescripcion,
                matCreditos = matCreditos,
                matCarrera = matCarrera,
                matProfesores = matProfesores,
            )

            materia.save()

            return redirect('mostrarMaterias')
            
        else:
            return render(request, 'materiaAñadir.html', {
                'formulario': formulario
            })
        
    else:
        return render(request, 'materiaAñadir.html', {
                'formulario': formulario
            })

def añadirMateriaForm(request):
    formulario = FormMateria()

    return render(request, 'materiaAñadir.html', {
        'formulario': formulario
    })

def modificarMateria(request):
    return HttpResponse('Hi')

def eliminarMateria(request, id):
    # try:
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM GestionCrud_materia WHERE id = %s", [id])
        
    return redirect('mostrarMaterias')