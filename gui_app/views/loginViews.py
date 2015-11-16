# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from ..forms import loginForm
from ..enum import ApiClass
from ..enum import ResponseType
from logging import getLogger
from django.core.exceptions import ValidationError
from .import roleViews
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
        form.full_clean()
        if not form.is_valid():
            errors = form.errors.as_data()
            for k in errors:
                msg = errors[k][0].messages[0]
                break
            return render(request, "gui_app/login.html", {'message':msg})
#             raise Exception(msg)

        #-- TokenAPI call, get a response
        url = ApiClass.Token.token.value
        data = {'email' : p['email'], 'password' : p['password'] }
        r = requests.get(url, data)
        #-- get response
        if r.status_code == ResponseType.Response.OK.value:
            t = json.loads(r.text)
            token = t['auth_token']
            return redirect(Path.top)
        else:

            return render(request, "gui_app/login.html")

        #-- roleAPI call, get a response
        url = ApiClass.Token.token.value
        data = {'token' : token }
        r = requests.get(url, data)
        if r.status_code == ResponseType.Response.OK.value:
            t = json.loads(r.text)
            token = t['auth_token']
            return redirect(Path.top)
        else:

            return render(request, "gui_app/login.html")

        #-- roleMenuAPI call, get a response

        #-- token acquisition

        #-- http code acquisition
        if r.reason == ResponseType.Response.OK.name:
            t = json.loads(r.text)
            token = t['auth_token']

            return redirect(Path.top)
        else:
            return render(request, "gui_app/login.html")

        #-- djagoログイン処理
#         if user and user.is_active:
#             auth.login(request, user)
#             return redirect(Path.view)
#         else:
#             raise Exception("アクティブなユーザーではありません")




def top(request):
    # role


    return render(request, "gui_app/top.html")
