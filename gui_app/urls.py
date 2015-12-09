from django.conf.urls import include, url
from .views import projectViews
from .views import cloudViews
from .views import baseImageViews
from .views import roleViews
from .views import loginViews
from .views import accountViews
from .views import systemViews
from .views import environmentViews
from .views import applicationViews
from .views import blueprintViews
from .views import patternViews
from .views import topViews


urlpatterns = [

    url('^login/', loginViews.login, name="login"),
    url('^logout/', loginViews.logout, name="logout"),
    url(r"^$", environmentViews.environmentList, name="top"),

    url('^project/list', projectViews.projectList, name="projectList"),
    url('^project/create', projectViews.projectCreate, name="projectCreate"),
    url('^project/(?P<id>\d+)/detail/', projectViews.projectDetail, name="projectDetail"),
    url('^project/(?P<id>\d+)/delete/', projectViews.projectDelete, name="projectDelete"),
    url('^project/add/$', projectViews.projectEdit, name="projectAdd"),
    url('^project/(?P<id>\d+)/edit/$', projectViews.projectEdit, name="projectEdit"),
    url('^project/(?P<id>\d+)/projectAddUser/$', projectViews.projectAddUser, name="projectAddUser"),

    url('^cloud/list', cloudViews.cloudList, name="cloudList"),
    url('^cloud/(?P<id>\d+)/detail/', cloudViews.cloudDetail, name="cloudDetail"),
    url('^cloud/create', cloudViews.cloudCreate, name="cloudCreate"),
    url('^cloud/(?P<id>\d+)/edit/$', cloudViews.cloudEdit, name="cloudEdit"),
    url('^cloud/(?P<id>\d+)/delete/', cloudViews.cloudDelete, name="cloudDelete"),

    url('^baseimage/(?P<id>\d+)/detail/', baseImageViews.baseImageDetail, name="baseImageDetail"),
    url('^cloud/(?P<cid>\d+)/baseimage/create', baseImageViews.baseImageCreate, name="baseImageCreate"),
    url('^baseimage/(?P<id>\d+)/edit/$', baseImageViews.baseImageEdit, name="baseImageEdit"),
    url('^baseimage/(?P<id>\d+)/delete/', baseImageViews.baseImageDelete, name="baseImageDelete"),

    url('^system/list', systemViews.systemList, name="systemList"),
    url('^system/(?P<id>\d+)/detail/', systemViews.systemDetail, name="systemDetail"),
    url('^system/create', systemViews.systemCreate, name="systemCreate"),
    url('^system/(?P<id>\d+)/edit/$', systemViews.systemEdit, name="systemEdit"),
    url('^system/(?P<id>\d+)/delete/', systemViews.systemDelete, name="systemDelete"),

    url('^environment/list', environmentViews.environmentList, name="environmentList"),
    url('^environment/(?P<id>\d+)/detail/', environmentViews.environmentDetail, name="environmentDetail"),
    url('^environment/create', environmentViews.environmentCreate, name="environmentCreate"),
    url('^environment/(?P<id>\d+)/edit/$', environmentViews.environmentEdit, name="environmentEdit"),
    url('^environment/(?P<id>\d+)/delete/', environmentViews.environmentDelete, name="environmentDelete"),

    url('^application/list', applicationViews.applicationList, name="applicationList"),
    url('^application/(?P<id>\d+)/detail/', applicationViews.applicationDetail, name="applicationDetail"),
    url('^application/create', applicationViews.applicationCreate, name="applicationCreate"),
    url('^application/(?P<id>\d+)/edit/$', applicationViews.applicationEdit, name="applicationEdit"),
    url('^application/(?P<id>\d+)/delete/', applicationViews.applicationDelete, name="applicationDelete"),

    url('^blueprint/list', blueprintViews.blueprintList, name="blueprintList"),
    url('^blueprint/(?P<id>\d+)/detail/', blueprintViews.blueprintDetail, name="blueprintDetail"),
    url('^blueprint/create', blueprintViews.blueprintCreate, name="blueprintCreate"),
    url('^blueprint/(?P<id>\d+)/edit/$', blueprintViews.blueprintEdit, name="blueprintEdit"),
    url('^blueprint/(?P<id>\d+)/delete/', blueprintViews.blueprintDelete, name="blueprintDelete"),

    url('^blueprint/list', blueprintViews.blueprintList, name="blueprintList"),
    url('^blueprint/(?P<id>\d+)/detail/', blueprintViews.blueprintDetail, name="blueprintDetail"),
    url('^blueprint/create', blueprintViews.blueprintCreate, name="blueprintCreate"),
    url('^blueprint/(?P<id>\d+)/edit/$', blueprintViews.blueprintEdit, name="blueprintEdit"),
    url('^blueprint/(?P<id>\d+)/delete/', blueprintViews.blueprintDelete, name="blueprintDelete"),

    url('^pattern/list', patternViews.patternList, name="patternList"),
    url('^pattern/(?P<id>\d+)/detail/', patternViews.patternDetail, name="patternDetail"),
    url('^pattern/create', patternViews.patternCreate, name="patternCreate"),
    url('^pattern/(?P<id>\d+)/edit/$', patternViews.patternEdit, name="patternEdit"),
    url('^pattern/(?P<id>\d+)/delete/', patternViews.patternDelete, name="patternDelete"),

    url('^role/index/', roleViews.index, name="role"),
    url('^role/(?P<id>\d+)/menu/', roleViews.roleChange, name="roleChange"),

    url('^account/list', accountViews.index, name="accountList"),
    url('^account/(?P<id>\d+)/detail/', accountViews.accountDetail, name="accountDetail"),
    url('^account/create/', accountViews.accountCreate, name="accountCreate"),
    url('^account/(?P<id>\d+)/edit/', accountViews.accountEdit, name="accountEdit"),
    url('^account/(?P<id>\d+)/delete/', accountViews.accountDelete, name="accountDelete"),
]