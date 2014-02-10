# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Join.name'
        db.delete_column(u'join_join', 'name')

        # Adding field 'Join.nome'
        db.add_column(u'join_join', 'nome',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Join.sobrenome'
        db.add_column(u'join_join', 'sobrenome',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Join.name'
        db.add_column(u'join_join', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Join.nome'
        db.delete_column(u'join_join', 'nome')

        # Deleting field 'Join.sobrenome'
        db.delete_column(u'join_join', 'sobrenome')


    models = {
        u'join.join': {
            'Meta': {'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'sobrenome': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['join']