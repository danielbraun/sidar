from django.contrib import admin
from models import *

for model in [Designer, Work, Country, Discipline, Category, Client, Technique, Collection, Subject, Generation]:
	admin.site.register(model)
