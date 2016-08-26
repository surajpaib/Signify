from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^embed/$', views.embed, name='embed'),
    url(r'^vid/(?P<pk>\d+)/$', views.vid_detail, name='vid_detail'),
]
