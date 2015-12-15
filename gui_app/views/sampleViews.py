# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import 《val》Form
from ..enum import ApiClass
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import 《Sample》
from ..utils import ValiUtil
from ..logs import log
from logging import getLogger
logger = getLogger('app')

class Path():
    top = "/ccgui/top/"
    list = "/ccgui/《val》/list/"
    detail = lambda nid: "/ccgui/《val》/{0}/".format(nid)
    edit = lambda nid: "/ccgui/《val》/{0}/edit".format(nid)

# Create your views here.
def 《val》List(request):
    try:
        url = ApiClass.《Sample》.list.value
        r = requests.get(url)
        log.info(《Sample》.list.value, r, None, Message.api_url.value)
        list = None
        if r.reason == ResponseType.Response.OK.name:
            log.info(《Sample》.list.value, None, r.text, Message.api_response.value)

            《val》s = json.loads(r.text)
            list = 《val》s['lists']
            return render(request, "gui_app/《val》/《val》List.html", {'《val》':list, 'message':'' })
        else:

            log.error(《Sample》.list.value, c, None)
            return render(request, "gui_app/《val》/《val》List.html", {'《val》':'', 'message':'' })
    except Exception as ex:

        log.error(《Sample》.list.value, None, ex)
        return render(request, "gui_app/《val》/《val》List.html", {'《val》':'', 'message':ex })

def 《val》Detail(request, id):
    try:
        data = {'auth_token':'token'}
        url = 'http://127.0.0.1:8000/api/v1/《val》/'+id+'/detail/'
        r = requests.get(url, data)
        log.info(《Sample》.detail.value, r, None, Message.api_url.value)


        if r.reason == ResponseType.Response.OK.name:
            log.info(《Sample》.detail.value, None, r.text, Message.api_response.value)
            《val》 = json.loads(r.text)
        else:
            log.error(《Sample》.detail.value, r, None)

        return render(request, "gui_app/《val》/《val》Detail.html", {'《val》': 《val》, 'message':'' })
    except Exception as ex:

        log.error(《Sample》.detail.value, None, ex)
        return render(request, "gui_app/《val》/《val》Detail.html", {'《val》': '', 'message':ex})


def 《val》Create(request):
    try:
        if request.method == "POST":
            #-- Get a value from a form
            p = request.POST
            #-- Validate check
            form = 《val》Form(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, "gui_app/《val》/《val》Create.html", {'《val》' : p, 'message':msg})

            #-- Call API
            url = ApiClass.《Sample》.create.value
            data = {'auth_token':'token', 'project_id':45} # session auth_token = request.session['auth_token']
            data.update(p)
            r = requests.get(url, data)
            #-- if response is "OK"
            if r.reason == ResponseType.Response.OK.name:
                return redirect(Path.list)
            else:
                #-- get message?
                log.error(《Sample》.create.value, r, None)
                return render(request, "gui_app/《val》/《val》Create.html", {'《val》' : p, 'message':msg})
        else:

            return render(request, "gui_app/《val》/《val》Create.html")
    except Exception as ex:

        log.error(《Sample》.create.value, None, ex)
        return render(request, "gui_app/《val》/《val》Create.html", {'《val》' : '', 'message':ex})

def 《val》Edit(request, id):
    try:
        if request.method == "GET":
            url = 'http://127.0.0.1:8000/api/v1/《val》/'+id+'/detail/'
            r = requests.get(url)
            log.info(《Sample》.edit.value, r, None, Message.api_url.value)

            《val》 = json.loads(r.text)
            log.info(《Sample》.edit.value, None, r.text, Message.api_response.value)

            return render(request, "gui_app/《val》/《val》Edit.html", {'《val》' : 《val》, 'message':''})
        elif request.method == "POST":
            #-- Get a value from a form
            p = request.POST
            #-- Validate check
            data = {'auth_token':'token', 'project_id':45, 'id':1}
            data.update(p)
            form = 《val》Form(data)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                print(form.is_valid())
                return render(request, "gui_app/《val》/《val》Edit.html", {'《val》' : p, 'message':msg})

            #-- Call API
            url = 'http://127.0.0.1:8000/api/v1/《val》/'+id+'/update/'
            r = requests.get(url, data)
            log.info(《Sample》.edit.value, r, None, Message.api_url.value)
            #-- if response is "OK"
            if r.reason == ResponseType.Response.OK.name:
#                 log.info(《Sample》.edit.value, None, r.text, Message.api_response.value)
                return redirect(Path.list)
            else:
                #-- get message?
                log.error(《Sample》.edit.value, r, None)
                return render(request, "gui_app/《val》/《val》Edit.html", {'《val》' : p, 'message':''})
        else:
            url = None
            return redirect(Path.list)
    except Exception as ex:
        log.error(《Sample》.edit.value, None, ex)

        return render(request, "gui_app/《val》/《val》Edit.html", {'《val》' : '', 'message':ex})

def 《val》Delete(request, id):
    try:
        url = 'http://127.0.0.1:8000/api/v1/《val》/'+id+'/delete/'
        r = requests.get(url)
        log.info(《Sample》.delete.value, r, None, Message.api_url.value)

        if r.reason == ResponseType.Response.OK.name:
            log.info(《Sample》.delete.value, None, r.text, Message.api_response.value)
            return redirect(Path.list)
        else:
            log.error(《Sample》.delete.value, r, None)
            return render(request, "gui_app/《val》/《val》Detail.html", {'《val》' : '', 'message':''})
    except Exception as ex:
        log.error(《Sample》.delete.value, r, None)
        return render(request, "gui_app/《val》/《val》Detail.html", {'《val》' : '', 'message':ex})

