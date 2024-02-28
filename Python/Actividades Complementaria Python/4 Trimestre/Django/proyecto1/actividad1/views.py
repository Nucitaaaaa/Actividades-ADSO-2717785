
from django.shortcuts import render 

#?vistas para renderizar en los templates y layout

def holaMundo (request): #Vista para retemplate 'Hola Mundo'
    return render(request, 'holamundo.html')


def saludo(request): #Vista para template 'saludo'
    return render(request, 'contacto.html', {
        'texto':'xd',
        'nombres': ['maria','pedro','juan'],
        'true' : True,
        'false' : False,
        'none' : None,
        'titulo' : 'MI PrImeRa ChamBa',
        'hacerLista' : 'Django es facil' 
    })

def contacto(request, name='', lastName=''): #Vista para template 'contacto'
    
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

    contactos = [ #Array para renderizar con el for 
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
    ]

    frameworks = {
        'react' : 'js',
        'django' : 'python',
        'laravel': 'php'
    }

    return render(request, 'contacto.html', {
        'contactos' : contactos, #se asigna a la variable contactos el array para manejarlo en el template
        'frameworks' : frameworks
    })


def inicio (request):  #Vista para template 'inicio'

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

    return render(request,'inicio.html',{
        'mi_variable': 'soy un dato que esta en la vista',
        # 'titulo':'Pagina de Inicio SENA',
        'name':nombre,
    })


