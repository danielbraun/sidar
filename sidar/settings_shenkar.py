from sidar.settings_common import *

import os


DEBUG = TEMPLATE_DEBUG = False
MEDIA_ROOT = '~/media/'
PORTFOLIO_CSV_ROOT = ''
PORFOLIO_IMAGE_DIR = '/home/sidar/images_to_import/'

ALLOWED_HOSTS = ['10.0.10.4', ]

PORTFOLIO_CSV_ROOT = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sidar',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
