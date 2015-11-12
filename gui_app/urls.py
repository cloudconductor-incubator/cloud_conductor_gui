from django.conf.urls import include, url
from .views import projectViews
from .views import cloudViews
from .views import baseImageViews
from .views import roleViews
from .views import loginViews

urlpatterns = [
#    url(r"^$", views.index, name="index"),
#    url('^registration/login', views.login, name="login"),
#    url('^registration/logout', views.logout, name="logout"),

    #CloudConductor
#     url('^projectList/', views.projectList, name="projectList"),
#     url('^projectCreate/', views.projectCreate, name="projectCreate"),
    url('^login/', loginViews.login, name="login"),
    url('^top/', loginViews.top, name="top"),
    url('^project/list', projectViews.projectList, name="projectList"),
    url('^project/create', projectViews.projectCreate, name="projectCreate"),
    url('^project/(?P<id>\d+)/detail/', projectViews.projectDetail, name="projectDetail"),
    url('^project/(?P<id>\d+)/delete/', projectViews.projectDelete, name="projectDelete"),
    url('^project/add/$', projectViews.projectEdit, name="projectAdd"),
    url('^project/(?P<id>\d+)/edit/$', projectViews.projectEdit, name="projectEdit"),
    url('^project/(?P<id>\d+)/projectAddUser/$', projectViews.projectAddUser, name="projectAddUser"),

    url('^cloud/list', cloudViews.cloudList, name="cloudList"),
    url('^cloud/(?P<id>\d+)/cloud/', cloudViews.cloudDetail, name="cloudDetail"),
    url('^cloud/create', cloudViews.cloudCreate, name="cloudCreate"),
    url('^cloud/(?P<id>\d+)/edit/$', cloudViews.cloudEdit, name="cloudEdit"),
    url('^cloud/(?P<id>\d+)/delete/', cloudViews.cloudDelete, name="cloudDelete"),

    url('^baseimage/(?P<id>\d+)/baseimage/', baseImageViews.baseImageDetail, name="baseImageDetail"),
    url('^baseimage/create', baseImageViews.baseImageCreate, name="baseImageCreate"),
    url('^baseimage/(?P<id>\d+)/edit/$', baseImageViews.baseImageEdit, name="baseImageEdit"),
    url('^baseimage/(?P<id>\d+)/delete/', baseImageViews.baseImageDelete, name="baseImageDelete"),

    url('^role/(?P<id>\d+)/menu/', roleViews.roleChange, name="roleChange"),

]