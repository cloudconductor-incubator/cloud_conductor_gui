# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from api.views.projectViews import project_list
from .forms import t_projectForm
from .enum import ApiClass
from .enum import ResponseType


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
    return render(request, "gui_app/top.html")

def index(request):
    return render(request, "gui_app/index.html")

# CloudConductor add
def projectList(request):
    url = ApiClass.Project.list.value
    r = requests.get(url)

    if r.reason == ResponseType.Response.OK.name:
        # json
        res = json.loads(r.text)
        projects = res['projects']
    else:
        projects = None

    return render(request, "gui_app/project/projectList.html", {"projects": projects})

def projectCreate(request):
    if request.method == "GET":
        return render(request, "gui_app/project/projectCreate.html")
    else:

        return redirect(Path.list)

def projectEdit(request, id=None):
    if request.method == "GET":
        url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/detail/'
        r = requests.get(url)
        p = json.loads(r.text)

        return render(request, "gui_app/project/projectEdit.html", {"project": {'id':p['id'], 'name':p['name'], 'description':p['description']}, 'project2':t_projectForm })
    else:

        #-- formから値を取得
        p = request.POST

        #-- Validate check

        #-- URL set
        if p['id'] == None:
            url = ApiClass.Project.create.value
        else:
            url = ApiClass.Project.edit.value

        #-- ProjectEditAPIにformの値をセットする
        data = {'auth_token' : 'auth_token', 'name' : p['name'], 'description' : p['description'] }
        r = requests.get(url, data)
        #-- 呼出、responseを取得する
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

    return redirect(Path.list)
