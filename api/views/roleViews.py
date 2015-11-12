from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from api.views.commonViews import render_json_response

def role_menu(request, id):
    if id == '1': # super user
        dict = OrderedDict([
            ('id', "1"),
            ('role_id', "1"),
            ('ac_name', "super name"),
            ('pj_pulldown', "1"),
            ('m_project', "1"),
            ('m_cloud', "1"),
            ('m_provisionning', "1"),
            ('m_support', "1"),
            ('w_cloud_registrarion', "1"),
            ('w_make_new_app', "1"),
            ('w_app_env', "1"),
            ('w_deploying_app', "1"),
        ])
    elif id == '2': # PJ
        dict = OrderedDict([
            ('id', "2"),
            ('role_id', "2"),
            ('ac_name', "PJ admin"),
            ('pj_pulldown', "1"),
            ('m_project', "1"),
            ('m_cloud', "1"),
            ('m_provisionning', "0"),
            ('m_support', "1"),
            ('w_cloud_registrarion', "1"),
            ('w_make_new_app', "0"),
            ('w_app_env', "0"),
            ('w_deploying_app', "0"),
        ])
    elif id == '3': #PJ
        dict = OrderedDict([
            ('id', "3"),
            ('role_id', "3"),
            ('ac_name', "user"),
            ('pj_pulldown', "0"),
            ('m_project', "0"),
            ('m_cloud', "0"),
            ('m_provisionning', "1"),
            ('m_support', "0"),
            ('w_cloud_registrarion', "0"),
            ('w_make_new_app', "0"),
            ('w_app_env', "1"),
            ('w_deploying_app', "1"),
        ])
    else:
        dict = None

    return render_json_response(request, dict)


