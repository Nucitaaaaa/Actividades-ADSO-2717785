
from django.shortcuts import render, HttpResponse, redirect

def holaMundo (request):
    return render(request, 'holamundo.html')


def saludo(request, redirigir = 0):
    return render(request, 'saludo.html')

def contacto(request, name='', lastName=''):
    
    # aprendiz = ""

    # if name and lastName:
    #     aprendiz += f"""<h2>Nombre Completo: </h2>
    #                     <h3>{name} {lastName}</h3>
    #     """

    # elif name:
    #     aprendiz += f"""<h2>Nombre: </h2>
    #                     <h3>{name} </h3>
    #     """

    # elif name == '' and lastName:
    #     aprendiz += f"""<h2>Apellido: </h2>
    #                     <h3>{lastName}</h3>
    #     """    

    # else:
    #     aprendiz += 'Sin información'

    contactos = {
    '555-1234',
    '555-5678',
    '555-9012',
    '555-3456',
    '555-7890',
    '555-2345',
    '555-6789',
    '555-0123',
    '555-4567',
    '555-8901'
}

    return render(request, 'contacto.html', {
        'contactos' : contactos
    })


def index (request):

    # year = 2024
    # while year <= 2050:
    #     template += f"<li>{str(year)}"
    #     if year %2==0:
    #         template += " (año par)"
        
    #     if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    #         template += " (año bisiesto)"
    #     template+="""</li>"""
    #     year += 1

    # template += """</ul><hr>"""

    nombre = 'Maria Buenaventura'

    return render(request,'index.html',{
        'mi_variable': 'soy un dato que esta en la vista',
        'titulo':'Pagina de Inicio SENA',
        'name':nombre
    })

