from django.conf.urls import include, url

from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    # project_list
    url(r'^v1/projects/$', views.projectViews.project_list, name='project_list'),     # list
    url(r'^v1/projects/(?P<id>\d+)/detail/$', views.projectViews.project_detail, name='project_detail'),     # detail
    url(r'^v1/projects/create/$', views.projectViews.project_create, name='project_create'),     # create
    url(r'^v1/projects/(?P<id>\d+)/update/$', views.projectViews.project_update, name='project_update'),     # update
    url(r'^v1/projects/(?P<id>\d+)/delete/$', views.projectViews.project_delete, name='project_delete'),     # delete
)

