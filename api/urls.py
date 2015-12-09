from django.conf.urls import include, url
from django.conf.urls import patterns, url
from api import views
from api.views import tokenViews
from api.views import cloudViews
from api.views import baseImageViews
from api.views import roleViews
from api.views import accountViews
from api.views import systemViews
from api.views import environmentViews
from api.views import applicationViews
from api.views import blueprintViews
from api.views import patternViews

urlpatterns = patterns('',
    # role
    url(r'^v1/role/(?P<id>\d+)/menu/$', views.roleViews.role_menu, name='role_menu'),
    url(r'^v1/role/(?P<id>\d+)/project/$', views.roleViews.role_project, name='role_project'),
    # project_list
    url(r'^v1/projects/$', views.projectViews.project_list, name='project_list'),     # list
    url(r'^v1/projects/(?P<id>\d+)/detail/$', views.projectViews.project_detail, name='project_detail'),     # detail
    url(r'^v1/projects/create/$', views.projectViews.project_create, name='project_create'),     # create
    url(r'^v1/projects/(?P<id>\d+)/update/$', views.projectViews.project_update, name='project_update'),     # update
    url(r'^v1/projects/(?P<id>\d+)/delete/$', views.projectViews.project_delete, name='project_delete'),     # delete
    url(r'^v1/assignments/$', views.projectViews.assign_user_list, name='assigin_list'),
    url(r'^v1/assigin/(?P<id>\d+)/edit/$', views.projectViews.project_assign_user, name='assigin_edit'),

    url(r'^v1/tokens$', views.tokenViews.token, name='token'),

#     url(r'^v1/project/list/$', views.projectViews.project_list, name='project_list'),
#     url(r'^v1/project/(?P<id>\d+)/detail/$', views.projectViews.project_detail, name='project_detail'),
#     url(r'^v1/project/create/$', views.projectViews.project_create, name='project_create'),
#     url(r'^v1/project/(?P<id>\d+)/update/$', views.projectViews.project_update, name='project_update'),
#     url(r'^v1/project/(?P<id>\d+)/delete/$', views.projectViews.project_delete, name='project_delete'),
#

    url(r'^v1/account/list/$', views.accountViews.account_list, name='account_list'),
    url(r'^v1/account/(?P<id>\d+)/detail/$', views.accountViews.account_detail, name='account_detail'),
    url(r'^v1/account/create/$', views.accountViews.account_create, name='account_create'),
    url(r'^v1/account/(?P<id>\d+)/update/$', views.accountViews.account_update, name='account_update'),
    url(r'^v1/account/(?P<id>\d+)/delete/$', views.accountViews.account_delete, name='account_delete'),
    url(r'^v1/cloud/list/$', views.cloudViews.cloud_list, name='cloud_list'),
    url(r'^v1/cloud/(?P<id>\d+)/detail/$', views.cloudViews.cloud_detail, name='cloud_detail'),
    url(r'^v1/cloud/create/$', views.cloudViews.cloud_create, name='cloud_create'),
    url(r'^v1/cloud/(?P<id>\d+)/update/$', views.cloudViews.cloud_update, name='cloud_update'),
    url(r'^v1/cloud/(?P<id>\d+)/delete/$', views.cloudViews.cloud_delete, name='cloud_delete'),
#
    url(r'^v1/base_images/list/$', views.baseImageViews.baseImage_list, name='baseImage_list'),
    url(r'^v1/base_images/(?P<id>\d+)/detail/$', views.baseImageViews.baseImage_detail, name='baseImage_detail'),
    url(r'^v1/base_images/create/$', views.baseImageViews.baseImage_create, name='baseImage_create'),
    url(r'^v1/base_images/(?P<id>\d+)/update/$', views.baseImageViews.baseImage_update, name='baseImage_update'),
    url(r'^v1/base_images/(?P<id>\d+)/delete/$', views.baseImageViews.baseImage_delete, name='baseImage_delete'),

    url(r'^v1/blueprint/list/$', views.blueprintViews.blueprint_list, name='blueprint_list'),
    url(r'^v1/blueprint/(?P<id>\d+)/detail/$', views.blueprintViews.blueprint_detail, name='blueprint_detail'),
    url(r'^v1/blueprint/create/$', views.blueprintViews.blueprint_create, name='blueprint_create'),
    url(r'^v1/blueprint/(?P<id>\d+)/update/$', views.blueprintViews.blueprint_update, name='blueprint_update'),
    url(r'^v1/blueprint/(?P<id>\d+)/delete/$', views.blueprintViews.blueprint_delete, name='blueprint_delete'),
    url(r'^v1/blueprint/parameters/$', views.blueprintViews.blueprint_parameters, name='blueprint_parameters'),

    url(r'^v1/pattern/list/$', views.patternViews.pattern_list, name='pattern_list'),
    url(r'^v1/pattern/(?P<id>\d+)/detail/$', views.patternViews.pattern_detail, name='pattern_detail'),
    url(r'^v1/pattern/create/$', views.patternViews.pattern_create, name='pattern_create'),
    url(r'^v1/pattern/(?P<id>\d+)/update/$', views.patternViews.pattern_update, name='pattern_update'),
    url(r'^v1/pattern/(?P<id>\d+)/delete/$', views.patternViews.pattern_delete, name='pattern_delete'),

    url(r'^v1/system/list/$', views.systemViews.system_list, name='system_list'),
    url(r'^v1/system/(?P<id>\d+)/detail/$', views.systemViews.system_detail, name='system_detail'),
    url(r'^v1/system/create/$', views.systemViews.system_create, name='system_create'),
    url(r'^v1/system/(?P<id>\d+)/update/$', views.systemViews.system_update, name='system_update'),
    url(r'^v1/system/(?P<id>\d+)/delete/$', views.systemViews.system_delete, name='system_delete'),
    url(r'^v1/system/switch/$', views.systemViews.system_switch, name='system_switch'),

    url(r'^v1/environment/list/$', views.environmentViews.environment_list, name='environment_list'),
    url(r'^v1/environment/(?P<id>\d+)/detail/$', views.environmentViews.environment_detail, name='environment_detail'),
    url(r'^v1/environment/create/$', views.environmentViews.environment_create, name='environment_create'),
    url(r'^v1/environment/(?P<id>\d+)/update/$', views.environmentViews.environment_update, name='environment_update'),
    url(r'^v1/environment/(?P<id>\d+)/delete/$', views.environmentViews.environment_delete, name='environment_delete'),
#
#     url(r'^v1/environment/eventList/$', views.environmentViews.environment_eventList, name='environment_eventList'),
#     url(r'^v1/environment/event/$', views.environmentViews.environment_event, name='environment_event'),
#     url(r'^v1/environment/sendEvent/$', views.environmentViews.environment_sendEvent, name='environment_sendEvent'),
#     url(r'^v1/environment/rebuild/$', views.environmentViews.environment_rebuild, name='environment_rebuild'),

    url(r'^v1/application/list/$', views.applicationViews.application_list, name='application_list'),
    url(r'^v1/application/(?P<id>\d+)/detail/$', views.applicationViews.application_detail, name='application_detail'),
    url(r'^v1/application/create/$', views.applicationViews.application_create, name='application_create'),
    url(r'^v1/application/(?P<id>\d+)/update/$', views.applicationViews.application_update, name='application_update'),
    url(r'^v1/application/(?P<id>\d+)/delete/$', views.applicationViews.application_delete, name='application_delete'),
    url(r'^v1/application/deploy/$', views.applicationViews.application_deploy, name='application_deploy'),
#
#
#     url(r'^v1/application_history/list/$', views.application_historyViews.application_history_list, name='application_history_list'),
#     url(r'^v1/application_history/(?P<id>\d+)/detail/$', views.application_historyViews.application_history_detail, name='application_history_detail'),
#     url(r'^v1/application_history/create/$', views.application_historyViews.application_history_create, name='application_history_create'),
#     url(r'^v1/application_history/(?P<id>\d+)/update/$', views.application_historyViews.application_history_update, name='application_history_update'),
#     url(r'^v1/application_history/(?P<id>\d+)/delete/$', views.application_historyViews.application_history_delete, name='application_history_delete'),


)

