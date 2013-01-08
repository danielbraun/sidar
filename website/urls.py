from django.conf.urls import patterns
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from backoffice import models
from django.views.generic.list import ListView
from django.conf.urls import include
from website.views import WorkListView, WorkDetailView, DesignerListView, DecadeListView
from website.views import DisciplineTemplateView
from website.views import CategoryListView
from website.views import SubjectListView


discipline = patterns('website.views',
                     (r'^article/$', DisciplineTemplateView.as_view(template_name='website/article_list.html'), {}, "article-list"),
                     (r'^bibliography/$', DisciplineTemplateView.as_view(template_name='website/bibliography.html'), {}, "bibliography"),
                     (r'^event/$', DisciplineTemplateView.as_view(template_name='website/event_list.html'), {}, "event-list"),
                     (r'^link/$', DisciplineTemplateView.as_view(template_name='website/link_list.html'), {}, "link-list"),
                     (r'^video/$', DisciplineTemplateView.as_view(template_name='website/video_list.html'), {}, "video-list"),
                     (r'^decade/$', DecadeListView.as_view(), {}, "decade-list"),
                     (r'^designer/$', DesignerListView.as_view(), {}, 'designer-list'),
                     (r'^category/$', CategoryListView.as_view(), {}, 'category-list'),
                     (r'^subject/$', SubjectListView.as_view(), {}, 'subject-list'),
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
