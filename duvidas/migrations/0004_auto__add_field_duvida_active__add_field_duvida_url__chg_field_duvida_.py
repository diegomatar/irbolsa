# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Duvida.active'
        db.add_column(u'duvidas_duvida', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Duvida.url'
        db.add_column(u'duvidas_duvida', 'url',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=50),
                      keep_default=False)


        # Changing field 'Duvida.palavra_chave'
        db.alter_column(u'duvidas_duvida', 'palavra_chave', self.gf('django.db.models.fields.CharField')(max_length=65))

    def backwards(self, orm):
        # Deleting field 'Duvida.active'
        db.delete_column(u'duvidas_duvida', 'active')

        # Deleting field 'Duvida.url'
        db.delete_column(u'duvidas_duvida', 'url')


        # Changing field 'Duvida.palavra_chave'
        db.alter_column(u'duvidas_duvida', 'palavra_chave', self.gf('django.db.models.fields.CharField')(max_length=65, null=True))

    models = {
        u'duvidas.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'categoria': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respostas': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'duvidas.duvida': {
            'Meta': {'object_name': 'Duvida'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'categorias': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['duvidas.Categoria']"}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palavra_chave': ('django.db.models.fields.CharField', [], {'default': "'palavra chave'", 'max_length': '65'}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'resposta': ('django.db.models.fields.CharField', [], {'default': "'responda aqui'", 'max_length': '2000'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'url': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['duvidas']