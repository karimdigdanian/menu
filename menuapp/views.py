from django.shortcuts import render
from django.http import HttpResponseRedirect

import environ # pylint: disable=import-error

from .models import Plato

#SendGrid Mail imports
import os
from sendgrid import SendGridAPIClient # pylint: disable=import-error
from sendgrid.helpers.mail import Mail # pylint: disable=import-error

env = environ.Env()
environ.Env.read_env()

def carta(request):
    listado = Plato.objects.all() # pylint: disable=no-member
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
    return render(request, 'menuapp/contacto.html', {})

def enviar(request):
    asunto = str(request.POST['asunto'])
    mensaje = str(request.POST['mensaje'])
    de = 'karim.lp@hotmail.com'
    para = str(env('EMAIL_DESTINO'))
    print('de:'+de)
    print('para:'+para)
    print(asunto)
    print(mensaje)
    message = Mail(
        from_email = de,
        to_emails = para,
        subject=asunto,
        html_content=mensaje
        )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
    return HttpResponseRedirect('/index')