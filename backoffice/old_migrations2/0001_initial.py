# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Discipline'
        db.create_table('backoffice_discipline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('backoffice', ['Discipline'])

        # Adding model 'Designer'
        db.create_table('backoffice_designer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('birth_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('death_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('birth_country', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['backoffice.Country'], null=True)),
            ('philosophy_summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('philosophy', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('generation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Generation'])),
        ))
        db.send_create_signal('backoffice', ['Designer'])

        # Adding model 'Work'
        db.create_table('backoffice_work', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sidar_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal('backoffice', ['Work'])

        # Adding model 'Country'
        db.create_table('backoffice_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('backoffice', ['Country'])

        # Adding model 'Category'
        db.create_table('backoffice_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('backoffice', ['Category'])

        # Adding model 'Client'
        db.create_table('backoffice_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('backoffice', ['Client'])

        # Adding model 'Technique'
        db.create_table('backoffice_technique', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('backoffice', ['Technique'])

        # Adding model 'Collection'
        db.create_table('backoffice_collection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('homepage', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('backoffice', ['Collection'])

        # Adding model 'Subject'
        db.create_table('backoffice_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('backoffice', ['Subject'])

        # Adding model 'Generation'
        db.create_table('backoffice_generation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('backoffice', ['Generation'])


    def backwards(self, orm):
        # Deleting model 'Discipline'
        db.delete_table('backoffice_discipline')

        # Deleting model 'Designer'
        db.delete_table('backoffice_designer')

        # Deleting model 'Work'
        db.delete_table('backoffice_work')

        # Deleting model 'Country'
        db.delete_table('backoffice_country')

        # Deleting model 'Category'
        db.delete_table('backoffice_category')

        # Deleting model 'Client'
        db.delete_table('backoffice_client')

        # Deleting model 'Technique'
        db.delete_table('backoffice_technique')

        # Deleting model 'Collection'
        db.delete_table('backoffice_collection')

        # Deleting model 'Subject'
        db.delete_table('backoffice_subject')

        # Deleting model 'Generation'
        db.delete_table('backoffice_generation')


    models = {
        'backoffice.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Category']", 'null': 'True', 'blank': 'True'})
        },
        'backoffice.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'backoffice.collection': {
            'Meta': {'object_name': 'Collection'},
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'backoffice.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'backoffice.designer': {
            'Meta': {'object_name': 'Designer'},
            'birth_country': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['backoffice.Country']", 'null': 'True'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'death_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Generation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'philosophy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'philosophy_summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        'backoffice.discipline': {
            'Meta': {'object_name': 'Discipline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'backoffice.generation': {
            'Meta': {'object_name': 'Generation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'backoffice.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'backoffice.technique': {
            'Meta': {'object_name': 'Technique'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'backoffice.work': {
            'Meta': {'object_name': 'Work'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sidar_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        }
    }

    complete_apps = ['backoffice']