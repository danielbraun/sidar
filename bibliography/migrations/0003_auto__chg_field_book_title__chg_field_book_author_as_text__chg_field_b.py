# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Book.title'
        db.alter_column('bibliography_book', 'title', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Book.author_as_text'
        db.alter_column('bibliography_book', 'author_as_text', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Book.comments'
        db.alter_column('bibliography_book', 'comments', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Book.publication_as_text'
        db.alter_column('bibliography_book', 'publication_as_text', self.gf('django.db.models.fields.CharField')(max_length=256))

    def backwards(self, orm):

        # Changing field 'Book.title'
        db.alter_column('bibliography_book', 'title', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Book.author_as_text'
        db.alter_column('bibliography_book', 'author_as_text', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Book.comments'
        db.alter_column('bibliography_book', 'comments', self.gf('django.db.models.fields.CharField')(max_length=128))

        # Changing field 'Book.publication_as_text'
        db.alter_column('bibliography_book', 'publication_as_text', self.gf('django.db.models.fields.CharField')(max_length=128))

    models = {
        'backoffice.discipline': {
            'Meta': {'ordering': "['name_he']", 'object_name': 'Discipline'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {}),
            'info_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'info_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'bibliography.book': {
            'Meta': {'ordering': "['title']", 'object_name': 'Book'},
            'author_as_text': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliography.BookCategory']"}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Discipline']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_as_text': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'bibliography.bookcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'BookCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['bibliography']