# -*- coding: utf-8 -*-
import csv
from sidar.settings import PORTFOLIO_CSV_ROOT
import codecs
import os


def remove_file_extension(filename):
    return os.path.splitext(filename)[0]


def nullify(str):
    if str == "" or str == 'eng':
        str = None
    return str


def emptify(str):
    if str is None:
        str = ""
    return str


def has_hebrew_chars(str):
    """
    >>> has_hebrew_chars(u'shdfgshjdf')
    False
    >>> has_hebrew_chars(u'sjkdfhsdjkfhצ')
    True
    """
    return any(u"\u0590" <= c <= u"\u05EA" for c in str)


def booleanize(str):
    """
    >>> booleanize("כן")
    True
    >>> booleanize("לא")
    False
    """
    if str == u"כן":
        return True
    if str == u"לא":
        return False


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


def all_portfolio_rows():
    file_count = 0
    for root, dirs, files in os.walk(PORTFOLIO_CSV_ROOT):
        for name in files:
            if name.rpartition('.')[-1] == "txt":
                with codecs.open(os.path.join(root, name), encoding='utf-16-le') as f:
                    file_count = file_count + 1
                    print ("Processing text file: %s" % os.path.join(root, name))
                    try:
                        reader = unicode_csv_reader(f, delimiter='\t')
                        for row in reader:
                            # Test if it's a valid portfolio file.
                            try:
                                row['Filename']
                            except KeyError:
                                continue
                            yield row
                    except TypeError:
                        pass
    if file_count == 0:
        raise Exception('Did not find any portfolio files. PORTFOLIO_CSV_ROOT = %s' % PORTFOLIO_CSV_ROOT.encode('utf-8'))
    print "Scanned through %s portfolio files." % file_count
