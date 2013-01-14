from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from backoffice.views import DisciplineTemplateView
from django.contrib import admin
admin.autodiscover()
from backoffice.views import BookListView, DecadeListView, DesignerListView
from backoffice.views import CategoryListView, SubjectListView, WorkDetailView, WorkListView
from django.views.generic.detail import DetailView
from backoffice import models
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

discipline_urls = patterns('website.views',
                          (r'^article/$', DisciplineTemplateView.as_view(template_name='backoffice/article_list.html'), {}, "article-list"),
                          (r'^book/$', BookListView.as_view(), {}, 'book-list'),
                          (r'^book/(\d+)/$', BookListView.as_view(), {}, 'book-list'),
                          (r'^event/$', DisciplineTemplateView.as_view(template_name='backoffice/event_list.html'), {}, "event-list"),
                          (r'^link/$', DisciplineTemplateView.as_view(template_name='backoffice/link_list.html'), {}, "link-list"),
                          (r'^video/$', DisciplineTemplateView.as_view(template_name='backoffice/video_list.html'), {}, "video-list"),
                          (r'^decade/$', DecadeListView.as_view(), {}, "decade-list"),
                          (r'^designer/$', DesignerListView.as_view(), {}, 'designer-list'),
                          (r'^category/$', CategoryListView.as_view(), {}, 'category-list'),
                          (r'^subject/$', SubjectListView.as_view(), {}, 'subject-list'),
                          (r'^work/(?P<pk>\d+)/$', WorkDetailView.as_view(), {}, "work-detail"),
                          (r'^work/$', WorkListView.as_view(), {}, "work-list"),
                          (r'^$', DetailView.as_view(model=models.Discipline, template_name='website/discipline_detail.html', pk_url_kwarg='discipline'), {}, "discipline-detail"),
                           )


site_urls = patterns('website.views',
                    (r'^about/$', TemplateView.as_view(template_name='about.html'), {}, "about"),
                    (r'^goals/$', TemplateView.as_view(template_name='goals.html'), {}, "goals"),
                    (r'^discipline/(?P<discipline>\d+)/', include(discipline_urls)),
                    (r'^$', ListView.as_view(template_name="home.html", queryset=models.Work.objects.one_from_each_discipline()), {'works': models.Work.objects.one_from_each_discipline()}, "home"),
                     )

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'sidar.views.home', name='home'),
                       # url(r'^sidar/', include('sidar.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include(site_urls)),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
                           (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )
