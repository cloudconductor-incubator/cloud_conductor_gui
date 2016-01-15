# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from ..forms import systemForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..logs import log


def systemList(request):
    try:
        systems = None
        # -- Get a system list, API call
        url = Url.systemList
        print(url)

        data = {'auth_token': request.session['auth_token']}
        systems = ApiUtil.requestGet(url, FuncCode.systemList.value, data)
#         systems = systems['lists']

        return render(request, Html.systemList, {'system': systems, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.systemList.value, None, ex)

        return render(request, Html.systemList, {"system": '', 'message': str(ex)})

    return render(request, Html.systemList, {'system': '', 'baseImage': '', 'message': ex})


def systemDetail(request, id):
    try:
        # -- system DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.systemDetail(id, Url.url)
        data = {
            'auth_token': token
        }
        p = ApiUtil.requestGet(url, FuncCode.systemDetail.value, data)

        return render(request, Html.systemDetail, {'system': p, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.systemDetail.value, None, ex)

        return render(request, Html.systemDetail, {'system': '', 'message': str(ex)})


def systemCreate(request):
    try:
        if request.method == "GET":
            data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }
            return render(request, Html.systemCreate, {'system': data, 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = systemForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)

                return render(request, Html.systemCreate, {'system': p, 'message': msg})

            # -- Create a system, api call
            url = Url.systemCreate
            data = {
                'auth_token': request.session['auth_token'],
                'project_id': p['project_id'],
                'name': p['name'],
                'description': p['description'],
                'domain': p['domain'],
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.systemCreate.value, data)

            return redirect(Path.systemList)
    except Exception as ex:
        p = request.POST
        log.error(FuncCode.systemCreate.value, None, ex)

        return render(request, Html.systemCreate, {'system': p, "message": str(ex)})


def systemEdit(request, id):
    try:
        if request.method == "GET":

            url = Url.systemDetail(id, Url.url)

            data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }
            p = ApiUtil.requestGet(url, FuncCode.systemEdit.value, data)
            p.update(data)

            return render(request, Html.systemEdit, {'system': p, 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = systemForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.systemEdit, {'system': p, 'message': msg})

            # -- Create a system, api call
            url = Url.systemEdit(id, Url.url)
            data = {
                'auth_token': request.session['auth_token'],
                'project_id': p['project_id'],
                'name': p['name'],
                'description': p['description'],
                'domain': p['domain'],
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, FuncCode.systemEdit.value, data)

            return redirect(Path.systemList)
    except Exception as ex:
        log.error(FuncCode.systemEdit.value, None, ex)

        return render(request, Html.systemEdit, {'system': request.POST, "message": str(ex)})


def systemDelete(request, id):
    try:
        # -- URL and data set
        url = Url.systemDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.systemDelete.value, data)

        return redirect(Path.systemList)
    except Exception as ex:
        log.error(FuncCode.systemDelete.value, None, ex)

        return render(request, Html.systemDetail, {'system': '', 'message': ex})
