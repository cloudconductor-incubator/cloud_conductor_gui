# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from ..forms import loginForm
from ..enum import ApiClass
from ..enum import ResponseType
from ..enum.FunctionCode import Common
from django.core.exceptions import ValidationError
from ..utils import ValiUtil
from .import roleViews
from ..logs import log

class Path():
    top = "/ccgui/top/"
    list = "/ccgui/project/list/"
    detail = lambda nid: "/ccgui/project/{0}/".format(nid)
    edit = lambda nid: "/ccgui/project/{0}/edit".format(nid)

# Create your views here.
def login(request):
    try:
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
                msg = ValiUtil.valiCheck(form)
                return render(request, "gui_app/login.html", {'message':msg })

            #-- TokenAPI call, get a response
            url = ApiClass.Token.token.value
            data = {'email' : p['email'], 'password' : p['password'] }
            r = requests.get(url, data)
            #-- get response
            if r.status_code != ResponseType.Response.OK.value:

                return render(request, "gui_app/login.html", {'message':r.text })


            t = json.loads(r.text)
            token = t['auth_token']
            request.session['auth_token'] = token

            #-- roleAPI call, get a response
#             r = requests.get(url, data)
#             if r.status_code == ResponseType.Response.OK.value:
#                 t = json.loads(r.text)
#                 token = t['auth_token']
#                 return redirect(Path.top)
#             else:
#
#                 return render(request, "gui_app/login.html")

            #-- projectAPI call, get a response
            p_url = ApiClass.Project.list.value
            data = {'auth_token' : request.session['auth_token']}
            preq = requests.get(p_url, data)
            log.info(Project.list.value, role, None, Message.api_url.value)
            #-- token acquisition
            if preq.status_code != ResponseType.Response.OK.value:
                log.info(Project.list.value, role, None, Message.api_url.value)
                return render(request, "gui_app/login.html", {'message':preq.text })

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
    except Exception as ex:
        log.error(Common.top.value, None, ex)
        return render(request, "gui_app/login.html", {"message": str(ex) })

def logout(request):
    # session delete
    request.session.clear()
    return render(request, "gui_app/login.html", {'message':'' })

