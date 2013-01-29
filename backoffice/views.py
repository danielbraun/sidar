# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from backoffice.forms import SearchForm
from backoffice.models import Designer, Discipline, Work, Generation, Category, Subject
from bibliography.models import Book, BookCategory

from django.utils.translation import get_language


class DisciplineMixin(object):
    def dispatch(self, *args, **kwargs):
        self.discipline = Discipline.objects.get(pk=kwargs['discipline'])
        return super(DisciplineMixin, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DisciplineMixin, self).get_context_data(**kwargs)
        context['discipline'] = self.discipline
        return context


class WorkListView(DisciplineMixin, ListView):
    paginate_by = 10

    def get_queryset(self):
        works = Work.objects.filter(discipline=self.discipline)
        designer = self.request.GET.get('designer')
        subject = self.request.GET.get('subject')
        category = self.request.GET.get('category')
        if designer:
            works = works.filter(designer=designer)
        if subject:
            works = works.filter(subjects=subject)
        if category:
            works = works.filter(category=category)
        return works

    def get_context_data(self, **kwargs):
        context = super(WorkListView, self).get_context_data(**kwargs)
        query = self.request.GET.copy()
        if query.get('page'):
            del query['page']
        context['filters'] = query.urlencode()
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
                'designer_groups': [Designer.objects.belonging_to_discipline(self.discipline, 'designer').filter(name_he__startswith=unicode(letter, 'utf-8')) for letter in group]
            })
        return object_list


class DecadeListView(DisciplineMixin, TemplateView):
    template_name = "backoffice/decade_list.html"

    def get_context_data(self, **kwargs):
            context = super(DecadeListView, self).get_context_data(**kwargs)
            context['decades'] = range(1890, 2030, 10)
            return context


class DisciplineTemplateView(DisciplineMixin, TemplateView):
    pass


class CategoryListView(DisciplineMixin, ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.belonging_to_discipline(self.discipline, 'category').order_by('parent', 'name_he').exclude(parent=None)


class SubjectListView(DisciplineMixin, ListView):
    model = Subject

    def get_queryset(self):
        return Subject.objects.belonging_to_discipline(self.discipline, 'subjects').order_by('parent', 'name_he').exclude(parent=None)


class BookListView(DisciplineMixin, ListView):

    def get_queryset(self):
        queryset = Book.objects.filter(discipline=self.discipline)
        try:
            self.category = BookCategory.objects.get(pk=self.args[0])
            queryset = queryset.filter(category=self.category)
        except IndexError:
            pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        try:
            context['category'] = self.category
        except AttributeError:
            pass
        return context


class DisciplineSearchView(DisciplineMixin, FormView):
    form_class = SearchForm
    template_name = 'search.html'

    def get_form_kwargs(self):
        kwargs = super(DisciplineSearchView, self).get_form_kwargs()
        kwargs['discipline'] = self.discipline
        return kwargs
