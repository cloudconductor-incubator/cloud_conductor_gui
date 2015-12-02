# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from api.views.projectViews import project_list
from ..forms import t_projectForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..enum import ApiClass
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import Project
from ..logs import log
from django.core.exceptions import ValidationError

class Path():
    top = "/ccgui/top/"
    list = "/ccgui/project/list/"
    create = "/gui_app/project/projectCreate.html"
    detail = lambda nid: "/ccgui/project/{0}/".format(nid)
    edit = lambda nid: "/ccgui/project/{0}/edit".format(nid)

# CloudConductor add
def projectList(request):
    try:
        r = None
        url = ApiClass.Project.list.value
        r = requests.get(url)
        log.info(Project.list.value, r, None, Message.api_url.value)

        # role
        roleUrl = 'http://127.0.0.1:8000/api/v1/role/2/menu/'
        role = requests.get(roleUrl)
        role_munu = json.loads(role.text)
        log.info(Project.list.value, role, None, Message.api_url.value)

        if r.reason == ResponseType.Response.OK.name:
            # json
            log.info(Project.list.value, None, r.text, Message.api_response.value)
            p = json.loads(r.text)
            projects = p['projects']
        else:
            log.error(Project.list.value, r, None)
            projects = None

        return render(request, "gui_app/project/projectList.html", {"projects": projects, 'role_munu':role_munu, 'message':'' })
    except Exception as ex:
        log.error(Project.list.value, None, ex)
        return render(request, "gui_app/project/projectList.html", {"projects": '', 'message':str(ex) })

def projectCreate(request):
    if request.method == "GET":

        return render(request, "gui_app/project/projectCreate.html", {'message':''})
    else:
        try:
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
            log.info(Project.create.value, r, None, Message.api_url.value)

            #-- if response is "OK"
            if r.reason == ResponseType.Response.OK.name:
                log.info(Project.create.value, None, r.text, Message.api_response.value)
                return redirect(Path.list)
            else:
                log.error(Project.create.value, r, None)
                return render(request, "gui_app/project/projectCreate.html", {'project': p, 'message':msg })

        except Exception as ex:
            log.error(Project.create.value, None, ex)

            return render(request, "gui_app/project/projectCreate.html", {'project':p, "message": str(ex) })

def projectEdit(request, id=None):
    try:
        if request.method == "GET":

            url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/detail/'
            r = requests.get(url)
            log.info(Project.edit.value, r, None, Message.api_url.value)

            p = json.loads(r.text)
            log.info(Project.edit.value, None, r.text, Message.api_response.value)
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
            log.info(Project.edit.value, r, None, Message.api_url.value)
            #-- if response is "OK"
            if r.reason == ResponseType.Response.OK.name:
                log.info(Project.edit.value, None, r.text, Message.api_response.value)
                return redirect(Path.list)
            else:
                #-- get message?
                log.error(Project.edit.value, r, None)
                return render(request, "gui_app/project/projectCreate.html", {'project': p, 'message':msg })
    except Exception as ex:

        log.error(Project.edit.value, None, ex)
        return render(request, "gui_app/project/projectEdit.html", {'project':'', 'message':ex })

def projectDetail(request, id):
    try:
        url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/detail/'
        r = requests.get(url)
        log.info(Project.detail.value, r, None, Message.api_url.value)
        p = json.loads(r.text)

        #-- AccountAPI call, get a response
        url2 = ApiClass.Account.list.value
        data = {'token' : 'tokenken'}
        ac = requests.get(url2, data)
        log.info(Project.detail.value, ac, None, Message.api_url.value)
        #-- get response
        if r.status_code == ResponseType.Response.OK.value:
            a = json.loads(ac.text)
            log.info(Project.detail.value, None, ac.text, Message.api_response.value)

            return render(request, "gui_app/project/projectDetail.html",{'project':p, 'accounts':a['lists'], 'message':''} )
        else:
            log.error(Project.detail.value, r, None)
            return render(request, "gui_app/project/projectDetail.html",{'project':'', 'accounts':'', 'message':''} )
    except Exception as ex:
        log.error(Project.detail.value, None, ex)
        return render(request, "gui_app/project/projectDetail.html",{'project':'', 'accounts':'', 'message':ex} )


def projectDelete(request, id):
    try:
        #-- Get a value from a form
        p = request.POST
        #-- Validate check

        #-- URL and data set
    #     url = ApiClass.Project.delete.value
        url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/delete/'
        data = {'auth_token' : 'auth_token'}
        r = requests.get(url, data) # requests.delete(url, data)
        log.info(Project.delete.value, r, None, Message.api_url.value)

        if r.status_code == ResponseType.Response.OK.value:
            return redirect(Path.list)
        else:
            log.error(Project.delete.value, r, None)
            #-- Validate Error message

            return render(request, "gui_app/project/projectDetail.html",{'project':p, 'accounts':'', 'message':''} )
    except Exception as ex:
        log.error(Project.edit.value, None, ex)
        return render(request, "gui_app/project/projectDetail.html",{'project':'', 'accounts':'', 'message':ex} )

def projectAddUser(request, id):

    return render(request, "gui_app/project/projectAddUser.html" )
