# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from collections import OrderedDict
from ..forms import patternForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..enum import ApiClass
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..logs import log


def patternList(request):
    try:
        patterns = None
        # -- Get a pattern list, API call
        url = Url.patternList
        print(url)

        data = {'auth_token': request.session['auth_token']}
        p = ApiUtil.requestGet(url, FuncCode.patternList.value, data)
        patterns = p['lists']

        return render(request, Html.patternList, {'patterns': patterns, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.patternList.value, None, ex)

        return render(request, Html.patternList, {"patterns": '', 'message': str(ex)})

    return render(request, "gui_app/pattern/patternDetail.html", {'patterns': '', 'baseImage': '', 'message': ex})


def patternDetail(request, id):
    try:
        # -- pattern DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.patternDetail(id, Url.url)
        data = {
            'auth_token': token
        }
        p = ApiUtil.requestGet(url, FuncCode.patternDetail.value, data)

        return render(request, Html.patternDetail, {'pattern': p, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.patternDetail.value, None, ex)

        return render(request, Html.patternDetail, {'pattern': '', 'message': str(ex)})


def patternCreate(request):
    try:
        if request.method == "GET":

            url = Url.environmentList
            p = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }
            envs = ApiUtil.requestGet(url, FuncCode.patternCreate.value, p)

            return render(request, Html.patternCreate, {'pattern': p, 'envs': envs['lists'], 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            print(p)

            upfile = request.FILES

            p(upfile)

            # -- Validate check
#             form = patternForm(p)
#             form.full_clean()
#             if not form.is_valid():
#                 msg = ValiUtil.valiCheck(form)
#                 return render(request, Html.patternCreate, {'pattern': p, 'message': msg})

            # -- Create a pattern, api call
            url = Url.patternCreate
            data = {
                'auth_token': request.session['auth_token'],
                'project_id': p['project_id'],
                'name': p['name'],
                'pattern_url': p['pattern_url'],
                'revision': p['revision'],
#                 'secret_key': p['secret_key'],
#                 'parameters': p['parameters'],
#                 'domain': p['domain'],
#                 'type': p['type'],
#                 'roles': p['environment']
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.patternCreate.value, data)

            return redirect(Path.patternList)
    except Exception as ex:
        log.error(FuncCode.patternCreate.value, None, ex)

        return render(request, Html.patternCreate, {'pattern': request.POST, "message": str(ex)})


def patternEdit(request, id):
    try:
        if request.method == "GET":

            url = Url.patternDetail(id, Url.url)

            data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }
            p = ApiUtil.requestGet(url, FuncCode.patternEdit.value, data)
            p.update(data)

            url2 = Url.environmentList
            envs = ApiUtil.requestGet(url2, FuncCode.patternEdit.value, data)

            return render(request, Html.patternEdit, {'pattern': p, 'envs': envs['lists'], 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = patternForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.patternEdit, {'pattern': p, 'message': msg})

            # -- Create a pattern, api call
            url = Url.patternEdit(id, Url.url)
            data = {
                'auth_token': request.session['auth_token'],
                'project_id': p['project_id'],
                'name': p['name'],
                'protocol': p['protocol'],
                'domain': p['domain'],
                'type': p['type'],
                'pattern_url': p['pattern_url'],
                'secret_key': p['secret_key'],
                'revision': p['revision'],
                'parameters': p['parameters'],
                'roles': p['environment']
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, FuncCode.patternEdit.value, data)

            return redirect(Path.patternList)
    except Exception as ex:
        log.error(FuncCode.patternEdit.value, None, ex)

        return render(request, Html.patternEdit, {'pattern': request.POST, "message": str(ex)})


def patternDelete(request, id):
    try:
        # -- URL and data set
        url = Url.patternDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.patternDelete.value, data)

        return redirect(Path.patternList)
    except Exception as ex:
        log.error(FuncCode.patternDelete.value, None, ex)

        return render(request, Html.patternDetail, {'pattern': '', 'message': ex})
