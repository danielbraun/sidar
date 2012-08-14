# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Designer.name_ar'
        db.delete_column('backoffice_designer', 'name_ar')

        # Deleting field 'Designer.name_en'
        db.delete_column('backoffice_designer', 'name_en')

        # Deleting field 'Designer.name_he'
        db.delete_column('backoffice_designer', 'name_he')

        # Adding field 'Technique.name_he'
        db.add_column('backoffice_technique', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Technique.name_en'
        db.add_column('backoffice_technique', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Technique.name_ar'
        db.add_column('backoffice_technique', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Generation.name_he'
        db.add_column('backoffice_generation', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Generation.name_en'
        db.add_column('backoffice_generation', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Generation.name_ar'
        db.add_column('backoffice_generation', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Client.name_he'
        db.add_column('backoffice_client', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Client.name_en'
        db.add_column('backoffice_client', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Client.name_ar'
        db.add_column('backoffice_client', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Work.name_he'
        db.add_column('backoffice_work', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Work.name_en'
        db.add_column('backoffice_work', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Work.name_ar'
        db.add_column('backoffice_work', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Discipline.name_he'
        db.add_column('backoffice_discipline', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Discipline.name_en'
        db.add_column('backoffice_discipline', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Discipline.name_ar'
        db.add_column('backoffice_discipline', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.name_he'
        db.add_column('backoffice_subject', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.name_en'
        db.add_column('backoffice_subject', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subject.name_ar'
        db.add_column('backoffice_subject', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.name_he'
        db.add_column('backoffice_category', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.name_en'
        db.add_column('backoffice_category', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Category.name_ar'
        db.add_column('backoffice_category', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.name_he'
        db.add_column('backoffice_country', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.name_en'
        db.add_column('backoffice_country', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.name_ar'
        db.add_column('backoffice_country', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.name_he'
        db.add_column('backoffice_collection', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.name_en'
        db.add_column('backoffice_collection', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.name_ar'
        db.add_column('backoffice_collection', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Designer.name_ar'
        db.add_column('backoffice_designer', 'name_ar',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Designer.name_en'
        db.add_column('backoffice_designer', 'name_en',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Designer.name_he'
        db.add_column('backoffice_designer', 'name_he',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Technique.name_he'
        db.delete_column('backoffice_technique', 'name_he')

        # Deleting field 'Technique.name_en'
        db.delete_column('backoffice_technique', 'name_en')

        # Deleting field 'Technique.name_ar'
        db.delete_column('backoffice_technique', 'name_ar')

        # Deleting field 'Generation.name_he'
        db.delete_column('backoffice_generation', 'name_he')

        # Deleting field 'Generation.name_en'
        db.delete_column('backoffice_generation', 'name_en')

        # Deleting field 'Generation.name_ar'
        db.delete_column('backoffice_generation', 'name_ar')

        # Deleting field 'Client.name_he'
        db.delete_column('backoffice_client', 'name_he')

        # Deleting field 'Client.name_en'
        db.delete_column('backoffice_client', 'name_en')

        # Deleting field 'Client.name_ar'
        db.delete_column('backoffice_client', 'name_ar')

        # Deleting field 'Work.name_he'
        db.delete_column('backoffice_work', 'name_he')

        # Deleting field 'Work.name_en'
        db.delete_column('backoffice_work', 'name_en')

        # Deleting field 'Work.name_ar'
        db.delete_column('backoffice_work', 'name_ar')

        # Deleting field 'Discipline.name_he'
        db.delete_column('backoffice_discipline', 'name_he')

        # Deleting field 'Discipline.name_en'
        db.delete_column('backoffice_discipline', 'name_en')

        # Deleting field 'Discipline.name_ar'
        db.delete_column('backoffice_discipline', 'name_ar')

        # Deleting field 'Subject.name_he'
        db.delete_column('backoffice_subject', 'name_he')

        # Deleting field 'Subject.name_en'
        db.delete_column('backoffice_subject', 'name_en')

        # Deleting field 'Subject.name_ar'
        db.delete_column('backoffice_subject', 'name_ar')

        # Deleting field 'Category.name_he'
        db.delete_column('backoffice_category', 'name_he')

        # Deleting field 'Category.name_en'
        db.delete_column('backoffice_category', 'name_en')

        # Deleting field 'Category.name_ar'
        db.delete_column('backoffice_category', 'name_ar')

        # Deleting field 'Country.name_he'
        db.delete_column('backoffice_country', 'name_he')

        # Deleting field 'Country.name_en'
        db.delete_column('backoffice_country', 'name_en')

        # Deleting field 'Country.name_ar'
        db.delete_column('backoffice_country', 'name_ar')

        # Deleting field 'Collection.name_he'
        db.delete_column('backoffice_collection', 'name_he')

        # Deleting field 'Collection.name_en'
        db.delete_column('backoffice_collection', 'name_en')

        # Deleting field 'Collection.name_ar'
        db.delete_column('backoffice_collection', 'name_ar')


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
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Discipline']"}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'raw_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backoffice.Subject']", 'symmetrical': 'False'}),
            'technique': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Technique']"}),
            'width': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['backoffice']