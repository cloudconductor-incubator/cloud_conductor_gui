from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from api.views.commonViews import render_json_response

def environment_list(request):

    lists = []

    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('blueprint_id', "1"),
        ('name', "tomcat_environment"),
        ('description', "tomcat environment"),
        ('status', "CREATE_COMPLETE"),
        ('ip_address', "xx.xx.xx.xx"),
        ('created_at', "2015-03-24T06:02:48.007Z"),
        ('updated_at', "2015-03-24T06:08:22.686Z"),
        ('application_status', "NOT_DEPLOYED"),

    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])

    return render_json_response(request, data)

def environment_detail(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('blueprint_id', "1"),
        ('name', "tomcat_environment"),
        ('description', "tomcat environment"),
        ('status', "CREATE_COMPLETE"),
        ('ip_address', "xx.xx.xx.xx"),
        ('created_at', "2015-03-24T06:02:48.007Z"),
        ('updated_at', "2015-03-24T06:08:22.686Z"),
        ('application_status', "NOT_DEPLOYED"),

    ])

    return render_json_response(request, dict)

def environment_create(request):

    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('blueprint_id', "1"),
        ('name', "tomcat_environment"),
        ('description', "tomcat environment"),
        ('status', "CREATE_COMPLETE"),
        ('ip_address', "xx.xx.xx.xx"),
        ('created_at', "2015-03-24T06:02:48.007Z"),
        ('updated_at', "2015-03-24T06:08:22.686Z"),
        ('application_status', "NOT_DEPLOYED"),

    ])

    return render_json_response(request, dict)

def environment_update(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('blueprint_id', "1"),
        ('name', "tomcat_environment"),
        ('description', "tomcat environment"),
        ('status', "CREATE_COMPLETE"),
        ('ip_address', "xx.xx.xx.xx"),
        ('created_at', "2015-03-24T06:02:48.007Z"),
        ('updated_at', "2015-03-24T06:08:22.686Z"),
        ('application_status', "NOT_DEPLOYED"),

    ])

    return render_json_response(request, dict)

def environment_delete(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('blueprint_id', "1"),
        ('name', "tomcat_environment"),
        ('description', "tomcat environment"),
        ('status', "CREATE_COMPLETE"),
        ('ip_address', "xx.xx.xx.xx"),
        ('created_at', "2015-03-24T06:02:48.007Z"),
        ('updated_at', "2015-03-24T06:08:22.686Z"),
        ('application_status', "NOT_DEPLOYED"),

    ])

    return render_json_response(request, dict)

def environment_event_list(request, id):
# 修正
    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('blueprint_id', "1"),
        ('name', "tomcat_environment"),
        ('description', "tomcat environment"),
        ('status', "CREATE_COMPLETE"),
        ('ip_address', "xx.xx.xx.xx"),
        ('created_at', "2015-03-24T06:02:48.007Z"),
        ('updated_at', "2015-03-24T06:08:22.686Z"),
        ('application_status', "NOT_DEPLOYED"),

    ])

    return render_json_response(request, dict)

def environment_event(request, id):
# 修正
    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('blueprint_id', "1"),
        ('name', "tomcat_environment"),
        ('description', "tomcat environment"),
        ('status', "CREATE_COMPLETE"),
        ('ip_address', "xx.xx.xx.xx"),
        ('created_at', "2015-03-24T06:02:48.007Z"),
        ('updated_at', "2015-03-24T06:08:22.686Z"),
        ('application_status', "NOT_DEPLOYED"),

    ])

    return render_json_response(request, dict)

def environment_send_event(request, id):
# 修正
    dict = OrderedDict([
        ('event_id', "d15ed933-94de-ac39-3c66-e8cc87de93be"),

    ])

    return render_json_response(request, dict)

def environment_rebuild(request, id):
# 修正
    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('blueprint_id', "1"),
        ('name', "tomcat_environment"),
        ('description', "tomcat environment"),
        ('status', "CREATE_COMPLETE"),
        ('ip_address', "xx.xx.xx.xx"),
        ('created_at', "2015-03-24T06:02:48.007Z"),
        ('updated_at', "2015-03-24T06:08:22.686Z"),
        ('application_status', "NOT_DEPLOYED"),

    ])

    return render_json_response(request, dict)
