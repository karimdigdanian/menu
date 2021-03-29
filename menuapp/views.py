from django.shortcuts import render

from .models import Plato


def carta(request):
    listado = Plato.objects.all() # pylint: disable=no-member
    for plato in listado:
        if (plato.ingredientes.exists()):
            print(plato.ingredientes.all())
    entrada = listado.filter(tipo = 1)
    principal = listado.filter(tipo = 2)
    bebida = listado.filter(tipo = 3)
    postre = listado.filter(tipo = 4)
    context = {'listado' : listado,
               'entrada' : entrada,
               'principal' : principal,
               'bebida' : bebida,
               'postre' : postre}
    return render(request, 'menuapp/carta.html', context)

def index(request):
    return render(request, 'menuapp/index.html', {})

def contacto(request):
    return render(request, 'menuapp/index.html', {})