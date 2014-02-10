# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Categorias'
        db.delete_table(u'duvidas_categorias')

        # Deleting model 'Duvidas'
        db.delete_table(u'duvidas_duvidas')

        # Adding model 'Categoria'
        db.create_table(u'duvidas_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('respostas', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'duvidas', ['Categoria'])

        # Adding model 'Duvida'
        db.create_table(u'duvidas_duvida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('categorias', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duvidas.Categoria'])),
            ('palavra_chave', self.gf('django.db.models.fields.CharField')(default='palavra', max_length=65, null=True, blank=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('pergunta', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('resposta', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'duvidas', ['Duvida'])


    def backwards(self, orm):
        # Adding model 'Categorias'
        db.create_table(u'duvidas_categorias', (
            ('categoria', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('respostas', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'duvidas', ['Categorias'])

        # Adding model 'Duvidas'
        db.create_table(u'duvidas_duvidas', (
            ('palavra_chave', self.gf('django.db.models.fields.CharField')(default='palavra', max_length=65)),
            ('categorias', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['duvidas.Categorias'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('resposta', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('pergunta', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('data', self.gf('django.db.models.fields.DateTimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('descricao', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'duvidas', ['Duvidas'])

        # Deleting model 'Categoria'
        db.delete_table(u'duvidas_categoria')

        # Deleting model 'Duvida'
        db.delete_table(u'duvidas_duvida')


    models = {
        u'duvidas.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'categoria': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respostas': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'duvidas.duvida': {
            'Meta': {'object_name': 'Duvida'},
            'categorias': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['duvidas.Categoria']"}),
            'data': ('django.db.models.fields.DateTimeField', [], {}),
            'descricao': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'palavra_chave': ('django.db.models.fields.CharField', [], {'default': "'palavra'", 'max_length': '65', 'null': 'True', 'blank': 'True'}),
            'pergunta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'resposta': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '65'})
        }
    }

    complete_apps = ['duvidas']