from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from api.views.commonViews import render_json_response

def account_list(request):

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

def account_detail(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('email', "admin@example.com"),
        ('name', "admin"),
        ('admin', "TRUE"),
        ('created_at', "2015-03-23T06:58:08.280Z"),
        ('updated_at', "2015-03-23T06:58:08.280Z"),

    ])

    return render_json_response(request, dict)

def account_create(request):

    dict = OrderedDict([
        ('id', "1"),
        ('email', "admin@example.com"),
        ('name', "admin"),
        ('admin', "TRUE"),
        ('created_at', "2015-03-23T06:58:08.280Z"),
        ('updated_at', "2015-03-23T06:58:08.280Z"),

    ])

    return render_json_response(request, dict)

def account_update(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('email', "admin@example.com"),
        ('name', "admin"),
        ('admin', "TRUE"),
        ('created_at', "2015-03-23T06:58:08.280Z"),
        ('updated_at', "2015-03-23T06:58:08.280Z"),

    ])

    return render_json_response(request, dict)

def account_delete(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('email', "admin@example.com"),
        ('name', "admin"),
        ('admin', "TRUE"),
        ('created_at', "2015-03-23T06:58:08.280Z"),
        ('updated_at', "2015-03-23T06:58:08.280Z"),

    ])

    return render_json_response(request, dict)