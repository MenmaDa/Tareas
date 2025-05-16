from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Tarea
from .forms import TareaForm
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.

def index(request):
    return render(request, 'paginas/index.html')

def listarTareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tarea/inicio.html', {'tareas': tareas})

def crear(request):
    form = TareaForm()
    return render(request, 'tarea/crear.html', {'form': form}) 

def editar(request, id):
    tarea = Tarea.objects.get(id=id)
    form = TareaForm(instance=tarea)
    return render(request, 'tarea/editar.html', {'form': form})

def agregarTarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarea')
    else:
        form = TareaForm()
    return render(request, 'tarea/crear.html', {'form': form})

def editarTarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('tarea')
    else:
        form = TareaForm(instance=tarea)
    return render(request, 'tarea/editar.html', {'form': form, 'tarea': tarea})

def eliminarTarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tarea')
    return render(request, 'tarea/eliminar.html', {'tarea': tarea})
    