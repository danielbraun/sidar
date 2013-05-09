from django.conf import settings
from django.conf.urls import patterns, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout, login
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from backoffice import models, views
from backoffice.views import DesignerDetailView, DisciplineTemplateView, DesignerListView, WorkFieldListViewByDiscipline, WorkListView, SearchView
from collection.views import CollectView
from helpers.views import RegistrationFormView


admin.autodiscover()


work_urls = patterns('',
                    (r'^$', WorkListView.as_view(), {}, "work-list"),
                    (r'^work-(?P<work>\d+)/$', WorkListView.as_view(), {}, "work-detail"),
                    (r'^work-(?P<pk>\d+)/collect/$', login_required(CollectView.as_view()))
                     )

discipline_urls = patterns('',
                          (r'^timeline/', include('timeline.urls')),

                          (r'^book/', include('bibliography.urls')),

                          (r'^about/$', views.DisciplineTemplateView.as_view(
                              template_name='backoffice/discipline_about.html'), {}, 'discipline-about'),
                          (r'^article/$', DisciplineTemplateView.as_view(
                              template_name='backoffice/article_list.html'), {}, "article-list"),
                          (r'^search/$', SearchView.as_view(), {}, 'search'),

                          (r'^event/$', DisciplineTemplateView.as_view(
                              template_name='backoffice/event_list.html'), {}, "event-list"),
                          (r'^link/$', DisciplineTemplateView.as_view(
                              template_name='backoffice/link_list.html'), {}, "link-list"),
                          (r'^video/$', DisciplineTemplateView.as_view(
                              template_name='backoffice/video_list.html'), {}, "video-list"),

                          (r'^year/$', DisciplineTemplateView.as_view(
                              template_name="backoffice/decade_list.html"), {}, "decade-list"),
                          (r'^year/(?P<from>\d*)-(?P<until>\d*)/', include(work_urls), {'main_filter': 'year'}),
                          (r'^year/(?P<from>\d*)-(?P<until>\d*)/(?P<year>\d+)/', include(work_urls), {'main_filter': 'year'}),

                          (r'^designer/$', DesignerListView.as_view(), {}, 'designer-list'),
                          (r'^designer/(?P<pk>\d+)/about/$', DesignerDetailView.as_view(), {}, "designer-detail"),
                          (r'^designer/(?P<designer>\d+)/', include(work_urls), {'main_filter': 'designer'}),
                           # (r'^designer/(?P<designer>\d+)/category/(?P<category>\d+)/', include(work_urls)),

                          (r'^category/$', WorkFieldListViewByDiscipline.as_view(
                              model=models.Category), {'work_field': 'category'}, 'category-list'),
                          (r'^category/(?P<category>\d+)/', include(work_urls), {'main_filter': 'category'}),
                          (r'^category/(?P<category>\d+)/designer/(?P<designer>\d+)/', include(
                              work_urls), {'main_filter': 'category'}),

                          (r'^subject/$', WorkFieldListViewByDiscipline.as_view(
                              model=models.Subject), {'work_field': 'subjects'}, 'subject-list'),
                          (r'^subject/(?P<subject>\d+)/', include(work_urls), {'main_filter': 'subject'}),
                          (r'^subject/(?P<subject>\d+)/designer/(?P<designer>\d+)/', include(
                              work_urls), {'main_filter': 'subject'}),

                           # (r'^work-(?P<work>\d+)/$', WorkListView.as_view(), {}, "work-detail"),
                          (r'^$', WorkListView.as_view(
                              template_name="backoffice/discipline_home.html"), {}, "discipline-detail"),
                           )


urlpatterns = patterns('',
                      (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Deliberately no trailing slash after pages
                      (r'^feedback/', include('feedback.urls')),
                      (r'^tinymce/', include('tinymce.urls')),
                      (r'^new/$', TemplateView.as_view(template_name="new/index.html")),
                      (r'^logout/$', logout),
                      (r'^login/$', login),
                      (r'^register/$', RegistrationFormView.as_view(), {}, "register"),
                      (r'^admin/', include(admin.site.urls)),
                      (r'^discipline/(?P<discipline>\d+)/', include(discipline_urls)),
                      (r'^collection/', include('collection.urls')),
                      (r'^$', ListView.as_view(
                       template_name="home.html",
                       queryset=models.Work.objects.one_from_each_discipline(),
                       model=models.Work), {}, "home"),
                      (r'^', include('django.contrib.flatpages.urls')),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
                           (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )
