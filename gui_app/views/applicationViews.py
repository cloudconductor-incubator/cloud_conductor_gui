# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from ..forms import applicationForm
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


def applicationList(request):
    try:
        applications = None
        # -- Get a application list, API call
        url = Url.applicationList
        print(url)

        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }
        apps = ApiUtil.requestGet(url, FuncCode.applicationList.value, data)
#         apps = apps['lists']

        return render(request, Html.applicationList, {'apps': apps, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.applicationList.value, None, ex)

        return render(request, Html.applicationList, {"application": '', 'message': str(ex)})

    return render(request, "gui_app/application/applicationDetail.html", {'apps': '', 'baseImage': '', 'message': ex})


def applicationDetail(request, id):
    try:
        # -- application DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.applicationDetail(id, Url.url)
        data = {
            'auth_token': token
        }
        p = ApiUtil.requestGet(url, FuncCode.applicationDetail.value, data)

        return render(request, Html.applicationDetail, {'app': p, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.applicationDetail.value, None, ex)

        return render(request, Html.applicationDetail, {'app': '', 'message': str(ex)})


def applicationCreate(request):
    try:
        data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }
        url = Url.systemList
        systems = ApiUtil.requestGet(url, FuncCode.systemList.value, data)
#         systems = systems['lists']

        if request.method == "GET":

            data.update({
                'systems': systems,
            })

            return render(request, Html.applicationCreate, {'app': data, 'message': '', 'systems': systems})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            cpPost = p.copy()

            # -- Validate check
            form = applicationForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                cpPost.update({
                    'systems': systems,
                })
                return render(request, Html.applicationCreate, {'app': cpPost, 'message': msg})

            # -- Create a application, api call
            url = Url.applicationCreate
            data = {
                'auth_token': p['auth_token'],
                'project_id': p['project_id'],
                'system_id': p['system_id'],
                'name': p['name'],
                'description': p['description'],
                'domain': p['domain']
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.applicationCreate.value, data)

            return redirect(Path.applicationList)
    except Exception as ex:
        log.error(FuncCode.applicationCreate.value, None, ex)

        return render(request, Html.applicationCreate, {'app': request.POST, "message": str(ex)})


def applicationEdit(request, id):
    try:
        if request.method == "GET":

            url = Url.applicationDetail(id, Url.url)

            data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
            }
            p = ApiUtil.requestGet(url, FuncCode.applicationEdit.value, data)
            data.update(p)

            url2 = Url.systemList
            systems = ApiUtil.requestGet(url2, FuncCode.systemList.value, data)
#             systems = systems['lists']
            data.update({
                'systems': systems,
            })
            print(data)

            return render(request, Html.applicationEdit, {'app': data, 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = applicationForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                print(p)
                return render(request, Html.applicationEdit, {'app': p, 'message': msg})

            # -- Create a application, api call
            url = Url.applicationEdit(id, Url.url)
            data = {
                'auth_token': p['auth_token'],
                'project_id': p['project_id'],
                'system_id': p['system_id'],
                'name': p['name'],
                'description': p['description'],
                'domain': p['domain']
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, FuncCode.applicationEdit.value, data)

            return redirect(Path.applicationList)
    except Exception as ex:
        log.error(FuncCode.applicationEdit.value, None, ex)

        return render(request, Html.applicationEdit, {'app': request.POST, "message": str(ex)})


def applicationDelete(request, id):
    try:
        # -- URL and data set
        url = Url.applicationDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.applicationDelete.value, data)

        return redirect(Path.applicationList)
    except Exception as ex:
        log.error(FuncCode.applicationDelete.value, None, ex)

        return render(request, Html.applicationDetail, {'app': '', 'message': ex})
