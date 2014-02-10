# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Duvida.data'
        db.alter_column(u'duvidas_duvida', 'data', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Duvida.descricao'
        db.alter_column(u'duvidas_duvida', 'descricao', self.gf('django.db.models.fields.TextField')(max_length=150))

    def backwards(self, orm):

        # Changing field 'Duvida.data'
        db.alter_column(u'duvidas_duvida', 'data', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Duvida.descricao'
        db.alter_column(u'duvidas_duvida', 'descricao', self.gf('django.db.models.fields.CharField')(max_length=150))

    models = {
        u'duvidas.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'categoria': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respostas': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'duvidas.duvida': {
            'Meta': {'ordering': "['categorias']", 'object_name': 'Duvida'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autor': ('django.db.models.fields.CharField', [], {'default': "'seu nome'", 'max_length': '20'}),
            'categorias': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['duvidas.Categoria']"}),
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palavra_chave': ('django.db.models.fields.CharField', [], {'default': "'palavra chave'", 'max_length': '65'}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'resposta': ('django.db.models.fields.CharField', [], {'default': "'responda aqui'", 'max_length': '2000'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'url': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['duvidas']