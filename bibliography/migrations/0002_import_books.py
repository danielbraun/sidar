# -*- coding: utf-8 -*-
from south.v2 import DataMigration

from backoffice.sidar_models import Biblio, Bibliocategory
from backoffice.utils import emptify
from sidar.settings_common import LEGACY_DB_NAMES


class Migration(DataMigration):
    depends_on = (
        ('backoffice', '0005_load_disciplines'),
    )

    def forwards(self, orm):
        for db_name in LEGACY_DB_NAMES:
            discipline = orm['backoffice.Discipline'].objects.get(name_en__startswith=db_name[4])
            for book in Biblio.objects.using(db_name).all():
                orm.Book(
                    title=book.itemname.strip(),
                    discipline=discipline,
                    category=orm.BookCategory.objects.get_or_create(
                        name=emptify(Bibliocategory.objects.using(db_name).get(pk=book.catcode).name)
                    )[0],
                    comments=emptify(book.comments).strip(),
                    author_as_text=emptify(book.author).strip(),
                    publication_as_text=emptify(book.publisher).strip()
                ).save()

    def backwards(self, orm):
        "Write your backwards methods here."

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
    symmetrical = True
