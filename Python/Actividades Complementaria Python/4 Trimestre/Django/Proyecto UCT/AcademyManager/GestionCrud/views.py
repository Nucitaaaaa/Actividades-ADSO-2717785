
from django.shortcuts import render, HttpResponse, redirect
from django.db import connection
from GestionCrud.models import Estudiante, Profesor, Materia, Carrera
from GestionCrud.forms import FormEstudiante, FormProfesor, FormCarrera, FormMateria, FormActualizarEstudiante, FormActualizarProfesor, FormActualizarCarrera, FormActualizarMateria, FormRegistro
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "inicio.html")


def quienesSomos(request):
    return render(request, "quienesSomos.html")


def contactos(request):
    return render(request, "contactos.html")

@login_required(login_url="login")
def academicManager(request):
    return render(request, "academicManager.html")


#?Vistas clase Estudiantes 

def mostrarEstudiantes(request):
    estudiantes = Estudiante.objects.raw("SELECT * FROM GestionCrud_estudiante")

    return render(request, 'estudiante.html', {
        'estudiantes' : estudiantes,
    })


def mostrarEstudiante(request, id):
    # estudiantes = Estudiante.objects.raw("SELECT * FROM GestionCrud_estudiante WHERE id = %s", [id])
    estudiante = Estudiante.objects.get(pk = id)

    return render(request, 'estudianteDetalles.html', {
        'estudiante' : estudiante,
    })


def añadirEstudiante(request):
    formulario = FormEstudiante()

    if request.method == 'POST': 
        formulario = FormEstudiante(request.POST, request.FILES) 

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

            messages.success(request, f'El estudiante "{estudiante.estNombre} {estudiante.estApellido}" se ha añadido con exito')
            return redirect('mostrarEstudiantes')
            
        else:
            return render(request, 'estudianteAñadir.html', {'formulario': formulario})
        
    else:
        formulario = FormEstudiante()
        return render(request, 'estudianteAñadir.html', {'formulario': formulario})
    

def modificarEstudiante(request, id):
    estudiante = Estudiante.objects.get(pk=id)

    if request.method == 'POST':
        formulario = FormActualizarEstudiante(request.POST, request.FILES, instance=estudiante)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Los datos del estudiante "{estudiante.estNombre} {estudiante.estApellido}" se han modificado con éxito')
            return redirect('mostrarEstudiantes')
    else:
        formulario = FormActualizarEstudiante(instance=estudiante)

    return render(request, 'estudianteModificar.html', {'formulario': formulario})


def eliminarEstudiante(request, id):
    estudiante = Estudiante.objects.get(pk=id)

    estudiante.delete()
    messages.success(request, f'El estudiante se ha eliminado con éxito')
    
    return redirect('mostrarEstudiantes')

#?Vistas clase Profesor

def mostrarProfesores(request):
    profesores = Profesor.objects.raw("SELECT id, profNombre, profApellido, profEmail FROM GestionCrud_profesor")

    return render(request, "profesor.html", {
        'profesores' : profesores,
    })

def mostrarProfesor(request, id):
    profesor = Profesor.objects.get(pk = id)

    return render(request, "profesorDetalles.html", {
        'profesor' : profesor,
    })

def añadirProfesor(request):
    formulario = FormProfesor() 

    if request.method == 'POST': 

        formulario = FormProfesor(request.POST, request.FILES) 

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            profNombre = data_form.get('nombre')
            profApellido = data_form.get('apellido')
            profEmail = data_form.get('email')
            profTelefono = data_form.get('telefono')
            profFechaNacimiento = data_form.get('fechaNacimiento')
            profFoto = data_form.get('foto')
            profMaterias = data_form.get('materias')

            profesor = Profesor( 
                profNombre = profNombre,
                profApellido = profApellido,
                profEmail = profEmail,
                profTelefono = profTelefono,
                profFechaNacimiento = profFechaNacimiento,
                profFoto = profFoto,
                profMaterias = profMaterias
            )

            profesor.save()

            messages.success(request, f'El profesor "{profesor.profNombre} {profesor.profApellido}" se ha añadido con exito')
            return redirect('mostrarProfesores')
            
        else:
            return render(request, 'profesorAñadir.html', {'formulario': formulario}) 
        
    else:
        formulario = FormProfesor() 
        return render(request, 'profesorAñadir.html', {'formulario': formulario})
    

