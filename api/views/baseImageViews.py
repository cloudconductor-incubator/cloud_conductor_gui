from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from api.views.commonViews import render_json_response

def baseImage_list(request):

    lists = []

    dict = OrderedDict([
        ('id', "1"),
        ('cloud_id', "1"),
        ('os', "CentOS-6.5"),
        ('source_image', "ami-xxxxxxxx"),
        ('ssh_username', "ec2-user"),
        ('created_at', "2015-03-23T07:22:34.992Z"),
        ('updated_at', "2015-03-23T07:23:41.252Z"),
    ])
    lists.append(dict)

    dict = OrderedDict([
        ('id', "2"),
        ('cloud_id', "1"),
        ('os', "CentOS-6.5"),
        ('source_image', "ami-xxxxxxxx"),
        ('ssh_username', "ec2-user"),
        ('created_at', "2015-03-23T07:22:34.992Z"),
        ('updated_at', "2015-03-23T07:23:41.252Z"),
    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])

    return render_json_response(request, data)

def baseImage_detail(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('cloud_id', "1"),
        ('os', "CentOS-6.5"),
        ('source_image', "ami-xxxxxxxx"),
        ('ssh_username', "ec2-user"),
        ('created_at', "2015-03-23T07:22:34.992Z"),
        ('updated_at', "2015-03-23T07:23:41.252Z"),

    ])

    return render_json_response(request, dict)

def baseImage_create(request):

    dict = OrderedDict([
        ('id', "1"),
        ('cloud_id', "1"),
        ('os', "CentOS-6.5"),
        ('source_image', "ami-xxxxxxxx"),
        ('ssh_username', "ec2-user"),
        ('created_at', "2015-03-23T07:22:34.992Z"),
        ('updated_at', "2015-03-23T07:23:41.252Z"),
    ])

    return render_json_response(request, dict)

def baseImage_update(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('cloud_id', "1"),
        ('os', "CentOS-6.5"),
        ('source_image', "ami-xxxxxxxx"),
        ('ssh_username', "ec2-user"),
        ('created_at', "2015-03-23T07:22:34.992Z"),
        ('updated_at', "2015-03-23T07:23:41.252Z"),

    ])

    return render_json_response(request, dict)

def baseImage_delete(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('cloud_id', "1"),
        ('os', "CentOS-6.5"),
        ('source_image', "ami-xxxxxxxx"),
        ('ssh_username', "ec2-user"),
        ('created_at', "2015-03-23T07:22:34.992Z"),
        ('updated_at', "2015-03-23T07:23:41.252Z"),

    ])

    return render_json_response(request, dict)


