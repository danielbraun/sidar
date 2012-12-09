# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Work.designer'
        db.add_column('backoffice_work', 'designer',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backoffice.Designer'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Work.designer'
        db.delete_column('backoffice_work', 'designer_id')


    models = {
        'backoffice.archives': {
            'Meta': {'object_name': 'Archives', 'db_table': "u'archives'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Address'", 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {}),
            'catcode': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'itemName'"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Phone'", 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.archivescategory': {
            'Meta': {'object_name': 'Archivescategory', 'db_table': "u'archivescategory'", 'managed': 'False'},
            'bgcolor': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'birthcountry': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'birthCountry'", 'blank': 'True'}),
            'birthyear': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'birthYear'", 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'collectorcode': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'collectorCode'", 'blank': 'True'}),
            'deathyear': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'deathYear'", 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'educator': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'exprtcode': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'linkactive': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'nameenglish': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameEnglish'", 'blank': 'True'}),
            'namehebrew': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameHebrew'"})
        },
        'backoffice.articles': {
            'Meta': {'object_name': 'Articles', 'db_table': "u'articles'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filenames': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'filenames1': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'itemName'"}),
            'source': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        'backoffice.articlescategory': {
            'Meta': {'object_name': 'Articlescategory', 'db_table': "u'articlescategory'", 'managed': 'False'},
            'bgcolor': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'sub': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.biblio': {
            'Meta': {'object_name': 'Biblio', 'db_table': "u'biblio'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'itemName'"}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.bibliocategory': {
            'Meta': {'object_name': 'Bibliocategory', 'db_table': "u'bibliocategory'", 'managed': 'False'},
            'bgcolor': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'sub': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.categories': {
            'Meta': {'object_name': 'Categories', 'db_table': "u'categories'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {}),
            'catcode': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkactive': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'linkname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'nameenglish': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameEnglish'", 'blank': 'True'}),
            'namehebrew': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameHebrew'"}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.categoriescategory': {
            'Meta': {'object_name': 'Categoriescategory', 'db_table': "u'categoriescategory'", 'managed': 'False'},
            'bgcolor': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'nameenglish': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameEnglish'"}),
            'namehebrew': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameHebrew'", 'blank': 'True'}),
            'sub': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
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
            'birth_country': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['backoffice.Country']", 'null': 'True'}),
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
        'backoffice.designers': {
            'Meta': {'object_name': 'Designers', 'db_table': "u'designers'", 'managed': 'False'},
            'artid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'birthcountry': ('django.db.models.fields.CharField', [], {'max_length': '75', 'db_column': "'birthCountry'", 'blank': 'True'}),
            'birthyear': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'birthYear'", 'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'commentsbrief': ('django.db.models.fields.TextField', [], {'db_column': "'CommentsBrief'", 'blank': 'True'}),
            'deathyear': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_column': "'deathYear'", 'blank': 'True'}),
            'designercode': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'designerCode'", 'blank': 'True'}),
            'linkactive': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'nameenglish': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameEnglish'", 'blank': 'True'}),
            'namehebrew': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameHebrew'"}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.designerscategory': {
            'Meta': {'object_name': 'Designerscategory', 'db_table': "u'designerscategory'", 'managed': 'False'},
            'catcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'})
        },
        'backoffice.discipline': {
            'Meta': {'object_name': 'Discipline'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.events': {
            'Meta': {'object_name': 'Events', 'db_table': "u'events'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'eventcontents': ('django.db.models.fields.TextField', [], {'db_column': "'eventContents'", 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subcontents1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subcontents2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subcontents3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subcontents4': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'subtitle1': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'subTitle1'"}),
            'subtitle2': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'subTitle2'", 'blank': 'True'}),
            'subtitle3': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'subTitle3'", 'blank': 'True'}),
            'subtitle4': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'subTitle4'", 'blank': 'True'})
        },
        'backoffice.generation': {
            'Meta': {'object_name': 'Generation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.links': {
            'Meta': {'object_name': 'Links', 'db_table': "u'links'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {}),
            'catcode': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'itemName'"}),
            'itemurl': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'sitelanguage': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.linkscategory': {
            'Meta': {'object_name': 'Linkscategory', 'db_table': "u'linkscategory'", 'managed': 'False'},
            'bgcolor': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'sub': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.movies': {
            'Meta': {'object_name': 'Movies', 'db_table': "u'movies'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {}),
            'catcode': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filenames': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'itemName'"}),
            'movielength': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'movieLength'", 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.moviescategory': {
            'Meta': {'object_name': 'Moviescategory', 'db_table': "u'moviescategory'", 'managed': 'False'},
            'bgcolor': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'sub': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.pages': {
            'Meta': {'object_name': 'Pages', 'db_table': "u'pages'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'itemname': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'itemName'"}),
            'pagecontents': ('django.db.models.fields.TextField', [], {'db_column': "'pageContents'", 'blank': 'True'}),
            'pagelink': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'pagetitle': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'pageTitle'", 'blank': 'True'})
        },
        'backoffice.sidaritems': {
            'Meta': {'object_name': 'SidarItems', 'db_table': "u'sidar_items'", 'managed': 'False'},
            'category_he': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'client': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Client'", 'blank': 'True'}),
            'client_he': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'collection_he': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Country'", 'blank': 'True'}),
            'country_he': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'Description'", 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'designer': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Designer'", 'blank': 'True'}),
            'designer_he': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'designercode': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'DesignerCode'", 'blank': 'True'}),
            'document_title': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Document Title'", 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Filename'", 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True', 'db_column': "'ID'"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Path'", 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Size'", 'blank': 'True'}),
            'size_he': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'subject_he': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'technique': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Technique'", 'blank': 'True'}),
            'technique_he': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'title_he': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'Topic'", 'blank': 'True'})
        },
        'backoffice.studiorelate': {
            'Meta': {'object_name': 'Studiorelate', 'db_table': "u'studiorelate'", 'managed': 'False'},
            'designer': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'relates': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'})
        },
        'backoffice.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.subjects': {
            'Meta': {'object_name': 'Subjects', 'db_table': "u'subjects'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {}),
            'catcode': ('django.db.models.fields.IntegerField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkactive': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'nameenglish': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameEnglish'", 'blank': 'True'}),
            'namehebrew': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameHebrew'"}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.subjectscategory': {
            'Meta': {'object_name': 'Subjectscategory', 'db_table': "u'subjectscategory'", 'managed': 'False'},
            'bgcolor': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'catcode': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '765', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'sub': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.technique': {
            'Meta': {'object_name': 'Technique'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'backoffice.timeline': {
            'Meta': {'object_name': 'Timeline', 'db_table': "u'timeline'", 'managed': 'False'},
            'added': ('django.db.models.fields.DateTimeField', [], {}),
            'addedby': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'artid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'db_column': "'Comments'", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'designers': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'designers_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'events': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'extra': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'linkactive': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'nameenglish': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameEnglish'", 'blank': 'True'}),
            'namehebrew': ('django.db.models.fields.CharField', [], {'max_length': '765', 'db_column': "'nameHebrew'"}),
            'status': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timewords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'yearend': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'yearstart': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'backoffice.users': {
            'Meta': {'object_name': 'Users', 'db_table': "u'users'", 'managed': 'False'},
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'privilages': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'userid': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        'backoffice.work': {
            'Meta': {'object_name': 'Work'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Country']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'description_ar': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_he': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Designer']", 'null': 'True'}),
            'discipline': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backoffice.Discipline']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_ar': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'name_he': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'raw_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'sidar_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['backoffice']