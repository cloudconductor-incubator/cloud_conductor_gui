# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from ..forms import baseImageForm
from ..enum import ApiClass
from ..enum import ResponseType
from ..utils import ValiUtil

class Path():
    top = "/ccgui/top/"
    list = "/ccgui/cloud/list/"
    detail = lambda nid: "/ccgui/cloud/{0}/".format(nid)
    edit = lambda nid: "/ccgui/cloud/{0}/edit".format(nid)

# Create your views here.
def baseImageDetail(request, id):
    url = 'http://127.0.0.1:8000/api/v1/baseImage/'+id+'/detail/'
    r = requests.get(url)
    baseImage = json.loads(r.text)

    return render(request, "gui_app/baseImage/baseImageDetail.html", {'baseImage': baseImage })

def baseImageCreate(request):
    if request.method == "POST":
    #-- Get a value from a form
        p = request.POST
        #-- Validate check
        form = baseImageForm(p)
        form.full_clean()
        if not form.is_valid():
            msg = ValiUtil.valiCheck(form)
            return render(request, "gui_app/baseImage/baseImageCreate.html", {'baseImage' : p, 'message':msg})

        #-- API call, get a response
        url = ApiClass.BaseImage.create.value
        r = requests.get(url)
        #-- if response is "OK"
        if r.reason == ResponseType.Response.OK.name:
            return redirect(Path.list)
        else:
            #-- get message?

            return redirect(Path.list)

    else:

        return render(request, "gui_app/baseImage/baseImageCreate.html")

def baseImageEdit(request, id):
    if request.method == "GET":
        url = 'http://127.0.0.1:8000/api/v1/baseImage/'+id+'/detail/'
        r = requests.get(url)
        baseImage = json.loads(r.text)

        return render(request, "gui_app/baseImage/baseImageEdit.html", {'baseImage' : baseImage})
    elif request.method == "POST":
        #-- Get a value from a form
        p = request.POST
        #-- Validate check
        form = baseImageForm(p)
        form.full_clean()
        if not form.is_valid():
            msg = ValiUtil.valiCheck(form)
            return render(request, "gui_app/cloud/baseImageEdit.html", {'baseImage' : p, 'message':msg})

        #-- API call, get a response
        url = 'http://127.0.0.1:8000/api/v1/baseImage/'+id+'/update/'
        r = requests.get(url)
        #-- if response is "OK"
        if r.reason == ResponseType.Response.OK.name:
            return redirect(Path.list)
        else:
            return render(request, "gui_app/cloud/baseImageEdit.html", {'baseImage' : p, 'message':msg})

    else:
        url = None
        return redirect(Path.list)

def baseImageDelete(request, id):
    url = 'http://127.0.0.1:8000/api/v1/baseImage/'+id+'/delete/'
    r = requests.get(url)
    json.loads(r.text)

    return redirect(Path.list)


