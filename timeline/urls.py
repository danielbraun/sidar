from django.conf.urls import patterns
from django.conf.urls import url
urlpatterns = patterns('',
                       url(r'^$', ListViewByDiscipline.as_view(), name='timeline_event_list')
                       )
