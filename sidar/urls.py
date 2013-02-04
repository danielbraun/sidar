from django.conf import settings
from django.conf.urls import patterns, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout, login
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from backoffice import models
from backoffice.views import DisciplineTemplateView, DecadeListView, DesignerListView, CategoryListView, SubjectListView, WorkDetailView, WorkListView, DisciplineSearchView
from collection.views import CollectView

from bibliography.views import BookListView

admin.autodiscover()

discipline_urls = patterns('',
                          (r'^about/$', DisciplineTemplateView.as_view(template_name='backoffice/discipline_about.html'), {}, 'discipline-about'),
                          (r'^article/$', DisciplineTemplateView.as_view(template_name='backoffice/article_list.html'), {}, "article-list"),
                          (r'^search/$', DisciplineSearchView.as_view(), {}, 'search'),
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
                          (r'^work/(?P<pk>\d+)/collect/$', login_required(CollectView.as_view())),
                          (r'^work/$', WorkListView.as_view(), {}, "work-list"),
                          (r'^$', DetailView.as_view(model=models.Discipline, pk_url_kwarg='discipline'), {}, "discipline-detail"),
                           )


urlpatterns = patterns('',
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Deliberately no trailing slash after pages
                       (r'^pages', include('django.contrib.flatpages.urls')),
                       (r'^logout/$', logout),
                       (r'^login/$', login),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^discipline/(?P<discipline>\d+)/', include(discipline_urls)),
                       (r'^collection/', include('collection.urls')),
                       (r'^$', ListView.as_view(template_name="home.html", queryset=models.Work.objects.one_from_each_discipline()), {'works': models.Work.objects.one_from_each_discipline()}, "home"),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
                           (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )
