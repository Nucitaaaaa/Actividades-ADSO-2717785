
from django.urls import path
import actividad1.views #Se importan las vistas de el documento 'views.py'

urlpatterns = [
    path('holaMundo/', actividad1.views.holaMundo, name="holaMundo"),
    path('saludo/', actividad1.views.saludo, name="saludo"), 
    path('', actividad1.views.inicio, name="inicio"), 
    path('contacto/', actividad1.views.contacto, name="contacto"), 
    path('mostrar_articulos/', actividad1.views.mostrar_articulos, name="mostrarArticulos"),
    path('modificar_articulo/<int:id>/<str:title>/<str:content>/', actividad1.views.modificar_articulo, name="modificarArticulo"),
    path('eliminar_articulo/<int:id>/', actividad1.views.eliminar_articulo, name="eliminarArticulo"),
    path('articulo_creado/', actividad1.views.articulo_creado, name="articuloCreado"),
    path('guardar_articulo/', actividad1.views.guardar_articulo, name="guardarArticulo"),
    path('create_full_article/', actividad1.views.create_full_article, name="createFullArticle"),
]