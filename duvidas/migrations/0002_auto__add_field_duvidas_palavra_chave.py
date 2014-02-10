# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Duvidas.palavra_chave'
        db.add_column(u'duvidas_duvidas', 'palavra_chave',
                      self.gf('django.db.models.fields.CharField')(default='palavra', max_length=65),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Duvidas.palavra_chave'
        db.delete_column(u'duvidas_duvidas', 'palavra_chave')


    models = {
        u'duvidas.categorias': {
            'Meta': {'object_name': 'Categorias'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respostas': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'duvidas.duvidas': {
            'Meta': {'object_name': 'Duvidas'},
            'categorias': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['duvidas.Categorias']"}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palavra_chave': ('django.db.models.fields.CharField', [], {'default': "'palavra'", 'max_length': '65'}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'resposta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '65'})
        }
    }

    complete_apps = ['duvidas']