
from django.shortcuts import render, HttpResponse, redirect

def holaMundo (request):
    return render(request, 'holamundo.html')


def saludo(request, redirigir = 0):
    return render(request, 'saludo.html')

def contacto(request, name='', lastName=''):
    aprendiz = ""

    if name and lastName:
        aprendiz += f"""<h2>Nombre Completo: </h2>
                        <h3>{name} {lastName}</h3>
        """

    elif name:
        aprendiz += f"""<h2>Nombre: </h2>
                        <h3>{name} </h3>
        """

    elif name == '' and lastName:
        aprendiz += f"""<h2>Apellido: </h2>
                        <h3>{lastName}</h3>
        """    

    else:
        aprendiz += 'Sin información'

    return render(request, 'contacto.html')


def index (request):
    return render(request, 'layout.html')

