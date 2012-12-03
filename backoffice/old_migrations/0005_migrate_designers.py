# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

from sidar.settings import LEGACY_DB_NAMES
from backoffice.utils import booleanize, emptify, nullify
from backoffice.sidar_models import Designers
from html2text import html2text


def nullify_country(name_he, orm):
    if name_he is None or name_he == "":
        return None
    else:
        return (orm.Country.objects.get_or_create(name_he=name_he))[0]


class Migration(DataMigration):
    def forwards(self, orm):
        "Write your forwards methods here."
        # Note: Remember to use orm['appname.ModelName'] rather than "from appname.models..."
        for db_name in LEGACY_DB_NAMES:
            for designer in Designers.objects.using(db_name).all():
                orm.Designer(
                    name_he=designer.namehebrew,
                    name_en=nullify(designer.nameenglish),
                    birth_country=nullify_country(designer.birthcountry, orm),
                    is_active=booleanize(designer.linkactive),
                    generation_id=designer.catcode,
                    birth_year=nullify(designer.birthyear),
                    death_year=nullify(designer.deathyear),
                    philosophy_summary_he=html2text(emptify(designer.comments).strip())
                ).save()

    def backwards(self, orm):
        for designer in orm.Designer.objects.all():
            designer.delete()

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
            'birth_country': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['backoffice.Country']", 'null': 'True'}),
            'birth_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'death_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
    symmetrical = True
