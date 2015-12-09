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
from ..enum.FunctionCode import FuncCode
from django.core.exceptions import ValidationError
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils.ApiUtil import Url
from .import roleViews
from ..logs import log

# Create your views here.
def login(request):
    try:
        if request.method == "GET":
            return render(request, Html.login, {'message': ''})
        else:
            #-- Get a value from a form

            msg = ''
            p = request.POST
            #-- Validate check
            form = loginForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.login, {'message': msg})

            #-- TokenAPI call, get a response
            url = Url.token
            data = {'email' : p['email'], 'password' : p['password'] }
            t = ApiUtil.requestGet(url, FuncCode.login.value, data)
            # -- Add the token to the session
            token = t['auth_token']
            request.session['auth_token'] = token


            #-- ProjectListAPI call, get a response
            projectUrl = Url.projectList
            data = {'auth_token': token}
            projectList = ApiUtil.requestGet(projectUrl, FuncCode.login.value, data)

            request.session['project_id'] = '1'

#             for project, p1 in projectList.items():
#                 dict(p1)
#                 print(project, p1)
#
#
#             print(projectList)

            return redirect(Path.top)
#             return render(request, Html.login)

            #-- djagoログイン処理
    #         if user and user.is_active:
    #             auth.login(request, user)
    #             return redirect(Path.view)
    #         else:
    #             raise Exception("アクティブなユーザーではありません")
    except Exception as ex:
        log.error(Common.top.value, None, ex)
        return render(request, Html.login, {"message": str(ex) })

def logout(request):
    # session delete
    request.session.clear()
    return render(request, "gui_app/login.html", {'message':'' })

