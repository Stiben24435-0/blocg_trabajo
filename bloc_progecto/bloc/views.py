from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Publicacion


def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all().order_by('-fecha_publicacion')
    return render(request, 'bloc/lista_publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)  # Cambia 'Publicacion' por 'publicacion'
    return render(request, 'bloc/detalle_publicacion.html', {'publicacion': publicacion})


   
class CrearPublicacion(CreateView):
     model = Publicacion
     fields = ['titulo', 'contenido', 'autor']
     template_name = 'bloc/formulario_publicacion.html'
     success_url = reverse_lazy('lista-publicaciones')
