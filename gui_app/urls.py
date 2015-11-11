from django.conf.urls import include, url
from . import views
from .views2 import cloudViews
from .views2 import baseImageViews

urlpatterns = [
#    url(r"^$", views.index, name="index"),
#    url('^registration/login', views.login, name="login"),
#    url('^registration/logout', views.logout, name="logout"),

    #CloudConductor
#     url('^projectList/', views.projectList, name="projectList"),
#     url('^projectCreate/', views.projectCreate, name="projectCreate"),
    url('^login/', views.login, name="login"),
    url('^top/', views.top, name="top"),
    url('^project/list', views.projectList, name="projectList"),
    url('^project/create', views.projectCreate, name="projectCreate"),
    url('^project/(?P<id>\d+)/detail/', views.projectDetail, name="projectDetail"),
    url('^project/(?P<id>\d+)/delete/', views.projectDelete, name="projectDelete"),
    url('^project/add/$', views.projectEdit, name="projectAdd"),
    url('^project/(?P<id>\d+)/edit/$', views.projectEdit, name="projectEdit"),

    url('^cloud/list', cloudViews.cloudList, name="cloudList"),
    url('^cloud/(?P<id>\d+)/cloud/', cloudViews.cloudDetail, name="cloudDetail"),
    url('^cloud/create', cloudViews.cloudCreate, name="cloudCreate"),
    url('^cloud/(?P<id>\d+)/edit/$', cloudViews.cloudEdit, name="cloudEdit"),
    url('^cloud/(?P<id>\d+)/delete/', cloudViews.cloudDelete, name="cloudDelete"),

    url('^baseimage/(?P<id>\d+)/baseimage/', baseImageViews.baseImageDetail, name="baseImageDetail"),
    url('^baseimage/create', baseImageViews.baseImageCreate, name="baseImageCreate"),
    url('^baseimage/(?P<id>\d+)/edit/$', baseImageViews.baseImageEdit, name="baseImageEdit"),
    url('^baseimage/(?P<id>\d+)/delete/', baseImageViews.baseImageDelete, name="baseImageDelete"),

]