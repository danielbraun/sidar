#!/bin/bash

cd /home/sidar/django_projects/sidar/
source bin/activate
exec ./manage.py run_gunicorn --user=sidar
