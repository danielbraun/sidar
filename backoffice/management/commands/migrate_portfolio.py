# -*- coding: utf-8 -*-
from backoffice.models import Work, Country, Category, Discipline, Client, Technique, Collection, Designer
from django.core.management.base import BaseCommand
from django.core.files import File
from sidar.settings import PORTFOLIO_CSV_ROOT
from html2text import html2text
import os
import csv
import codecs


def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.DictReader(utf_8_encoder(unicode_csv_data),
                                dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield dict((unicode(key, 'utf-8'), unicode(value, 'utf-8')) for (key, value) in row.items())


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')


class Command(BaseCommand):
    help = "Fetch all portfolio files 26 and create rows."

    def handle(self, *args, **options):
        from django.utils import translation
        from sidar.settings import LANGUAGES
        translation.activate(LANGUAGES[0][0])
        # Build a hash table of paths for filenames
        path_hash = dict()
        for root, dirs, files in os.walk(PORTFOLIO_CSV_ROOT):
            for filename in files:
                if filename.rpartition('.')[-1] == "jpg":
                    path_hash[filename] = os.path.join(root, filename)

        for root, dirs, files in os.walk(PORTFOLIO_CSV_ROOT):
            for name in files:
                if name.rpartition('.')[-1] == "txt":
                    with codecs.open(os.path.join(root, name), encoding='utf-16-le') as f:
                        reader = unicode_csv_reader(f, delimiter='\t')
                        for row in reader:
                            Work(
                                name_he=row[u'שם העבודה'], name_en=row['Document Title'],
                                country=Country.from_portfolio(row),
                                raw_image=File(open(path_hash[row['Filename']])),
                                # subjects     = Subject.from_portfolio(row),
                                discipline=Discipline.from_portfolio(row),
                                category=Category.from_portfolio(row),
                                client=Client.from_portfolio(row),
                                technique=Technique.from_portfolio(row),
                                # collection   =  ask reuven
                                collection=Collection.objects.get_or_create(name_he=None)[0],
                                description_he=html2text(row[u'תאור']).strip(),
                                description_en=html2text(row[u'Description']).strip(),
                                # publish_date   = datetime.now(),
                                publish_date_as_text_he=row[u'תאריך'].strip(),
                                publish_date_as_text_en=row[u'Date'].strip(),
                                size_as_text_he=row[u'גודל'].strip(),
                                size_as_text_en=row[u'Size'].strip(),
                                # height         = 0.00,
                                designer=Designer.from_portfolio(row)
                                # width          = 0.00
                            ).save()

                            # for subject in Subject.from_portfolio(row):
                            # 	work.subjects.add(subject)
