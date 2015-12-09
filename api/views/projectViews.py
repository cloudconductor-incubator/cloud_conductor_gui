from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from api.views.commonViews import render_json_response

def project_list(request):

    projects = []

    dict = OrderedDict([
        ('id', "1"),
        ('name', "sample_project"),
        ('description', "sample_project_description"),
        ('created_at', "2015-03-24T01:26:41.224Z"),
        ('updated_at', "2015-03-24T01:26:41.224Z"),
   ])

    dict.updata = OrderedDict([
        ('id', "2"),
        ('name', "sample_project"),
        ('description', "sample_project_description"),
        ('created_at', "2015-03-24T01:26:41.224Z"),
        ('updated_at', "2015-03-24T01:26:41.224Z"),
   ])
    projects.append(dict)

    data = OrderedDict([ ('projects', projects) ])

    return render_json_response(request, data)

def project_detail(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('name', "sample_project"),
        ('description', "sample_project_description"),
        ('created_at', "2015-03-24T01:26:41.224Z"),
        ('updated_at', "2015-03-24T01:26:41.224Z"),
    ])

    return render_json_response(request, dict)

def project_create(request):

    dict = OrderedDict([
        ('id', "1"),
        ('name', "sample_project"),
        ('description', "sample_project_description"),
        ('created_at', "2015-03-24T01:26:41.224Z"),
        ('updated_at', "2015-03-24T01:26:41.224Z"),
    ])

    return render_json_response(request, dict)

def project_update(request, id):

    dict = OrderedDict([
        ('id', id),
        ('name', "sample_project"),
        ('description', "sample_project_description"),
        ('created_at', "2015-03-24T01:26:41.224Z"),
        ('updated_at', "2015-03-24T01:26:41.224Z"),
    ])

    return render_json_response(request, dict)

def project_delete(request, id):

    dict = OrderedDict([
        ('id', id),
        ('name', "sample_project"),
        ('description', "sample_project_description"),
        ('created_at', "2015-03-24T01:26:41.224Z"),
        ('updated_at', "2015-03-24T01:26:41.224Z"),
    ])

    return render_json_response(request, dict)

def assign_user_list(request):

    lists = []

    dict = OrderedDict([
        ('id', "1"),
        ('email', "admin@example.com"),
        ('name', "admin"),
        ('admin', "TRUE"),
        ('created_at', "2015-03-23T06:58:08.280Z"),
        ('updated_at', "2015-03-23T06:58:08.280Z"),
    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])

    return render_json_response(request, data)

def project_assign_user(request, id):

    lists = []

    dict = OrderedDict([
        ('id', "1"),
        ('email', "admin@example.com"),
        ('name', "admin"),
        ('admin', "TRUE"),
        ('created_at', "2015-03-23T06:58:08.280Z"),
        ('updated_at', "2015-03-23T06:58:08.280Z"),
    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])

    return render_json_response(request, data)

