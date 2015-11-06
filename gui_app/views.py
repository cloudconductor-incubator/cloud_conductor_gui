# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from gui_app.forms import t_projectForm
import json
import requests
from api.views.projectViews import project_list
from gui_app.enum import ApiClass


class Path():
    index = "/ccgui/"
    list = "/ccgui/project/list/"
    detail = lambda nid: "/ccgui/project/{0}/".format(nid)
    edit = lambda nid: "/ccgui/project/{0}/edit".format(nid)

# Create your views here.
def login(request):
    return render(request, "gui_app/login.html")

def top(request):
    return render(request, "gui_app/top.html")

def index(request):
    return render(request, "gui_app/index.html")


# CloudConductor add
def projectList(request):
    url = ApiClass.Project.list.value

    print(url)
    r = requests.get(url)
# json decode1
    res = json.loads(r.text)
    projects = res['projects']

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

        #statesCode
        c = r.status_code
        print(c)


        return render(request, "gui_app/project/projectEdit.html", {"project": {'id':p['id'], 'name':p['name'], 'description':p['description']} })
    else:

        return redirect(Path.list)

def projectDetail(request, id):

    url = 'http://127.0.0.1:8000/api/v1/projects/'+id+'/detail/'
    r = requests.get(url)
    p = json.loads(r.text)

    #statesCode
    c = r.status_code
    print(c)

# {'menu': 'join','breads':breads,"loginname":loginname}
    return render(request, "gui_app/project/projectDetail.html",{'id':p['id'], 'name':p['name'], 'description':p['description']} )

def projectDelete(request, id):

    return redirect(Path.list)
