from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tarea', views.listarTareas, name='tarea'),
    path('tarea/agregar', views.agregarTarea, name='agregarTarea'),
    path('tarea/editar/<int:id>/', views.editarTarea, name='editarTarea'),
    path('tarea/eliminar/<int:id>/', views.eliminarTarea, name='eliminarTarea'),
]
