from django.db import models
from tinymce.models import HTMLField


class Categoria(models.Model):
    categoria = models.CharField(max_length=200, default='')
    respostas = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.categoria

class Duvida(models.Model):
    active = models.BooleanField('Ativar Pergunta', default=False)
    categorias = models.ForeignKey(Categoria)
    autor = models.CharField(max_length= 20, default='seu nome')
    palavra_chave = models.CharField('palavra chave', max_length=65, default='palavra chave')
    titulo = models.CharField(max_length=65)
    descricao = HTMLField()
    url = models.SlugField(default='')
    pergunta = models.CharField(max_length=2000)
    resposta = models.CharField(default='responda aqui', max_length=2000)
    data = models.DateTimeField('data', auto_now_add=True, auto_now=False)
    
    def __unicode__(self):
        return self.titulo
    class Meta:
        ordering = ['categorias',]