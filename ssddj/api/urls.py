from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = patterns('',
            url(r'^provisioner/$', views.Provisioner.as_view()),
                url(r'^targets/(?P<pk>[0-9]+)/$', views.TargetDetail.as_view()),
                )

urlpatterns = format_suffix_patterns(urlpatterns)
