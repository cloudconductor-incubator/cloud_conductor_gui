from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from api.views.commonViews import render_json_response

def application_list(request):

    lists = []

    dict = OrderedDict([
        ('id', "1"),

    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])

    return render_json_response(request, data)

def application_detail(request, id):

    dict = OrderedDict([
        ('id', "1"),

    ])

    return render_json_response(request, dict)

def application_create(request):

    dict = OrderedDict([
        ('id', "1"),

    ])

    return render_json_response(request, dict)

def application_update(request, id):

    dict = OrderedDict([
        ('id', id),

    ])

    return render_json_response(request, dict)

def application_delete(request, id):

    dict = OrderedDict([
        ('id', id),

    ])

    return render_json_response(request, dict)


