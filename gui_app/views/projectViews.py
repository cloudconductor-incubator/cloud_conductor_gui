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
from ..forms import t_projectForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..enum import ApiClass
from ..enum import ResponseType
from logging import getLogger
from django.core.exceptions import ValidationError
# logger = getLogger(__name__)
logger = getLogger('app')

class Path():
    top = "/ccgui/top/"
    list = "/ccgui/project/list/"
    detail = lambda nid: "/ccgui/project/{0}/".format(nid)
    edit = lambda nid: "/ccgui/project/{0}/edit".format(nid)

# CloudConductor add
def projectList(request):
    url = ApiClass.Project.list.value
    r = requests.get(url)
    logger.info( "LogTEST：OK！" )
    logger.warning("warning")
    # role
    roleUrl = 'http://127.0.0.1:8000/api/v1/role/2/menu/'
    role = requests.get(roleUrl)
    role_munu = json.loads(role.text)

    if r.reason == ResponseType.Response.OK.name:
        # json
        p = json.loads(r.text)
        projects = p['projects']

        logger.info( "LogTEST：OK！" )

    else:
        projects = None

    return render(request, "gui_app/project/projectList.html", {"projects": projects, 'role_munu':role_munu })

def projectCreate(request):
    if request.method == "GET":

        form = t_projectForm()
        return render(request, "gui_app/project/projectCreate.html", {'message':''})
    else:

        #-- Get a value from a form
        msg = ''
        p = request.POST
        #-- Validate check
        form = t_projectForm(request.POST)
        form.full_clean()
        if not form.is_valid():
            msg = ValiUtil.valiCheck(form)
            return render(request, "gui_app/project/projectCreate.html", {'project': p, 'message':msg })

        #-- URL set
        url = ApiClass.Project.create.value
        data = {'auth_token':'auth_token', 'name':p['name'], 'description':p['description']}
        #-- API call, get a response
        r = requests.get(url, data)
        #-- if response is "OK"
        if r.reason == ResponseType.Response.OK.name:
            return redirect(Path.list)
        else:

            return render(request, "gui_app/project/projectCreate.html", {'project': p, 'message':msg })

def projectEdit(request, id=None):
    if request.method == "GET":
        url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/detail/'
        r = requests.get(url)
        p = json.loads(r.text)

        return render(request, "gui_app/project/projectEdit.html", {'project': p, 'message':'' })
    else:
        #-- Get a value from a form
        p = request.POST
        msg = ''
        #-- Validate check
        form = t_projectForm(request.POST)
        form.full_clean()
        if not form.is_valid():
            msg = ValiUtil.valiCheck(form)
            return render(request, "gui_app/project/projectEdit.html", {'project': p, 'message':msg })

        #-- URL set
        url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/update/'
        #-- Set the value to the form
        data = {'auth_token':'auth_token', 'name':p['name'], 'description':p['description']}
        #-- API call, get a response
        r = requests.get(url, data)
        #-- if response is "OK"
        if r.reason == ResponseType.Response.OK.name:
            return redirect(Path.list)
        else:
            #-- get message?

            return render(request, "gui_app/project/projectCreate.html", {'project': p, 'message':msg })

def projectDetail(request, id):

    url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/detail/'
    r = requests.get(url)
    p = json.loads(r.text)

    #-- AccountAPI call, get a response
    url2 = ApiClass.Account.list.value
    data = {'token' : 'tokenken'}
    ac = requests.get(url2, data)
    #-- get response
    if r.status_code == ResponseType.Response.OK.value:
        a = json.loads(ac.text)

    return render(request, "gui_app/project/projectDetail.html",{'project':p, 'accounts':a['lists']} )

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

def projectAddUser(request, id):

    return render(request, "gui_app/project/projectAddUser.html" )
