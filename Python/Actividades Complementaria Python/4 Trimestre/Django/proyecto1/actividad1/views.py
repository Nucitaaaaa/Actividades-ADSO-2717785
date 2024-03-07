
from django.shortcuts import render, HttpResponse,redirect
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist
from actividad1.models import Article
from django.db.models import Q #para que funcione or

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

def contacto(request, name='', lastName=''): 

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

    nombre = 'Maria Buenaventura'

    return render(request,'inicio.html',{
        'mi_variable': 'soy un dato que esta en la vista',
        # 'titulo':'Pagina de Inicio SENA',
        'name':nombre,
    })

# def crear_articulo(request, title, content, public):
#     articulo = Article(
#         title = title,
#         content = content,
#         public = True,
#     )

#     articulo.save()

#     return redirect('mostrarArticulos')

def crear_articulo(request):
    articulo = Article(
        title = title,
        content = content,
        public = True,
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: title:{title}, content:{content}")


def articulo_creado(request):
    return render(request, 'crearArticulo.html')


def mostrar_articulos(request):
    articulos = Article.objects.raw("SELECT * FROM actividad1_article")
    return render(request, 'articulos.html', {
        'articulos':articulos,
    })


# def modificar_articulo(request, id):
#     try:
#         articulo = Article.objects.get(id=id)
#         articulo.title = "no se xdddd"
#         articulo.public = True
#         articulo.save()

#         response = f"El articulo {articulo.id} ({articulo.title}) ha sido actualizado, su estado es {articulo.public}"
#     except:
#         response = "<strong>Articulo no encontrado</strong>"
    

#     return HttpResponse(response)

def modificar_articulo(request, title, content, id):
    try:
        # Ejecutar la consulta SQL para eliminar el artículo
        with connection.cursor() as cursor:
            cursor.execute("UPDATE actividad1_article SET title = %s, content = %s WHERE id = %s", [title, content, id])
        
        # Redirigir a la página de visualización de artículos
        return redirect('mostrarArticulos')
    
    except ObjectDoesNotExist:
        
        return HttpResponse ("<strong>Articulo no encontrado</strong>")


# def eliminar_articulo(request, id):
#     try:
#         articulo = Article.objects.get(id=id)
#         articulo.delete()
#         return redirect('mostrarArticulos')
#     except:
#         response = "<strong>Articulo no encontrado</strong>"
    
#     return HttpResponse(response)


def eliminar_articulo(request, id):
    try:
        # Ejecutar la consulta SQL para eliminar el artículo
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM actividad1_article WHERE id = %s", [id])
        
        # Redirigir a la página de visualización de artículos
        return redirect('mostrarArticulos')
    
    except ObjectDoesNotExist:

        return HttpResponse ("<strong>Articulo no encontrado</strong>")

    

    



