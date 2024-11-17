from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.CharField(max_length=100, default="Anónimo")
    fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self): 
        return self.titulo