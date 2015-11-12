# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from api.views.projectViews import project_list
from .forms import t_projectForm
from .util import roleUtil
from .enum import ApiClass
from .enum import ResponseType
from logging import getLogger
logger = getLogger(__name__)

class Path():
    top = "/ccgui/top/"
    list = "/ccgui/project/list/"
    detail = lambda nid: "/ccgui/project/{0}/".format(nid)
    edit = lambda nid: "/ccgui/project/{0}/edit".format(nid)

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "gui_app/login.html")
    else:

        #-- loginからemail,passwordを取得
        p = request.POST

        #-- tokenAPIに上記値をセットし、呼出
        url = ApiClass.Token.token.value
        data = {'loginid' : p['lodinid'], 'password' : p['password'] }
        r = requests.get(url, data)

        #-- responseを取得
        if r.reason == ResponseType.Response.OK.name:
            t = json.loads(r.text)
            token = t['auth_token']
        else:
            #-- バリデーション、email、もしくはpasswodの不一致によりエラー

            return render(request, "gui_app/login.html")
        #-- roleAPIにresponse値をセットする

        #-- responseを取得

        #-- roleMenuAPIにresponse値をセットする

        #-- responseを取得

        #-- cookieにtoke,role,roleMenuを保存
#         roleUtil.RoleMenu('2')

#         roleUrl = 'http://127.0.0.1:8000/api/v1/role/3/menu/'
#         role = requests.get(roleUrl)
#         role_munu = json.loads(role.text)
#
#         request.session['id'] = role_munu['id']
#         request.session['role_id'] = role_munu['role_id']
#         request.session['pj_pulldown'] = role_munu['pj_pulldown']
#         request.session['m_project'] = role_munu['m_project']
#         request.session['m_cloud'] = role_munu['m_cloud']
#         request.session['m_provisionning'] = role_munu['m_provisionning']
#         request.session['m_support'] = role_munu['m_support']
#         request.session['w_cloud_registrarion'] = role_munu['w_cloud_registrarion']
#         request.session['w_make_new_app'] = role_munu['w_make_new_app']
#         request.session['w_app_env'] = role_munu['w_app_env']
#         request.session['w_deploying_app'] = role_munu['w_deploying_app']

        #-- 画面遷移

        #-- token acquisition


        #-- http code acquisition
        if r.reason == ResponseType.Response.OK.name:
            t = json.loads(r.text)
            token = t['auth_token']

            return redirect(Path.top)
        else:


            return render(request, "gui_app/login.html")


def top(request):
    # role


    return render(request, "gui_app/top.html")

def index(request):
    return render(request, "gui_app/index.html")

# CloudConductor add
def projectList(request):
    url = ApiClass.Project.list.value
    r = requests.get(url)

    # role
    roleUrl = 'http://127.0.0.1:8000/api/v1/role/2/menu/'
    role = requests.get(roleUrl)
    role_munu = json.loads(role.text)

    if r.reason == ResponseType.Response.OK.name:
        # json
        p = json.loads(r.text)
        projects = p['projects']
    else:
        projects = None

    return render(request, "gui_app/project/projectList.html", {"projects": projects, 'role_munu':role_munu })

def projectCreate(request):
    if request.method == "GET":

        form = t_projectForm()
        return render(request, "gui_app/project/projectCreate.html")
    else:
        #-- Get a value from a form
        p = request.POST

        #-- Validate check

        #-- URL set


        return redirect(Path.list)

def projectEdit(request, id=None):
    if request.method == "GET":
#         ArticleFormSet = formset_factory(t_projectForm)
        if id != None:
            url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/detail/'
            r = requests.get(url)
            p = json.loads(r.text)
            form = t_projectForm(p)
#             p2 = ArticleFormSet()
        messages.error(request, "Error!")
        return render(request, "gui_app/project/projectEdit.html", {'project': p, 'project2':form, 'message':'' })
    else:

        #-- Get a value from a form
        p = request.POST

        #-- Validate check
        form = t_projectForm(request.POST)
        if form.is_valid():
            print('エラーなし')
            logger.debug('debug:OK')
        else:
            print('エラーデス')
            logger.debug('debug:error')


        #-- URL set
        url = ApiClass.Project.update.value

        #-- ProjectEditAPIにformの値をセットする
        data = {'auth_token':'auth_token', 'name':p['name'], 'description':p['description']}
        #-- API call, get a response
        r = requests.get(url, data)
        #-- if response is "OK"
        if r.status_code == ResponseType.Response.OK.value:

            return redirect(Path.list)
        else:
            #-- get message?

            #-- response edit

            return redirect(Path.list)


def projectDetail(request, id):

    url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/detail/'
    r = requests.get(url)
    p = json.loads(r.text)

    return render(request, "gui_app/project/projectDetail.html",{'id':p['id'], 'name':p['name'], 'description':p['description']} )

def projectDelete(request, id):

    #-- Get a value from a form
    p = request.POST
    #-- Validate check

    #-- URL and data set
#     url = ApiClass.Project.delete.value
    url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/delete/'
    data = {'auth_token' : 'auth_token'}
    r = requests.get(url, data) # requests.delete(url, data)

    if r.reason == ResponseType.Response.OK.value:
        return redirect(Path.list)
    else:
        #-- Validate Error message


        return redirect(Path.list)
