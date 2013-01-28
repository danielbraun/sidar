# -*- coding: utf-8 -*-
from django import forms

from backoffice.models import Designer, Category, Subject


class SearchForm(forms.Form):
    designer = forms.ModelChoiceField(None, label=Designer._meta.verbose_name.title())
    category = forms.ModelChoiceField(None, label=Category._meta.verbose_name.title())
    subject = forms.ModelChoiceField(None, label=Subject._meta.verbose_name.title())
    free_text = forms.CharField(label=u'חיפוש חופשי')

    def __init__(self, **kwargs):
        discipline = kwargs.pop('discipline')
        super(SearchForm, self).__init__(**kwargs)
        self.fields['designer'].queryset = Designer.objects.belonging_to_discipline(discipline, 'designer')
        self.fields['category'].queryset = Category.objects.belonging_to_discipline(discipline, 'category')
        self.fields['subject'].queryset = Subject.objects.belonging_to_discipline(discipline, 'subjects')
