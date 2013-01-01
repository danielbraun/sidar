# -*- coding: utf-8 -*-
from backoffice.models import Designer, Discipline

from django.shortcuts import render

from backoffice.models import Work

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from backoffice.models import Generation


def generic_list(request, discipline, model, field):
    discipline = Discipline.objects.get(pk=discipline)
    return render(request, 'website/generic_list.html', {
        'discipline': discipline,
        'object_list': model.objects.belonging_to_discipline(discipline, field)
    })


class WorkListView(ListView):
    template_name = 'website/work_list.html'
    paginate_by = 10

    def get_queryset(self):
        self.discipline = Discipline.objects.get(pk=self.kwargs['discipline'])
        works = Work.objects.filter(discipline=self.discipline)
        try:
            works = works.filter(designer=self.request.GET['designer'])
        except KeyError:
            pass
        return works

    def get_context_data(self, **kwargs):
        context = super(WorkListView, self).get_context_data(**kwargs)
        context['discipline'] = self.discipline
        try:
            query = self.request.GET.copy()
            del query['page']
            context['filters'] = query.urlencode()
        except KeyError:
            pass
        return context


class DisciplineMixin(object):
    # def dispatch(self, request, *args, **kwargs):
    #     response = super(DisciplineMixin, self).dispatch(request, *args, **kwargs)
    #     return response

    def get_context_data(self, **kwargs):
        context = super(DisciplineMixin, self).get_context_data(**kwargs)
        context['discipline'] = Discipline.objects.get(pk=self.kwargs['discipline'])
        return context


class WorkDetailView(DisciplineMixin, DetailView):
    template_name = "website/work_detail.html"
    model = Work


class DesignerListView(DisciplineMixin, ListView):
    template_name = "website/designer_list.html"
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
        self.discipline = Discipline.objects.get(pk=self.kwargs['discipline'])
        object_list = []
        for group in self.letter_groups:
            object_list.append({
                'letters': group,
                'designer_groups': [Designer.objects.belonging_to_discipline(self.discipline, 'designer').filter(name_he__startswith=unicode(letter, 'utf-8')) for letter in group]
            })
        return object_list
