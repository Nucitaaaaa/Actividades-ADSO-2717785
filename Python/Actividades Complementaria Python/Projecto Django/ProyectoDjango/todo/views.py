from django.shortcuts import render
from .models import Tarea

# Create your views here.
def home(request):
    tareas = Tarea.objects.all()
    context = {'tareas':tareas}
    return render(request, 'todo/home.html', context)