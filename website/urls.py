from django.conf.urls import patterns
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from backoffice import models
from django.views.generic.list import ListView
from django.conf.urls import include

from website.views import WorkListView
from website.views import WorkDetailView
from website.views import DesignerListView
discipline = patterns('website.views',

                      (r'^designer/$', DesignerListView.as_view(), {}, 'designer-list'),
                      (r'^category/$', 'generic_list', {'model': models.Category, 'field': 'category'}, 'category-list'),
                      (r'^subject/$', 'generic_list', {'model': models.Subject, 'field': 'subjects'}, 'subject-list'),
                      (r'^work/(?P<pk>\d+)/$', WorkDetailView.as_view(), {}, "work-detail"),
                      (r'^work/$', WorkListView.as_view(), {}, "work-list"),
                      (r'^$', DetailView.as_view(model=models.Discipline, template_name='website/discipline_detail.html', pk_url_kwarg='discipline'), {}, "discipline-detail"),
                      )


urlpatterns = patterns('website.views',
                       (r'^about/$', TemplateView.as_view(template_name='website/about.html'), {}, "about"),
                       (r'^goals/$', TemplateView.as_view(template_name='website/goals.html'), {}, "goals"),
                       (r'^discipline/(?P<discipline>\d+)/', include(discipline)),
                       (r'^$', ListView.as_view(template_name="website/home.html", queryset=models.Work.objects.one_from_each_discipline()), {'works': models.Work.objects.one_from_each_discipline()}, "home"),
                       )
