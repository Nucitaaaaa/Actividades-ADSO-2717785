
from django import forms
from django.core import validators
from .models import Estudiante, Profesor, Materia, Carrera

class FormEstudiante(forms.Form):

    nombre = forms.CharField(
        label="Nombre",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formEstNombre',
                'placeholder':'Ingrese su nombre'
            }
        ),
        validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Nombre): solo se permiten letras y espacios.')
        ]
    )


    apellido = forms.CharField(        
        label="Apellido",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formEstApe',
                'placeholder':'Ingrese su apellido'
            }
        ),
        validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Apellido): solo se permiten letras y espacios.')
        ]
    )
    
    email = forms.EmailField(
        label="E-mail",
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'formEstEmail',
                'placeholder':'Ingrese su E-mail'
            }
        ),
        validators= [
            validators.EmailValidator('Error(Email): El email está mal digitado.')
        ]
    )

    telefono = forms.IntegerField(
        label="Telefono",
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class':'formEstTel',
                'placeholder':'Ingrese su numero de telefono'
            }
        ),
        validators= [
            validators.RegexValidator('^[0-9]+$', 'Error(Telefono): solo se permiten numeros.')
        ]
    )

    fechaNacimiento = forms.DateField(
        label="Fecha De Nacimiento",
        required=True,
        widget=forms.DateTimeInput(
            attrs={
                'class':'formEstFeNa',
                'type': 'date'
            }
        )
    )

    foto = forms.ImageField(
        label="Foto",
        required=False,
    )

    carrera = forms.CharField(
        label="Carrera",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formEstCar',
                'placeholder':'Ingrese el nombre de su carrera'
            }
        ),
        validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Carrera): solo se permiten letras y espacios.')
        ]
    )


class FormActualizarEstudiante(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['estNombre', 'estApellido', 'estEmail', 'estTelefono', 'estFechaNacimiento', 'estFoto', 'estCarrera']


class FormProfesor(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formProfNombre',
                'placeholder':'Ingrese su nombre'
            }
        ),validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Nombre): solo se permiten letras y espacios.')
        ]
    )

    apellido = forms.CharField(        
        label="Apellido",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formProfApe',
                'placeholder':'Ingrese su apellido'
            }
        ),validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Apellido): solo se permiten letras y espacios.')
        ]
    )
    
    email = forms.EmailField(
        label="E-mail",
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class':'formProfEmail',
                'placeholder':'Ingrese su E-mail'
            }
        ), 
        validators= [
            validators.EmailValidator('Error(Email): El email está mal digitado.')
        ]
    )

    telefono = forms.IntegerField(
        label="Telefono",
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class':'formProfTel',
                'placeholder':'Ingrese su numero de telefono'
            }
        ), 
        validators= [
            validators.RegexValidator('^[0-9]+$', 'Error(Telefono): solo se permiten numeros.')
        ]
    )

    fechaNacimiento = forms.DateField(
        label="Fecha De Nacimiento",
        required=True,
        widget=forms.DateInput(
            attrs={
                'class':'formProfFeNa',
                'type': 'date'
            }
        )
    )

    foto = forms.ImageField(
        label="Foto",
        required=False,
    )

    materias = forms.CharField(
        label="Materias",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formProfMat',
                'placeholder':'Ingrese el nombre de su materia'
            }
        ), 
        validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Materia): solo se permiten letras y espacios.')
        ]
    )

class FormActualizarProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['profNombre', 'profApellido', 'profEmail', 'profTelefono', 'profFechaNacimiento', 'profFoto', 'profCMaterias']


class FormCarrera(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formCarNombre',
                'placeholder':'Ingrese el nombre de la carrera'
            }
        ),
        validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Nombre): solo se permiten letras y espacios.')
        ]
    )

    duracion = forms.CharField(        
        label="Duración",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formCarDur',
                'placeholder':'Ingrese la duración de la carrera (ej: 9 semestres)'
            }
        ),
        validators= [
            validators.RegexValidator('^[a-zA-Z0-9 ]*$', 'Error(Duracion): solo se permiten letras, numeros y espacios.')
        ]
    )
    

    materias = forms.CharField(
        label="Materias",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formCarMat',
                'placeholder':'Ingrese las materias que se darán en la carrera'
            }
        ), 
        validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Materia): solo se permiten letras y espacios.')
        ]
    )


class FormActualizarCarrera(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['carNombre', 'carDuracion', 'carMaterias']


class FormMateria(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formMatNombre',
                'placeholder':'Ingrese el nombre de la materia'
            }
        ),validators= [
            validators.RegexValidator('^[a-zA-Z0-9 ]*$', 'Error(Nombre): solo se permiten letras, numeros y espacios.')
        ]
    )

    descripcion = forms.CharField(        
        label="Descripcion",
        required=False,
        widget=forms.Textarea(
            attrs={
                'class':'formMatDesc',
                'placeholder':'Ingrese la descripción de la materia'
            }
        ),
        validators= [
            validators.RegexValidator('^[\w\sáéíóúÁÉÍÓÚüÜ,.-]*$', 'Error(Descripcion): solo se permiten letras y espacios.')
        ]
    )

    creditos = forms.IntegerField(
        label="Creditos",
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class':'formMatCred',
                'placeholder':'Ingrese la cantidad de creditos (Ej: 2)'
            }
        ), 
        validators= [
            validators.RegexValidator('^[0-9]+$', 'Error(Creditos): solo se permiten numeros.')
        ]
    )

    carrera = forms.CharField(
        label="Carrera",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formMatCar',
                'placeholder':'Ingrese el nombre de la carrera'
            }
        ),
        validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Carrera): solo se permiten letras y espacios.')
        ]
    )

    profesor = forms.CharField(
        label="Profesor",
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'formMatProf',
                'placeholder':'Ingrese el nombre del profesor que dará la materia'
            }
        ),
        validators= [
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Profesor): solo se permiten letras y espacios.')
        ]
    )


class FormActualizarMateria(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['matNombre', 'matDescripcion', 'matCreditos', 'matProfesores', 'matCarrera']