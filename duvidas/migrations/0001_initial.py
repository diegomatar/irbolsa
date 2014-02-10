# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categorias'
        db.create_table(u'duvidas_categorias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('respostas', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'duvidas', ['Categorias'])

        # Adding model 'Duvidas'
        db.create_table(u'duvidas_duvidas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categorias', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duvidas.Categorias'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('pergunta', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('resposta', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'duvidas', ['Duvidas'])


    def backwards(self, orm):
        # Deleting model 'Categorias'
        db.delete_table(u'duvidas_categorias')

        # Deleting model 'Duvidas'
        db.delete_table(u'duvidas_duvidas')


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
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'resposta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '65'})
        }
    }

    complete_apps = ['duvidas']