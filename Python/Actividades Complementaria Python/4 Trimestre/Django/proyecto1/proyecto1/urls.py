"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
import actividad1.views #Se importan las vistas de el documento 'views.py'

urlpatterns = [
    path('admin/', admin.site.urls), 

    path('holaMundo/', actividad1.views.holaMundo, name="holaMundo"), #URL que lleva a la vista de 'Hola mundo'
    path('saludo/', actividad1.views.saludo, name="saludo"), #URL que lleva a la vista de 'Saludo'
    path('', actividad1.views.inicio, name="inicio"), #URL que lleva a la vista de 'Inicio'
    path('contacto/', actividad1.views.contacto, name="contacto"), #URL que lleva a la vista de 'Contacto'
    # path('crear_articulo/<str:title>/<str:content>/<str:public>', actividad1.views.crear_articulo, name="crearArticulo"),
    # path('mostrar_articulo/', actividad1.views.mostrar_articulo, name="mostrarArticulo"),
    path('mostrar_articulos/', actividad1.views.mostrar_articulos, name="mostrarArticulos"),
    
    path('modificar_articulo/<int:id>/<str:title>/<str:content>/', actividad1.views.modificar_articulo, name="modificarArticulo"),
    
    path('eliminar_articulo/<int:id>/', actividad1.views.eliminar_articulo, name="eliminarArticulo"),
    
    path('articulo_creado/', actividad1.views.articulo_creado, name="articuloCreado"),
    
    path('guardar_articulo/', actividad1.views.guardar_articulo, name="guardarArticulo"),
    
    path('create_full_article/', actividad1.views.create_full_article, name="createFullArticle"),
]

# path('contacto/<str:name>', actividad1.views.contacto, name="contacto"),
# path('contacto/<str:name>/<str:lastName>', actividad1.views.contacto, name="contacto"),
