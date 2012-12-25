# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Keyword.name'
        db.alter_column('backoffice_keyword', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Keyword.name_ar'
        db.alter_column('backoffice_keyword', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Keyword.name_en'
        db.alter_column('backoffice_keyword', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Keyword.name_he'
        db.alter_column('backoffice_keyword', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Designer.name'
        db.alter_column('backoffice_designer', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Designer.name_ar'
        db.alter_column('backoffice_designer', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Designer.name_he'
        db.alter_column('backoffice_designer', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Designer.name_en'
        db.alter_column('backoffice_designer', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Technique.name'
        db.alter_column('backoffice_technique', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Technique.name_ar'
        db.alter_column('backoffice_technique', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Technique.name_en'
        db.alter_column('backoffice_technique', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Technique.name_he'
        db.alter_column('backoffice_technique', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Generation.name'
        db.alter_column('backoffice_generation', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Generation.name_ar'
        db.alter_column('backoffice_generation', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Generation.name_en'
        db.alter_column('backoffice_generation', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Generation.name_he'
        db.alter_column('backoffice_generation', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Client.name'
        db.alter_column('backoffice_client', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Client.name_ar'
        db.alter_column('backoffice_client', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Client.name_en'
        db.alter_column('backoffice_client', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Client.name_he'
        db.alter_column('backoffice_client', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Work.name_ar'
        db.alter_column('backoffice_work', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Work.name_en'
        db.alter_column('backoffice_work', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Work.name'
        db.alter_column('backoffice_work', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Work.name_he'
        db.alter_column('backoffice_work', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Discipline.name'
        db.alter_column('backoffice_discipline', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Discipline.name_ar'
        db.alter_column('backoffice_discipline', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Discipline.name_en'
        db.alter_column('backoffice_discipline', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Discipline.name_he'
        db.alter_column('backoffice_discipline', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Subject.name'
        db.alter_column('backoffice_subject', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Subject.name_ar'
        db.alter_column('backoffice_subject', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Subject.name_en'
        db.alter_column('backoffice_subject', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Subject.name_he'
        db.alter_column('backoffice_subject', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Category.name'
        db.alter_column('backoffice_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Category.name_ar'
        db.alter_column('backoffice_category', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Category.name_he'
        db.alter_column('backoffice_category', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Category.name_en'
        db.alter_column('backoffice_category', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Country.name'
        db.alter_column('backoffice_country', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Country.name_ar'
        db.alter_column('backoffice_country', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Country.name_en'
        db.alter_column('backoffice_country', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Country.name_he'
        db.alter_column('backoffice_country', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Collection.name'
        db.alter_column('backoffice_collection', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Collection.name_ar'
        db.alter_column('backoffice_collection', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Collection.name_he'
        db.alter_column('backoffice_collection', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Collection.name_en'
        db.alter_column('backoffice_collection', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # Changing field 'Keyword.name'
        db.alter_column('backoffice_keyword', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Keyword.name_ar'
        db.alter_column('backoffice_keyword', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Keyword.name_en'
        db.alter_column('backoffice_keyword', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Keyword.name_he'
        db.alter_column('backoffice_keyword', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Designer.name'
        db.alter_column('backoffice_designer', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Designer.name_ar'
        db.alter_column('backoffice_designer', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Designer.name_he'
        db.alter_column('backoffice_designer', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Designer.name_en'
        db.alter_column('backoffice_designer', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Technique.name'
        db.alter_column('backoffice_technique', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Technique.name_ar'
        db.alter_column('backoffice_technique', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Technique.name_en'
        db.alter_column('backoffice_technique', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Technique.name_he'
        db.alter_column('backoffice_technique', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Generation.name'
        db.alter_column('backoffice_generation', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Generation.name_ar'
        db.alter_column('backoffice_generation', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Generation.name_en'
        db.alter_column('backoffice_generation', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Generation.name_he'
        db.alter_column('backoffice_generation', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Client.name'
        db.alter_column('backoffice_client', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Client.name_ar'
        db.alter_column('backoffice_client', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Client.name_en'
        db.alter_column('backoffice_client', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Client.name_he'
        db.alter_column('backoffice_client', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Work.name_ar'
        db.alter_column('backoffice_work', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Work.name_en'
        db.alter_column('backoffice_work', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Work.name'
        db.alter_column('backoffice_work', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Work.name_he'
        db.alter_column('backoffice_work', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Discipline.name'
        db.alter_column('backoffice_discipline', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Discipline.name_ar'
        db.alter_column('backoffice_discipline', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Discipline.name_en'
        db.alter_column('backoffice_discipline', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Discipline.name_he'
        db.alter_column('backoffice_discipline', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Subject.name'
        db.alter_column('backoffice_subject', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Subject.name_ar'
        db.alter_column('backoffice_subject', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Subject.name_en'
        db.alter_column('backoffice_subject', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Subject.name_he'
        db.alter_column('backoffice_subject', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Category.name'
        db.alter_column('backoffice_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Category.name_ar'
        db.alter_column('backoffice_category', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Category.name_he'
        db.alter_column('backoffice_category', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Category.name_en'
        db.alter_column('backoffice_category', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Country.name'
        db.alter_column('backoffice_country', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Country.name_ar'
        db.alter_column('backoffice_country', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Country.name_en'
        db.alter_column('backoffice_country', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Country.name_he'
        db.alter_column('backoffice_country', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Collection.name'
        db.alter_column('backoffice_collection', 'name', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Collection.name_ar'
        db.alter_column('backoffice_collection', 'name_ar', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Collection.name_he'
        db.alter_column('backoffice_collection', 'name_he', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Collection.name_en'
        db.alter_column('backoffice_collection', 'name_en', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    models = {
        'backoffice.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Category']", 'null': 'True', 'blank': 'True'})
        },
        'backoffice.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.collection': {
            'Meta': {'object_name': 'Collection'},
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.designer': {
            'Meta': {'object_name': 'Designer'},
            'birth_country': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['backoffice.Country']", 'null': 'True'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'death_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'generation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Generation']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.generation': {
            'Meta': {'object_name': 'Generation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.keyword': {
            'Meta': {'object_name': 'Keyword'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.technique': {
            'Meta': {'object_name': 'Technique'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.work': {
            'Meta': {'object_name': 'Work'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Category']", 'null': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Client']", 'null': 'True'}),
            'collections': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backoffice.Collection']", 'symmetrical': 'False'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Country']", 'null': 'True', 'blank': 'True'}),
            'date_accuracy_level': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '2', 'blank': 'True'}),
            'depth': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Designer']", 'null': 'True'}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Discipline']", 'null': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backoffice.Keyword']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'publish_date_as_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'raw_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'sidar_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'size_as_text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backoffice.Subject']", 'null': 'True', 'symmetrical': 'False'}),
            'techniques': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backoffice.Technique']", 'symmetrical': 'False'}),
            'width': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['backoffice']