def modificarProfesor(request, id):
    profesor = Profesor.objects.get(pk=id)

    if request.method == 'POST':
        formulario = FormActualizarProfesor(request.POST, request.FILES, instance=profesor)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Los datos del profesor "{profesor.profNombre} {profesor.profApellido}" se han modificado con éxito')
            return redirect('mostrarProfesores')
    else:
        formulario = FormActualizarProfesor(instance=profesor)

    return render(request, 'profesorModificar.html', {'formulario': formulario})


def eliminarProfesor(request, id):
    profesor = Profesor.objects.get(pk=id)

    profesor.profMaterias.clear()
    profesor.delete()

    messages.success(request, f'El Profesor se ha eliminado con éxito')
    
    return redirect('mostrarProfesores')

#?Vistas clase Carrera

def mostrarCarreras(request):
    carreras = Carrera.objects.raw("SELECT id, carNombre FROM GestionCrud_carrera")

    return render(request, "carrera.html", {
        'carreras' : carreras,
    })


def mostrarCarrera(request, id):
    carrera = Carrera.objects.get(pk = id)

    return render(request, "carreraDetalles.html", {
        'carrera' : carrera,
    })


def añadirCarrera(request):
    formulario = FormCarrera() 

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

            messages.success(request, f'La carrera "{carrera.carNombre}" se ha añadido con exito')
            carrera.save()

            return redirect('mostrarCarreras')
            
        else:
            return render(request, 'carreraAñadir.html', {'formulario': formulario})
        
    else: 
        formulario = FormCarrera() 
        return render(request, 'carreraAñadir.html', {'formulario': formulario})


def modificarCarrera(request, id):
    carrera = Carrera.objects.get(pk=id)

    if request.method == 'POST':
        formulario = FormActualizarCarrera(request.POST, instance=carrera)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Los datos de la carrera "{carrera.carNombre}" se han modificado con éxito')
            return redirect('mostrarCarreras')
    else:
        formulario = FormActualizarCarrera(instance=carrera)

    return render(request, 'carreraModificar.html', {'formulario': formulario})


def eliminarCarrera(request, id):
    carrera = Carrera.objects.get(pk=id)

    carrera.carMaterias.clear()
    carrera.delete()
    messages.success(request, f'La carrera "{carrera.carNombre}" se ha eliminado con éxito')
    
    return redirect('mostrarCarreras')


#?Vistas clase Materia

def mostrarMaterias(request):
    materias = Materia.objects.raw("SELECT id, matNombre FROM GestionCrud_materia")

    return render(request, "materia.html", {
        'materias' : materias,
    })

def mostrarMateria(request, id):
    materia = Materia.objects.get(pk = id)

    return render(request, "materiaDetalles.html", {
        'materia' : materia,
    })

def añadirMateria(request):
    formulario = FormMateria()

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
                matNombre=matNombre,
                matDescripcion=matDescripcion,
                matCreditos=matCreditos,
                matProfesores=matProfesores,
            )

            materia.save()

            if matCarrera:
                materia.matCarrera.set(matCarrera)

            messages.success(request, f'La materia "{materia.matNombre}" se ha añadido con exito')
            materia.save()

            return redirect('mostrarMaterias')
            
        else:
            return render(request, 'materiaAñadir.html', {'formulario': formulario})
        
    else:
        formulario = FormMateria()
        return render(request, 'materiaAñadir.html', {'formulario': formulario})


def modificarMateria(request, id):
    materia = Materia.objects.get(pk=id)

    if request.method == 'POST':
        formulario = FormActualizarMateria(request.POST, instance=materia)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, f'Los datos de la materia "{materia.matNombre}" se han modificado con éxito')
            return redirect('mostrarMaterias')
    else:
        formulario = FormActualizarMateria(instance=materia)

    return render(request, 'materiaModificar.html', {'formulario': formulario})
    

def eliminarMateria(request, id):
    materia = Materia.objects.get(pk=id)

    materia.matCarrera.clear()
    materia.delete()
    messages.success(request, f'La Materia se ha eliminado con éxito')
    
    return redirect('mostrarMaterias')


def paginaRegistro(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    else:
        formRegistro = FormRegistro()
        
        if request.method == 'POST':
            formRegistro = FormRegistro(request.POST)

            if formRegistro.is_valid():
                formRegistro.save()
                messages.success(request, f'El usuario se ha registrado con exito')
                return redirect('index')
            
    return render(request, 'users/registro.html', {
        'formRegistro' : formRegistro
        })


def paginaLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            
            else:
                messages.warning(request, "El Usuario o Contraseña son incorrectas")

    return render(request, 'users/login.html')


def paginaLogout(request):
    logout(request)
    return redirect('index')