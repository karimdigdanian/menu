from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

import environ # pylint: disable=import-error

from .models import Plato

#SendGrid imports
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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
    message = Mail(
    from_email='karim.lp@hotmail.com',
    to_emails='kardigda@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
    return HttpResponseRedirect('/carta')


def enviar2(request):
    print("def enviar")
    asunto = request.POST['asunto']
    de = request.POST['de']
    mensaje = request.POST['mensaje']
    send_mail(
        asunto,
        mensaje,
        de,
        [env('EMAIL_DESTINO')],
    )
    print("envio")
    
    return HttpResponseRedirect('/carta/')
    #return render(request, 'menuapp/index.html', {})
    