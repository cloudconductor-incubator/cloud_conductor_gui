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
        ('system_id', "1"),
        ('name', "jpetstore"),
        ('description', "jpetstore"),
        ('domain', "null"),
        ('created_at', "2015-03-24T06:28:56.156Z"),
        ('updated_at', "2015-03-24T06:28:56.156Z"),
    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])

    return render_json_response(request, data)

def application_detail(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('name', "jpetstore"),
        ('description', "jpetstore"),
        ('domain', "null"),
        ('created_at', "2015-03-24T06:28:56.156Z"),
        ('updated_at', "2015-03-24T06:28:56.156Z"),

    ])

    return render_json_response(request, dict)

def application_create(request):

    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('name', "jpetstore"),
        ('description', "jpetstore"),
        ('domain', "null"),
        ('created_at', "2015-03-24T06:28:56.156Z"),
        ('updated_at', "2015-03-24T06:28:56.156Z"),

    ])

    return render_json_response(request, dict)

def application_update(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('name', "jpetstore"),
        ('description', "jpetstore"),
        ('domain', "null"),
        ('created_at', "2015-03-24T06:28:56.156Z"),
        ('updated_at', "2015-03-24T06:28:56.156Z"),

    ])

    return render_json_response(request, dict)

def application_delete(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('system_id', "1"),
        ('name', "jpetstore"),
        ('description', "jpetstore"),
        ('domain', "null"),
        ('created_at', "2015-03-24T06:28:56.156Z"),
        ('updated_at', "2015-03-24T06:28:56.156Z"),

    ])

    return render_json_response(request, dict)

def application_deploy(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('environment_id', "1"),
        ('application_history_id', "1"),
        ('status', " PROGRESS  "),
        ('created_at', " 2015-03-24T06:30:13.631Z  "),
        ('updated_at', " 2015-03-24T06:30:13.631Z "),

    ])

    return render_json_response(request, dict)

def application_history_list(request):

    lists = []

    dict = OrderedDict([
        ('id', "1"),
        ('application_id', "1"),
        ('type', "dynamic"),
        ('version', "20150324-001"),
        ('protocol', "http"),
        ('url', "https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore.war"),
        ('revision', "master"),
        ('pre_deploy', "null"),
        ('post_deploy', "null"),
        ('parameters', "{\"migration\": {\"type\": \"sql\", \"url\": \"https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore_postgres.sql\"}}"),
        ('created_at', "2015-03-24T06:29:09.528Z"),
        ('updated_at', "2015-03-24T06:29:09.528Z"),

    ])
    lists.append(dict)

    data = OrderedDict([ ('lists', lists) ])

    return render_json_response(request, data)

def application_history_detail(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('application_id', "1"),
        ('type', "dynamic"),
        ('version', "20150324-001"),
        ('protocol', "http"),
        ('url', "https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore.war"),
        ('revision', "master"),
        ('pre_deploy', "null"),
        ('post_deploy', "null"),
        ('parameters', "{\"migration\": {\"type\": \"sql\", \"url\": \"https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore_postgres.sql\"}}"),
        ('created_at', "2015-03-24T06:29:09.528Z"),
        ('updated_at', "2015-03-24T06:29:09.528Z"),

    ])

    return render_json_response(request, dict)

def application_history_create(request):

    dict = OrderedDict([
        ('id', "1"),
        ('application_id', "1"),
        ('type', "dynamic"),
        ('version', "20150324-001"),
        ('protocol', "http"),
        ('url', "https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore.war"),
        ('revision', "master"),
        ('pre_deploy', "null"),
        ('post_deploy', "null"),
        ('parameters', "{\"migration\": {\"type\": \"sql\", \"url\": \"https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore_postgres.sql\"}}"),
        ('created_at', "2015-03-24T06:29:09.528Z"),
        ('updated_at', "2015-03-24T06:29:09.528Z"),

    ])

    return render_json_response(request, dict)

def application_history_update(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('application_id', "1"),
        ('type', "dynamic"),
        ('version', "20150324-001"),
        ('protocol', "http"),
        ('url', "https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore.war"),
        ('revision', "master"),
        ('pre_deploy', "null"),
        ('post_deploy', "null"),
        ('parameters', "{\"migration\": {\"type\": \"sql\", \"url\": \"https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore_postgres.sql\"}}"),
        ('created_at', "2015-03-24T06:29:09.528Z"),
        ('updated_at', "2015-03-24T06:29:09.528Z"),

    ])

    return render_json_response(request, dict)

def application_history_delete(request, id):

    dict = OrderedDict([
        ('id', "1"),
        ('application_id', "1"),
        ('type', "dynamic"),
        ('version', "20150324-001"),
        ('protocol', "http"),
        ('url', "https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore.war"),
        ('revision', "master"),
        ('pre_deploy', "null"),
        ('post_deploy', "null"),
        ('parameters', "{\"migration\": {\"type\": \"sql\", \"url\": \"https://s3-ap-northeast-1.amazonaws.com/cloudconductor-test/sources/public/jpetstore_postgres.sql\"}}"),
        ('created_at', "2015-03-24T06:29:09.528Z"),
        ('updated_at', "2015-03-24T06:29:09.528Z"),

    ])

    return render_json_response(request, dict)