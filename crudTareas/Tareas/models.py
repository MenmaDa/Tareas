from django.db import models

# Create your models here.
class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    prioridad = models.CharField(max_length=10, choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')])
def __str__(self):
    fila = "Tarea: " + self.titulo + " - Descripcion: " + self.descripcion
    return fila

def delete(self, using=None, keep_parents=False):
    super().delete(using=using, keep_parents=keep_parents)