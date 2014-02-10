from django.contrib import admin
from .models import Categoria, Duvida


class CategoriaAdmin(admin.ModelAdmin):
    class Meta:
        model = Categoria
        
    list_display = ('categoria', 'respostas')
    search_fields = ['categoria']

admin.site.register(Categoria, CategoriaAdmin)


class DuvidaAdmin(admin.ModelAdmin):
    class Meta:
        model = Duvida
    list_display = ('titulo', 'palavra_chave', 'active', 'categorias', 'data')
    search_fields = ['titulo']
    fieldsets = [
        (None,               {'fields': ['active']}),
        ('Duvida', {'fields': ['titulo', 'pergunta', 'resposta', 'autor', 'categorias']}),
        ('SEO', {'fields': ['palavra_chave', 'descricao', 'url']}),
    ]

admin.site.register(Duvida, DuvidaAdmin)