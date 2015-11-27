# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from ..forms import cloudForm
from ..enum import ApiClass
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import Cloud
from ..utils import ValiUtil
from ..logs import log
from logging import getLogger
logger = getLogger('app')

class Path():
    top = "/ccgui/top/"
    list = "/ccgui/cloud/list/"
    detail = lambda nid: "/ccgui/cloud/{0}/".format(nid)
    edit = lambda nid: "/ccgui/cloud/{0}/edit".format(nid)

# Create your views here.
def cloudList(request):
    try:
        url = ApiClass.Cloud.list.value
        c = requests.get(url)
        log.info(Cloud.list.value, c, None, Message.api_url.value)
        clist = None
        if c.reason == ResponseType.Response.OK.name:
            log.info(Cloud.list.value, None, c.text, Message.api_response.value)

            clouds = json.loads(c.text)
            clist = clouds['lists']
            return render(request, "gui_app/cloud/cloudList.html", {'cloud':clist, 'message':'' })
        else:

            log.error(Cloud.list.value, c, None)
            return render(request, "gui_app/cloud/cloudList.html", {'cloud':'', 'message':'' })
    except Exception as ex:

        log.error(Cloud.list.value, None, ex)
        return render(request, "gui_app/cloud/cloudList.html", {'cloud':'', 'message':ex })

def cloudDetail(request, id):
    try:
        data = {'auth_token':'token'}
        url = 'http://127.0.0.1:8000/api/v1/cloud/'+id+'/detail/'
        url2 = ApiClass.BaseImage.list.value
        r = requests.get(url, data)
        log.info(Cloud.detail.value, r, None, Message.api_url.value)

        b = requests.get(url2, data)
        log.info(Cloud.detail.value, b, None, Message.api_url.value)

        blist = None
        if r.reason == ResponseType.Response.OK.name:
            log.info(Cloud.detail.value, None, r.text, Message.api_response.value)
            cloud = json.loads(r.text)
        else:
            log.error(Cloud.detail.value, r, None)

        if b.reason == ResponseType.Response.OK.name:
            log.info(Cloud.detail.value, None, b.text, Message.api_response.value)
            baseImages = json.loads(b.text)
            blist = baseImages['lists']
        else:
            log.error(Cloud.create.value, b, None)

        return render(request, "gui_app/cloud/cloudDetail.html", {'cloud': cloud, 'baseImage':blist, 'message':'' })
    except Exception as ex:

        log.error(Cloud.detail.value, None, ex)
        return render(request, "gui_app/cloud/cloudDetail.html", {'cloud': '', 'baseImage':'', 'message':ex})


def cloudCreate(request):
    try:
        if request.method == "POST":
            #-- Get a value from a form
            p = request.POST
            #-- Validate check
            form = cloudForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, "gui_app/cloud/cloudCreate.html", {'cloud' : p, 'message':msg})

            #-- Call API
            url = ApiClass.Cloud.create.value
            data = {'auth_token':'token', 'project_id':45} # session auth_token = request.session['auth_token']
            data.update(p)
            r = requests.get(url, data)
            #-- if response is "OK"
            if r.reason == ResponseType.Response.OK.name:
                return redirect(Path.list)
            else:
                #-- get message?
                log.error(Cloud.create.value, r, None)
                return render(request, "gui_app/cloud/cloudCreate.html", {'cloud' : p, 'message':msg})
        else:

            return render(request, "gui_app/cloud/cloudCreate.html")
    except Exception as ex:

        log.error(Cloud.create.value, None, ex)
        return render(request, "gui_app/cloud/cloudCreate.html", {'cloud' : '', 'message':ex})

def cloudEdit(request, id):
    try:
        if request.method == "GET":
            url = 'http://127.0.0.1:8000/api/v1/cloud/'+id+'/detail/'
            r = requests.get(url)
            log.info(Cloud.edit.value, r, None, Message.api_url.value)

            cloud = json.loads(r.text)
            log.info(Cloud.edit.value, None, r.text, Message.api_response.value)

            return render(request, "gui_app/cloud/cloudEdit.html", {'cloud' : cloud, 'message':''})
        elif request.method == "POST":
            #-- Get a value from a form
            p = request.POST
            #-- Validate check
            data = {'auth_token':'token', 'project_id':45, 'id':1}
            data.update(p)
            form = cloudForm(data)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                print(form.is_valid())
                return render(request, "gui_app/cloud/cloudEdit.html", {'cloud' : p, 'message':msg})

            #-- Call API
            url = 'http://127.0.0.1:8000/api/v1/cloud/'+id+'/update/'
            r = requests.get(url, data)
            log.info(Cloud.edit.value, r, None, Message.api_url.value)
            #-- if response is "OK"
            if r.reason == ResponseType.Response.OK.name:
#                 log.info(Cloud.edit.value, None, r.text, Message.api_response.value)
                return redirect(Path.list)
            else:
                #-- get message?
                log.error(Cloud.edit.value, r, None)
                return render(request, "gui_app/cloud/cloudEdit.html", {'cloud' : p, 'message':''})
        else:
            url = None
            return redirect(Path.list)
    except Exception as ex:
        log.error(Cloud.edit.value, None, ex)

        return render(request, "gui_app/cloud/cloudEdit.html", {'cloud' : '', 'message':ex})

def cloudDelete(request, id):
    try:
        url = 'http://127.0.0.1:8000/api/v1/cloud/'+id+'/delete/'
        r = requests.get(url)
        log.info(Cloud.delete.value, r, None, Message.api_url.value)

        if r.reason == ResponseType.Response.OK.name:
            log.info(Cloud.delete.value, None, r.text, Message.api_response.value)
            return redirect(Path.list)
        else:
            log.error(Cloud.delete.value, r, None)
            return render(request, "gui_app/cloud/cloudDetail.html", {'cloud' : '', 'message':''})
    except Exception as ex:
        log.error(Cloud.delete.value, r, None)
        return render(request, "gui_app/cloud/cloudDetail.html", {'cloud' : '', 'message':ex})

