from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Duvida
from .forms import DuvidaForm


def todas_duvidas(request):
    duvidas = Duvida.objects.filter(active=True)
    return render_to_response('duvidas/duvidas.html', locals(), context_instance=RequestContext(request))


def uma_duvida(request, url):
    duvida = get_object_or_404(Duvida, url=url)
    return render_to_response('duvidas/respostas.html', locals(), context_instance=RequestContext(request))


def duvida_enviada(request):
    
    return render_to_response('duvidas/enviada.html', locals(), context_instance=RequestContext(request))


def enviar_duvida(request):
    form = DuvidaForm(request.POST or None)
    if form.is_valid():
        nova_duvida = form.save(commit=False)
        nova_duvida.save()
        #send_mail('subject', 'Nome: '+ new_join.nome + '\n Email: ' + new_join.email + '\n Timestamp: ' + new_join.timestamp, str(new_join.email), ['impostoderendanabolsa@gmail.com'])
        subject = 'Nova Duvida Recebida'
        message = """
        Ola Diego,
        
        Voce recebeu uma duvida pelo site IR na bolsa.
        
        Para responde-la acesse:
        http://impostoderendanabolsa.com.br/admin
        
        Abracos,
        Diego
        """
        from_email = settings.EMAIL_HOST_USER
        to_list = [settings.EMAIL_HOST_USER]
        
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        return HttpResponseRedirect('/duvidas/duvida_enviada')
    
    return render_to_response('duvidas/enviar.html', locals(), context_instance=RequestContext(request))


