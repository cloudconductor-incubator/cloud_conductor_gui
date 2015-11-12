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
from ..forms import loginForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..enum import ApiClass
from ..enum import ResponseType
from logging import getLogger
from django.core.exceptions import ValidationError
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

        #-- Get a value from a form
        msg = ''
        p = request.POST

        #-- Validate check
        form = loginForm(p)

        #-- API call, get a response
        url = ApiClass.Token.token.value
        data = {'loginid' : p['lodinid'], 'password' : p['password'] }
        r = requests.get(url, data)

        #-- get response
        if r.reason == ResponseType.Response.OK.name:
            t = json.loads(r.text)
            token = t['auth_token']
        else:

            return render(request, "gui_app/login.html")
        #-- roleAPI call, get a response

        #-- roleMenuAPI call, get a response

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
