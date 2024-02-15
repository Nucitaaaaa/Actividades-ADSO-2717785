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
import actividad1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('holaMundo/', actividad1.views.holaMundo, name="holaMundo"),
    path('saludo/<int:redirigir>', actividad1.views.saludo, name="saludo"),
    path('index/', actividad1.views.index, name="saludo"),
    path('', actividad1.views.index, name="index"),
    
    path('contacto/', actividad1.views.contacto, name="contacto"),
    path('contacto/<str:name>', actividad1.views.contacto, name="contacto"),
    path('contacto/<str:name>/<str:lastName>', actividad1.views.contacto, name="contacto"),
]
