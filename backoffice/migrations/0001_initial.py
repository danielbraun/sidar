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
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('death_date', self.gf('django.db.models.fields.DateField')()),
            ('birth_country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Country'])),
            ('philosophy', self.gf('django.db.models.fields.TextField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('generation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Generation'])),
        ))
        db.send_create_signal('backoffice', ['Designer'])

        # Adding model 'Work'
        db.create_table('backoffice_work', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('raw_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Discipline'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Category'])),
            ('publish_date', self.gf('django.db.models.fields.DateField')()),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Client'])),
            ('technique', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Technique'])),
            ('height', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('width', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Country'])),
            ('collection', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Collection'])),
        ))
        db.send_create_signal('backoffice', ['Work'])

        # Adding M2M table for field subjects on 'Work'
        db.create_table('backoffice_work_subjects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('work', models.ForeignKey(orm['backoffice.work'], null=False)),
            ('subject', models.ForeignKey(orm['backoffice.subject'], null=False))
        ))
        db.create_unique('backoffice_work_subjects', ['work_id', 'subject_id'])

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

        # Removing M2M table for field subjects on 'Work'
        db.delete_table('backoffice_work_subjects')

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
            'birth_country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Country']"}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'generation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Generation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'philosophy': ('django.db.models.fields.TextField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Category']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Client']"}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Collection']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Discipline']"}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'raw_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backoffice.Subject']", 'symmetrical': 'False'}),
            'technique': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Technique']"}),
            'width': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['backoffice']