# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from backoffice.forms import SearchForm
from backoffice.models import Designer, Discipline, Work, Generation

from backoffice.models import Subject

from backoffice.models import Category

from django.views.generic.base import View


class DisciplineMixin(object):
    def dispatch(self, *args, **kwargs):
        self.discipline = get_object_or_404(Discipline, pk=kwargs['discipline'], active=True)
        return super(DisciplineMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DisciplineMixin, self).get_context_data(**kwargs)
        context['discipline'] = self.discipline
        return context


class WorkListView(DisciplineMixin, ListView):
    paginate_by = 10

    def get_queryset(self):
        works = Work.objects.filter(discipline=self.discipline)
        filters = self.kwargs

        self.designer = filters.get('designer')
        self.subject = filters.get('subject')
        self.category = filters.get('category')
        self.from_year = filters.get('from')
        self.until_year = filters.get('until')
        self.year = filters.get('year')

        if self.designer:
            self.designer = get_object_or_404(Designer, pk=self.designer)
            self.designer.available_categories = self.designer.available_categories_by_discipline(self.discipline)
            works = works.filter(designer=self.designer)

        if self.subject:
            self.subject = get_object_or_404(Subject, pk=self.subject)
            self.subject.available_designers = self.subject.designers_by_discipline(self.discipline.id)
            works = works.filter(subjects=self.subject)

        if self.category:
            self.category = get_object_or_404(Category, pk=self.category)
            self.category.available_designers = self.category.designers_by_discipline(self.discipline.id)
            works = works.filter(category=self.category)

        if self.from_year:
            works = works.filter(publish_year__gte=self.from_year)

        if self.until_year:
            works = works.filter(publish_year__lte=self.until_year)

        if self.until_year or self.from_year:
            self.available_years = works.values_list('publish_year', flat=True).distinct().order_by('publish_year')

        if self.year:
            works = works.filter(publish_year=self.year)
            self.year = int(self.year)

        return works.order_by('id')

    def get_context_data(self, **kwargs):
        context = super(WorkListView, self).get_context_data(**kwargs)
        context['main_filter'] = self.kwargs.get('main_filter')
        context['designer'] = self.designer
        context['category'] = self.category
        context['subject'] = self.subject
        context['from'] = self.from_year
        context['until'] = self.until_year
        context['year'] = self.year
        if context['main_filter'] in ['from', 'until', 'year']:
            context['main_filter'] = 'years'
            context['available_years'] = self.available_years
        self.work = self.kwargs.get('work')
        if self.work:
            self.template_name = 'backoffice/work_detail.html'
            self.work = get_object_or_404(self.get_queryset(), pk=self.work)
            context['work'] = self.work
            qs = self.get_queryset().filter(id__gt=self.work.id)
            if qs:
                context['next_work'] = qs[0]
            qs = self.get_queryset().filter(id__lt=self.work.id).order_by('-id')
            if qs:
                context['previous_work'] = qs[0]
        return context


class WorkDetailView(DisciplineMixin, DetailView):
    model = Work


class DesignerListView(DisciplineMixin, ListView):
    template_name = 'backoffice/designer_list.html'

    letter_groups = (
        ('א',),
        ('ב', 'ג', 'ד'),
        ('ה', 'ו'),
        ('ז', 'ח', 'ט'),
        ('י', 'כ', 'ל'),
        ('מ', 'נ'),
        ('ס', 'ע'),
        ('פ',),
        ('צ', 'ק'),
        ('ר',),
        ('ש', 'ת')
    )

    def get_context_data(self, **kwargs):
        context = super(DesignerListView, self).get_context_data(**kwargs)
        context['generations'] = Generation.objects.all()
        return context

    def get_queryset(self):
        object_list = []
        for group in self.letter_groups:
            object_list.append({
                'letters': group,
                'designer_groups': [Designer.objects.belonging_to_discipline(self.discipline, 'designer').filter(name_he__startswith=unicode(letter, 'utf-8')).exclude(generation=None) for letter in group]
            })
        return object_list


class DisciplineTemplateView(DisciplineMixin, TemplateView):
    pass


class WorkFieldListViewByDiscipline(DisciplineMixin, ListView):
    def get_queryset(self):
        return self.model.objects.belonging_to_discipline(self.discipline, self.kwargs['work_field']).order_by('parent', 'name_he').exclude(parent=None)


class DisciplineSearchView(DisciplineMixin, FormView):
    form_class = SearchForm
    template_name = 'search.html'

    def get_form_kwargs(self):
        kwargs = super(DisciplineSearchView, self).get_form_kwargs()
        kwargs['discipline'] = self.discipline
        return kwargs


class SearchView(DisciplineMixin, TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data()
        context['form'] = SearchForm(discipline=self.discipline)
        if self.request.GET:
            return WorkListView.as_view()(self.request, discipline=self.discipline.id)
        else:
            self.template_name = "search.html"
        # WorkListView.as_view()
        return context


class DesignerDetailView(DisciplineMixin, DetailView):
    model = Designer

    def get_context_data(self, **kwargs):
        context = super(DesignerDetailView, self).get_context_data()
        context['designer'].available_categories = context['designer'].available_categories_by_discipline(self.discipline)
        return context
