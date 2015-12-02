from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from api.views.commonViews import render_json_response

def blueprint_list(request):

    lists = []

    dict = OrderedDict([
        ('id', "3"),
        ('project_id', "1"),
        ('name', "tomcat"),
        ('description', "tomcat pattern"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),
        ('status', "CREATE_COMPLETE"),

    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])
    return render_json_response(request, data)

def blueprint_detail(request, id):

    dict = OrderedDict([
        ('id', "3"),
        ('project_id', "1"),
        ('name', "tomcat"),
        ('description', "tomcat pattern"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),
        ('status', "CREATE_COMPLETE"),

    ])

    return render_json_response(request, dict)

def blueprint_create(request):

    dict = OrderedDict([
        ('id', "3"),
        ('project_id', "1"),
        ('name', "tomcat"),
        ('description', "tomcat pattern"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),
        ('status', "CREATE_COMPLETE"),

    ])

    return render_json_response(request, dict)

def blueprint_update(request, id):

    dict = OrderedDict([
        ('id', "3"),
        ('project_id', "1"),
        ('name', "tomcat"),
        ('description', "tomcat pattern"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),
        ('status', "CREATE_COMPLETE"),

    ])

    return render_json_response(request, dict)

def blueprint_delete(request, id):

    dict = OrderedDict([
        ('id', "3"),
        ('project_id', "1"),
        ('name', "tomcat"),
        ('description', "tomcat pattern"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),
        ('status', "CREATE_COMPLETE"),

    ])

    return render_json_response(request, dict)

def blueprint_parameters(request, id):

##あとで修正
    dict = OrderedDict([
        ('id', "3"),
        ('project_id', "1"),
        ('name', "tomcat"),
        ('description', "tomcat pattern"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),
        ('status', "CREATE_COMPLETE"),

    ])

    return render_json_response(request, dict)
