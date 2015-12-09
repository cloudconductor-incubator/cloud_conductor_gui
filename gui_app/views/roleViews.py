# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect

def roleChange(request, id):

    roleUrl = 'http://127.0.0.1:8000/api/v1/role/' +id+ '/menu/'
    role = requests.get(roleUrl)
    role_munu = json.loads(role.text)

    request.session['id'] = role_munu['id']
    request.session['role_id'] = role_munu['role_id']
    request.session['ac_name'] = role_munu['ac_name']
    request.session['pj_pulldown'] = role_munu['pj_pulldown']
    request.session['m_project'] = role_munu['m_project']
    request.session['m_cloud'] = role_munu['m_cloud']
    request.session['m_provisionning'] = role_munu['m_provisionning']
    request.session['m_support'] = role_munu['m_support']
    request.session['w_cloud_registrarion'] = role_munu['w_cloud_registrarion']
    request.session['w_make_new_app'] = role_munu['w_make_new_app']
    request.session['w_app_env'] = role_munu['w_app_env']
    request.session['w_deploying_app'] = role_munu['w_deploying_app']

    roleUrl = 'http://127.0.0.1:8000/api/v1/role/' +id+ '/project/'
    role = requests.get(roleUrl)
    role_munu = json.loads(role.text)

    request.session['project_list'] = role_munu['project_list']
    request.session['project_detail'] = role_munu['project_detail']
    request.session['project_create'] = role_munu['project_create']
    request.session['project_edit'] = role_munu['project_edit']
    request.session['project_delete'] = role_munu['project_delete']
    request.session['add_user'] = role_munu['add_user']

    return redirect('/ccgui')

def index(request):
    return render(request, "gui_app/role/role.html")

