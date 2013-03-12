from django.conf import settings
from django.conf.urls import patterns, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout, login
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from backoffice import models, views
from backoffice.views import DisciplineTemplateView, DesignerListView, DisciplineDetailView, WorkFieldListViewByDiscipline, WorkListView, SearchView
from bibliography.views import BookListView
from collection.views import CollectView


admin.autodiscover()


work_urls = patterns('',
    (r'^$', WorkListView.as_view(), {}, "work-list"),
    (r'^work-(?P<work>\d+)/$', WorkListView.as_view(), {}, "work-detail")
    )

discipline_urls = patterns('',
                          (r'^about/$', views.DisciplineTemplateView.as_view(template_name='backoffice/discipline_about.html'), {}, 'discipline-about'),
                          (r'^article/$', DisciplineTemplateView.as_view(template_name='backoffice/article_list.html'), {}, "article-list"),
                          (r'^search/$', SearchView.as_view(), {}, 'search'),

                          (r'^book/$', BookListView.as_view(), {}, 'book-list'),
                          (r'^book/(\d+)/$', BookListView.as_view(), {}, 'book-list'),

                          (r'^event/$', DisciplineTemplateView.as_view(template_name='backoffice/event_list.html'), {}, "event-list"),
                          (r'^link/$', DisciplineTemplateView.as_view(template_name='backoffice/link_list.html'), {}, "link-list"),
                          (r'^video/$', DisciplineTemplateView.as_view(template_name='backoffice/video_list.html'), {}, "video-list"),

                          (r'^year/$', DisciplineTemplateView.as_view(template_name="backoffice/decade_list.html"), {}, "decade-list"),
                          (r'^year/(?P<from>\d*)-(?P<until>\d*)/', include(work_urls), {'main_filter': 'year'}),
                          (r'^year/(?P<from>\d*)-(?P<until>\d*)/(?P<year>\d+)/', include(work_urls), {'main_filter': 'year'}),

                          (r'^designer/$', DesignerListView.as_view(), {}, 'designer-list'),
                          (r'^designer/(?P<pk>\d+)/about/$', DisciplineDetailView.as_view(model=models.Designer), {}, "designer-detail"),
                          (r'^designer/(?P<designer>\d+)/', include(work_urls), {'main_filter': 'designer'}),
                          # (r'^designer/(?P<designer>\d+)/category/(?P<category>\d+)/', include(work_urls)),

                          (r'^category/$', WorkFieldListViewByDiscipline.as_view(model=models.Category), {'work_field': 'category'}, 'category-list'),
                          (r'^category/(?P<category>\d+)/', include(work_urls), {'main_filter': 'category'}),
                          (r'^category/(?P<category>\d+)/designer/(?P<designer>\d+)/', include(work_urls), {'main_filter': 'category'}),

                          (r'^subject/$', WorkFieldListViewByDiscipline.as_view(model=models.Subject), {'work_field': 'subjects'}, 'subject-list'),
                          (r'^subject/(?P<subject>\d+)/', include(work_urls), {'main_filter': 'subject'}),
                          (r'^subject/(?P<subject>\d+)/designer/(?P<designer>\d+)/', include(work_urls), {'main_filter': 'subject'}),

                          (r'^work-(?P<work>\d+)/$', WorkListView.as_view(), {}, "work-detail"),
                          (r'^work/(?P<pk>\d+)/collect/$', login_required(CollectView.as_view())),
                          (r'^$', WorkListView.as_view(template_name="backoffice/discipline_home.html"), {}, "discipline-detail"),
                           )


urlpatterns = patterns('',
                       (r'^new/$', TemplateView.as_view(template_name='next_gen/index.html')),
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
