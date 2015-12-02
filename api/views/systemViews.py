from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from api.views.commonViews import render_json_response

def system_list(request):

    lists = []

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('primary_environment_id', " null"),
        ('name', " tomcat_system"),
        ('description', " tomcat system"),
        ('domain', " sample.dev.cloudconductor.jp"),
        ('created_at', " 2015-03-24T05:18:00.950Z"),
        ('updated_at', " 2015-03-24T05:18:00.950Z"),

    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])

    return render_json_response(request, data)

def system_detail(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('primary_environment_id', " null"),
        ('name', " tomcat_system"),
        ('description', " tomcat system"),
        ('domain', " sample.dev.cloudconductor.jp"),
        ('created_at', " 2015-03-24T05:18:00.950Z"),
        ('updated_at', " 2015-03-24T05:18:00.950Z"),

    ])

    return render_json_response(request, dict)

def system_create(request):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('primary_environment_id', " null"),
        ('name', " tomcat_system"),
        ('description', " tomcat system"),
        ('domain', " sample.dev.cloudconductor.jp"),
        ('created_at', " 2015-03-24T05:18:00.950Z"),
        ('updated_at', " 2015-03-24T05:18:00.950Z"),

    ])

    return render_json_response(request, dict)

def system_update(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('primary_environment_id', " null"),
        ('name', " tomcat_system"),
        ('description', " tomcat system"),
        ('domain', " sample.dev.cloudconductor.jp"),
        ('created_at', " 2015-03-24T05:18:00.950Z"),
        ('updated_at', " 2015-03-24T05:18:00.950Z"),

    ])

    return render_json_response(request, dict)

def system_delete(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('primary_environment_id', " null"),
        ('name', " tomcat_system"),
        ('description', " tomcat system"),
        ('domain', " sample.dev.cloudconductor.jp"),
        ('created_at', " 2015-03-24T05:18:00.950Z"),
        ('updated_at', " 2015-03-24T05:18:00.950Z"),

    ])

    return render_json_response(request, dict)

def system_switch(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('primary_environment_id', " null"),
        ('name', " tomcat_system"),
        ('description', " tomcat system"),
        ('domain', " sample.dev.cloudconductor.jp"),
        ('created_at', " 2015-03-24T05:18:00.950Z"),
        ('updated_at', " 2015-03-24T05:18:00.950Z"),

    ])

    return render_json_response(request, dict)
