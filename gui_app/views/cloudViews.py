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
from ..utils import ValiUtil

class Path():
    top = "/ccgui/top/"
    list = "/ccgui/cloud/list/"
    detail = lambda nid: "/ccgui/cloud/{0}/".format(nid)
    edit = lambda nid: "/ccgui/cloud/{0}/edit".format(nid)

# Create your views here.
def cloudList(request):
    url = ApiClass.Cloud.list.value
    url2 = ApiClass.BaseImage.list.value
    c = requests.get(url)
    b = requests.get(url2)
    print(c.url)

    clist = None
    blist = None

    print(b.url)
    if c.reason == ResponseType.Response.OK.name:
        clouds = json.loads(c.text)
        clist = clouds['lists']

    if b.reason == ResponseType.Response.OK.name:
        baseImages = json.loads(b.text)
        blist = baseImages['lists']

    return render(request, "gui_app/cloud/cloudList.html", {'cloud':clist, 'baseImage':blist})

def cloudDetail(request, id):
    url = 'http://127.0.0.1:8000/api/v1/cloud/'+id+'/detail/'
    r = requests.get(url)
    cloud = json.loads(r.text)

    return render(request, "gui_app/cloud/cloudDetail.html", {'cloud': cloud })

def cloudCreate(request):
    if request.method == "POST":
        #-- Get a value from a form
        p = request.POST
        #-- Validate check
        form = cloudForm(p)
        form.full_clean()
        if not form.is_valid():
            msg = ValiUtil.valiCheck(form)
            return render(request, "gui_app/cloud/cloudCreate.html", {'cloud' : p, 'message':msg})

        #-- API call, get a response
        url = ApiClass.Cloud.create.value
        r = requests.get(url)
        #-- if response is "OK"
        if r.reason == ResponseType.Response.OK.name:
            return redirect(Path.list)
        else:
            #-- get message?


            return redirect(Path.list)
    else:

        return render(request, "gui_app/cloud/cloudCreate.html")

def cloudEdit(request, id):
    if request.method == "GET":
        url = 'http://127.0.0.1:8000/api/v1/cloud/'+id+'/detail/'
        r = requests.get(url)
        cloud = json.loads(r.text)

        return render(request, "gui_app/cloud/cloudEdit.html", {'cloud' : cloud})
    elif request.method == "POST":
        #-- Get a value from a form
        p = request.POST
        #-- Validate check
        form = cloudForm(p)
        form.full_clean()
        if not form.is_valid():
            msg = ValiUtil.valiCheck(form)

            return render(request, "gui_app/cloud/cloudEdit.html", {'cloud' : p, 'message':msg})

        url = 'http://127.0.0.1:8000/api/v1/cloud/'+id+'/edit/'
        r = requests.get(url)
        print(r.url)
        #-- if response is "OK"
        if r.reason == ResponseType.Response.OK.name:
            return redirect(Path.list)
        else:
            #-- get message?


            return redirect(Path.list)
    else:
        url = None
        return redirect(Path.list)

def cloudDelete(request, id):
    url = 'http://127.0.0.1:8000/api/v1/cloud/'+id+'/delete/'
    r = requests.get(url)
    json.loads(r.text)

    return redirect(Path.list)


