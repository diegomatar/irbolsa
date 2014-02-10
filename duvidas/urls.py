from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('duvidas.views',
    url(r'^$', 'todas_duvidas', name='duvidas'),
    url(r'^duvida_enviada$', 'duvida_enviada', name='duvida_enviada'),
    url(r'^enviar_duvida$', 'enviar_duvida', name='enviar_duvida'),
    url(r'^(?P<url>.*)/$', 'uma_duvida'),
)