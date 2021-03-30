from django.urls import path

from . import views

app_name = 'menuapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'), # para redireccionar al index
    path('carta', views.carta, name='carta'),
    path('contacto', views.contacto, name='contacto'),
    path('enviar', views.enviar, name='enviar'),
]