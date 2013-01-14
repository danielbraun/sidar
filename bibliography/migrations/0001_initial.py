# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BookCategory'
        db.create_table('bibliography_bookcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('bibliography', ['BookCategory'])

        # Adding model 'Book'
        db.create_table('bibliography_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('discipline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Discipline'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bibliography.BookCategory'])),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('author_as_text', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('publication_as_text', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('bibliography', ['Book'])


    def backwards(self, orm):
        # Deleting model 'BookCategory'
        db.delete_table('bibliography_bookcategory')

        # Deleting model 'Book'
        db.delete_table('bibliography_book')


    models = {
        'backoffice.discipline': {
            'Meta': {'ordering': "['name_he']", 'object_name': 'Discipline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'bibliography.book': {
            'Meta': {'object_name': 'Book'},
            'author_as_text': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bibliography.BookCategory']"}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Discipline']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_as_text': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'bibliography.bookcategory': {
            'Meta': {'object_name': 'BookCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['bibliography']