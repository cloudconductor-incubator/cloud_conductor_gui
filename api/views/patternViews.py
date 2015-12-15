from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from api.views.commonViews import render_json_response

def pattern_list(request):

    patterns = []
    dict = OrderedDict([
        ('url', "https://github.com/cloudconductor-patterns/tomcat_pattern.git"),
        ('revision', "master"),
    ])
    patterns.append(dict)

    dict = OrderedDict([
        ('url', "https://github.com/cloudconductor-patterns/tomcat_pattern.git"),
        ('revision', "master"),
    ])
    patterns.append(dict)


    lists = []
    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "tomcat pattern"),
        ('protocol', "1"),
        ('type', "tomcat pattern"),
        ('pattern_url', "https://github.com/cloudconductor-incubator/cloud_conductor_gui.git"),
        ('secret_key', "tomcat pattern"),
        ('revision', "master"),
        ('parameters', "xxxxx.war"),
        ('roles', "xxxxx.war"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),
        ('patterns_attributes', patterns)

    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])
    return render_json_response(request, data)

def pattern_detail(request, id):

    patterns = []
    dict = OrderedDict([
        ('url', "https://github.com/cloudconductor-patterns/tomcat_pattern.git"),
        ('revision', "master"),
    ])
    patterns.append(dict)

    dict = OrderedDict([
        ('url', "https://github.com/cloudconductor-patterns/tomcat_pattern.git"),
        ('revision', "master"),
    ])
    patterns.append(dict)


    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "tomcat pattern"),
        ('protocol', "1"),
        ('type', "tomcat pattern"),
        ('pattern_url', "pattern_url"),
        ('secret_key', "tomcat pattern"),
        ('revision', "https://github.com/cloudconductor-incubator/cloud_conductor_gui.git"),
        ('parameters', "xxxxx.war"),
        ('patterns_attributes', patterns),
        ('roles', "xxxxx.war"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),

    ])

    return render_json_response(request, dict)

def pattern_create(request):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "tomcat pattern"),
        ('protocol', "1"),
        ('type', "tomcat pattern"),
        ('pattern_url', "pattern_url"),
        ('secret_key', "tomcat pattern"),
        ('revision', "https://github.com/cloudconductor-incubator/cloud_conductor_gui.git"),
        ('parameters', "xxxxx.war"),
        ('roles', "xxxxx.war"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),

    ])

    return render_json_response(request, dict)

def pattern_update(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "tomcat pattern"),
        ('protocol', "1"),
        ('type', "tomcat pattern"),
        ('pattern_url', "pattern_url"),
        ('secret_key', "tomcat pattern"),
        ('revision', "https://github.com/cloudconductor-incubator/cloud_conductor_gui.git"),
        ('parameters', "xxxxx.war"),
        ('roles', "xxxxx.war"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),

    ])

    return render_json_response(request, dict)

def pattern_delete(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "tomcat pattern"),
        ('protocol', "1"),
        ('type', "tomcat pattern"),
        ('pattern_url', "pattern_url"),
        ('secret_key', "tomcat pattern"),
        ('revision', "https://github.com/cloudconductor-incubator/cloud_conductor_gui.git"),
        ('parameters', "xxxxx.war"),
        ('roles', "xxxxx.war"),
        ('created_at', "2015-03-24T02:48:11.583Z"),
        ('updated_at', "2015-03-24T02:48:11.583Z"),

    ])

    return render_json_response(request, dict)
