# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from ..forms import environmentForm
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


def environmentList(request):
    try:
        envs = None
        # -- Get a environment list, API call
        url = Url.environmentList
        print(url)

        data = {'auth_token': request.session['auth_token']}
        p = ApiUtil.requestGet(url, FuncCode.environmentList.value, data)
        envs = p['lists']

        return render(request, Html.environmentList, {'envs': envs, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.environmentList.value, None, ex)

        return render(request, Html.environmentList, {"environment": '', 'message': str(ex)})


def environmentDetail(request, id):
    try:
        # -- environment DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.environmentDetail(id, Url.url)
        data = {
                'auth_token': token
                }
        p = ApiUtil.requestGet(url, FuncCode.environmentDetail.value, data)

        return render(request, Html.environmentDetail, {'env': p, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.environmentDetail.value, None, ex)

        return render(request, Html.environmentDetail, {'env': '', 'message': str(ex)})


def environmentCreate(request):
    try:
        if request.method == "GET":

            data = {
                 'auth_token': request.session['auth_token'],
                 'project_id': request.session['project_id']
                 }

            urlCloud = Url.cloudList
            clouds = ApiUtil.requestGet(urlCloud, FuncCode.environmentCreate.value, data)

            urlSystem = Url.systemList
            systems = ApiUtil.requestGet(urlSystem, FuncCode.environmentCreate.value, data)

            urlBlueprint = Url.blueprintList
            blueprints = ApiUtil.requestGet(urlBlueprint, FuncCode.environmentCreate.value, data)

            data.update({
                      'clouds': clouds['lists'],
                      'systems': systems['lists'],
                      'blueprints': blueprints['lists'],
                      })
            print(data)

            return render(request, Html.environmentCreate, {'env': data, 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = environmentForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.environmentCreate, {'env': p, 'message': msg})

            # -- Create a environment, api call
            url = Url.environmentCreate
            data = {
                'auth_token': p['auth_token'],
                'project_id': p['project_id'],
                'system_id': p['system_id'],
                'blueprint_id': p['blueprint_id'],
                'name': p['name'],
                'description': p['description'],
                'template_parameters': p['template_parameters'],
                'user_attributes': p['user_attributes'],
                'candidates_attributes': p['candidates_attributes'],
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.environmentCreate.value, data)

            return redirect(Path.environmentList)
    except Exception as ex:
        log.error(FuncCode.environmentCreate.value, None, ex)

        return render(request, Html.environmentCreate, {'env': request.POST, "message": str(ex)})


def environmentEdit(request, id):
    try:
        if request.method == "GET":

            url = Url.environmentDetail(id, Url.url)

            data = {
                 'auth_token': request.session['auth_token'],
                 'project_id': request.session['project_id']
                 }
            p = ApiUtil.requestGet(url, FuncCode.environmentEdit.value, data)
            p.update(data)

            urlCloud = Url.cloudList
            clouds = ApiUtil.requestGet(urlCloud, FuncCode.environmentEdit.value, data)

            urlSystem = Url.systemList
            systems = ApiUtil.requestGet(urlSystem, FuncCode.environmentEdit.value, data)

            urlBlueprint = Url.blueprintList
            blueprints = ApiUtil.requestGet(urlBlueprint, FuncCode.environmentEdit.value, data)

            p.update({
                      'clouds': clouds['lists'],
                      'systems': systems['lists'],
                      'blueprints': blueprints['lists'],
                      })
            print(p)

            return render(request, Html.environmentEdit, {'env': p, 'clouds': clouds['lists'], 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = environmentForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.environmentEdit, {'env': p, 'message': msg})

            # -- Create a environment, api call
            url = Url.environmentEdit(id, Url.url)
            data = {
                'auth_token': request.session['auth_token'],
                'project_id': p['project_id'],
                'system_id': p['system_id'],
                'blueprint_id': p['blueprint_id'],
                'name': p['name'],
                'description': p['description'],
                'template_parameters': p['template_parameters'],
                'user_attributes': p['user_attributes'],
                'candidates_attributes': p['candidates_attributes'],
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, FuncCode.environmentEdit.value, data)

            return redirect(Path.environmentList)
    except Exception as ex:
        log.error(FuncCode.environmentEdit.value, None, ex)

        return render(request, Html.environmentEdit, {'env': request.POST, "message": str(ex)})


def environmentDelete(request, id):
    try:
        # -- URL and data set
        url = Url.environmentDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.environmentDelete.value, data)

        return redirect(Path.environmentList)
    except Exception as ex:
        log.error(FuncCode.environmentDelete.value, None, ex)

        return render(request, Html.environmentDetail, {'env': '', 'message': ex})

