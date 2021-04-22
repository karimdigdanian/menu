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
    asunto = request.POST['asunto']
    de = str(request.POST['de'])
    mensaje = request.POST['mensaje']
    para = str(env('EMAIL_HOST_USER'))
    message = Mail(
        from_email = de,
        to_emails = para,
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>'
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