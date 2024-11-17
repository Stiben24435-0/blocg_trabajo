from django.urls import path
from .views import lista_publicaciones, detalle_publicacion, CrearPublicacion

urlpatterns = [
    path('', lista_publicaciones, name='lista-publicaciones'),
    path('publicacion/<int:pk>/', detalle_publicacion, name='detalle-publicacion'),
    path('nueva/', CrearPublicacion.as_view(), name='nueva-publicacion'),]