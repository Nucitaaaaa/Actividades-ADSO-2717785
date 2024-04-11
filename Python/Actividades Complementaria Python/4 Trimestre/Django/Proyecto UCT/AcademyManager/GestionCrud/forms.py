
from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

    carrera = forms.ModelChoiceField(
        label="Carrera",
        queryset=Carrera.objects.all(),  
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'formEstCar',
            }
        )
    )

    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'telefono', 'fechaNacimiento', 'foto', 'carrera']


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

    materias = forms.ModelMultipleChoiceField(
        label="Materias",
        queryset=Materia.objects.all(),  
        required=True, 
        widget=forms.SelectMultiple(
            attrs={
                'class': 'formProfMaterias',
            }
        )
    )

    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'telefono', 'fechaNacimiento', 'foto', 'materias']


class FormActualizarProfesor(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['profNombre', 'profApellido', 'profEmail', 'profTelefono', 'profFechaNacimiento', 'profFoto', 'profMaterias']


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

    materias = forms.ModelMultipleChoiceField(
        label="Materias",
        queryset=Materia.objects.all(),  
        required=True, 
        widget=forms.SelectMultiple(
            attrs={
                'class': 'formCarMat',
            }
        )
    )

    class Meta:
        model = Carrera
        fields = ['nombre', 'duracion', 'materias']


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
            validators.RegexValidator('^[a-zA-Z\sáéíóúüñÁÉÍÓÚÜÑ]*$', 'Error(Nombre): solo se permiten letras, numeros y espacios.')
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

    carrera = forms.ModelMultipleChoiceField(
        label="Carrera",
        queryset=Carrera.objects.all(),  
        required=True,
        widget=forms.SelectMultiple(
            attrs={
                'class': 'formMatCar',
            }
        )
    )

    profesor = forms.ModelChoiceField(
            label="Profesor",
            queryset=Profesor.objects.all(),  
            required=True,
            widget=forms.Select(
                attrs={
                    'class': 'formMatProf',
                }
            )
        )

    class Meta:
        model = Materia
        fields = ['nombre', 'descripcion', 'creditos', 'profesor', 'carrera']

class FormActualizarMateria(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['matNombre', 'matDescripcion', 'matCreditos', 'matProfesores', 'matCarrera']


class FormRegistro(UserCreationForm):
    class Meta:
        model = User
        fields=['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
