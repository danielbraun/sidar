from django.conf.urls import patterns
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from backoffice.models import Discipline
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                      (r'^discipline/$', login_required(ListView.as_view(model=Discipline,
                                                                         template_name="sidar_admin/list.html"))),
                      (r'^discipline/(?P<pk>\d+)/$', UpdateView.as_view(model=Discipline,
                                                                        template_name="sidar_admin/form.html",
                                                                        success_url="../"
                                                                        ))
                       )
