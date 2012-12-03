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
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('backoffice', ['Discipline'])

        # Adding model 'Designer'
        db.create_table('backoffice_designer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('birth_year', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('death_year', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('birth_country', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['backoffice.Country'])),
            ('philosophy_summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('philosophy_summary_he', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('philosophy_summary_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('philosophy_summary_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('philosophy', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('generation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Generation'])),
        ))
        db.send_create_signal('backoffice', ['Designer'])

        # Adding model 'Work'
        db.create_table('backoffice_work', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('designer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Designer'], null=True)),
            ('raw_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Discipline'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Category'])),
            ('publish_date_as_text', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('publish_date_as_text_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('publish_date_as_text_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('publish_date_as_text_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Client'])),
            ('technique', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Technique'])),
            ('size_as_text', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('size_as_text_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('size_as_text_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('size_as_text_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('description_he', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_ar', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
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
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('backoffice', ['Country'])

        # Adding model 'Category'
        db.create_table('backoffice_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Category'], null=True, blank=True)),
        ))
        db.send_create_signal('backoffice', ['Category'])

        # Adding model 'Client'
        db.create_table('backoffice_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('backoffice', ['Client'])

        # Adding model 'Technique'
        db.create_table('backoffice_technique', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('backoffice', ['Technique'])

        # Adding model 'Collection'
        db.create_table('backoffice_collection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('homepage', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('backoffice', ['Collection'])

        # Adding model 'Subject'
        db.create_table('backoffice_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('backoffice', ['Subject'])

        # Adding model 'Generation'
        db.create_table('backoffice_generation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
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
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Category']", 'null': 'True', 'blank': 'True'})
        },
        'backoffice.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.collection': {
            'Meta': {'object_name': 'Collection'},
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.designer': {
            'Meta': {'object_name': 'Designer'},
            'birth_country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['backoffice.Country']"}),
            'birth_year': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'death_year': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Generation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'philosophy': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'philosophy_summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'philosophy_summary_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'philosophy_summary_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'philosophy_summary_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        'backoffice.discipline': {
            'Meta': {'object_name': 'Discipline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.generation': {
            'Meta': {'object_name': 'Generation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.technique': {
            'Meta': {'object_name': 'Technique'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.work': {
            'Meta': {'object_name': 'Work'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Category']"}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Client']"}),
            'collection': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Collection']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Country']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Designer']", 'null': 'True'}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Discipline']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'publish_date_as_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'publish_date_as_text_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'publish_date_as_text_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'publish_date_as_text_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'raw_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'size_as_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'size_as_text_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'size_as_text_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'size_as_text_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backoffice.Subject']", 'symmetrical': 'False'}),
            'technique': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Technique']"})
        }
    }

    complete_apps = ['backoffice']