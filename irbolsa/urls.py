from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    # Examples:
    url(r'^$', 'join.views.home', name='home'),
    url(r'^obrigado$', 'join.views.obrigado', name='obrigado'),
    url(r'^sucesso$', 'join.views.sucesso', name='sucesso'),
    url(r'^afiliados$', 'join.views.afiliados', name='afiliados'),
    url(r'^oferta$', 'join.views.oferta', name='oferta'),
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^duvidas/', include('duvidas.urls')),
)
