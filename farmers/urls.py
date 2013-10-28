from django.conf.urls import patterns, url

urlpatterns = patterns('farmers.views',
    url(r'^farmers/$', 'farmer_list'),
    url(r'^farmers/(?P<pk>[0-9]+)/$', 'farmer_detail'),
)