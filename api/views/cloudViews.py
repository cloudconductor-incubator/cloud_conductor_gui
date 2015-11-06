from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from api.views.commonViews import render_json_response

def cloud_list(request):

    lists = []

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "aws_us_east_1"),
        ('description', "AWS US East"),
        ('type', "aws"),
        ('entry_point', "us-east-1"),
        ('key', "[FILTERED]"),
        ('secret', "********"),
        ('tenant_name', "null"),
        ('created_at', "2015-03-23T07:22:34.981Z"),
        ('updated_at', "2015-03-23T07:23:41.249Z"),
    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])

    return render_json_response(request, data)

def cloud_detail(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "aws_us_east_1"),
        ('description', "AWS US East"),
        ('type', "aws"),
        ('entry_point', "us-east-1"),
        ('key', "[FILTERED]"),
        ('secret', "********"),
        ('tenant_name', "null"),
        ('created_at', "2015-03-23T07:22:34.981Z"),
        ('updated_at', "2015-03-23T07:23:41.249Z"),


    ])

    return render_json_response(request, dict)

def cloud_create(request):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "aws_us_east_1"),
        ('description', "AWS US East"),
        ('type', "aws"),
        ('entry_point', "us-east-1"),
        ('key', "[FILTERED]"),
        ('secret', "********"),
        ('tenant_name', "null"),
        ('created_at', "2015-03-23T07:22:34.981Z"),
        ('updated_at', "2015-03-23T07:23:41.249Z"),


    ])

    return render_json_response(request, dict)

def cloud_update(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "aws_us_east_1"),
        ('description', "AWS US East"),
        ('type', "aws"),
        ('entry_point', "us-east-1"),
        ('key', "[FILTERED]"),
        ('secret', "********"),
        ('tenant_name', "null"),
        ('created_at', "2015-03-23T07:22:34.981Z"),
        ('updated_at', "2015-03-23T07:23:41.249Z"),


    ])

    return render_json_response(request, dict)

def cloud_delete(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('project_id', "1"),
        ('name', "aws_us_east_1"),
        ('description', "AWS US East"),
        ('type', "aws"),
        ('entry_point', "us-east-1"),
        ('key', "[FILTERED]"),
        ('secret', "********"),
        ('tenant_name', "null"),
        ('created_at', "2015-03-23T07:22:34.981Z"),
        ('updated_at', "2015-03-23T07:23:41.249Z"),

    ])

    return render_json_response(request, dict)


