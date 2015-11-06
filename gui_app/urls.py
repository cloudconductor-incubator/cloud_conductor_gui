from django.conf.urls import include, url
from . import views

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


]