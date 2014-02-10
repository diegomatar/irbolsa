from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from .models import Join
from .forms import JoinForm



def home(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        new_join.save()
        #send_mail('subject', 'Nome: '+ new_join.nome + '\n Email: ' + new_join.email + '\n Timestamp: ' + new_join.timestamp, str(new_join.email), ['impostoderendanabolsa@gmail.com'])
        subject = 'Obrigado!'
        message = """
        Oi,
        
        Obrigado por fazer o download do primeiro capitulo do guia Imposto de Renda na Bolsa.
        
        Lembre-se de que voce pode comprar a versao completa aqui:
        http://impostoderendanabolsa.com.br
        
        Abracos,
        Diego
        """
        from_email = settings.EMAIL_HOST_USER
        to_list = [new_join.email, settings.EMAIL_HOST_USER]
        
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        return HttpResponseRedirect('/obrigado')
    
    return render_to_response('join/home.html', locals(), context_instance=RequestContext(request))


def afiliados(request):
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        new_join.save()
        #send_mail('subject', 'Nome: '+ new_join.nome + '\n Email: ' + new_join.email + '\n Timestamp: ' + new_join.timestamp, str(new_join.email), ['impostoderendanabolsa@gmail.com'])
        subject = 'Obrigado!'
        message = """
        Oi,
        
        Obrigado por fazer o download do primeiro capitulo do guia Imposto de Renda na Bolsa.
        
        Lembre-se de que voce pode comprar a versao completa aqui:
        http://impostoderendanabolsa.com.br
        
        Abracos,
        Diego
        """
        from_email = settings.EMAIL_HOST_USER
        to_list = [new_join.email, settings.EMAIL_HOST_USER]
        
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        return HttpResponseRedirect('/obrigado')
    
    return render_to_response('join/afiliados.html', locals(), context_instance=RequestContext(request))


def obrigado(request):
    return render_to_response('join/obrigado.html', locals(), context_instance=RequestContext(request))


def sucesso(request):
    return render_to_response('join/sucesso.html', locals(), context_instance=RequestContext(request))


def oferta(request):
    return render_to_response('join/oferta.html', locals(), context_instance=RequestContext(request))