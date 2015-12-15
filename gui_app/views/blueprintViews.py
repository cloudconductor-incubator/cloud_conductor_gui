# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from ..forms import blueprintForm
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


def blueprintList(request):
    try:
        blueprints = None
        # -- Get a blueprint list, API call
        url = Url.blueprintList
        print(url)

        data = {'auth_token': request.session['auth_token']}
        p = ApiUtil.requestGet(url, FuncCode.blueprintList.value, data)
        blueprints = p['lists']

        return render(request, Html.blueprintList, {'blueprints': blueprints, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.blueprintList.value, None, ex)

        return render(request, Html.blueprintList, {"blueprints": '', 'message': str(ex)})


def blueprintDetail(request, id):
    try:
        # -- blueprint DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.blueprintDetail(id, Url.url)
        data = {
                'auth_token': token
                }
        p = ApiUtil.requestGet(url, FuncCode.blueprintDetail.value, data)

        return render(request, Html.blueprintDetail, {'blueprint': p, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.blueprintDetail.value, None, ex)

        return render(request, Html.blueprintDetail, {'blueprint': '', 'message': str(ex)})


def blueprintCreate(request):
    try:
        if request.method == "GET":

            data = {
                 'auth_token': request.session['auth_token'],
                 'project_id': request.session['project_id']
                 }

            url = Url.patternList
            patterns = ApiUtil.requestGet(url, FuncCode.blueprintCreate.value, data)

            return render(request, Html.blueprintCreate, {'blueprint': data, 'patterns': patterns['lists'], 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = blueprintForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.blueprintCreate, {'blueprint': p, 'message': msg})

            # -- Create a blueprint, api call
            url = Url.blueprintCreate
            data = {
                'auth_token': p['auth_token'],
                'project_id': p['project_id'],
                'name': p['name'],
                'description': p['description'],
                'patterns_attributes': p['patterns_attributes'],
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.blueprintCreate.value, data)

            return redirect(Path.blueprintList)
    except Exception as ex:
        log.error(FuncCode.blueprintCreate.value, None, ex)

        return render(request, Html.blueprintCreate, {'blueprint': request.POST, "message": str(ex)})


def blueprintEdit(request, id):
    try:
        if request.method == "GET":

            url = Url.blueprintDetail(id, Url.url)

            data = {
                 'auth_token': request.session['auth_token'],
                 'project_id': request.session['project_id']
                 }
            p = ApiUtil.requestGet(url, FuncCode.blueprintEdit.value, data)
            p.update(data)

            return render(request, Html.blueprintEdit, {'blueprint': p,'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = blueprintForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.blueprintEdit, {'blueprint': p, 'message': msg})

            # -- Create a blueprint, api call
            url = Url.blueprintEdit(id, Url.url)
            data = {
                'auth_token': p['auth_token'],
                'project_id': p['project_id'],
                'name': p['name'],
                'description': p['description'],
                'patterns_attributes': p['patterns_attributes'],
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, FuncCode.blueprintEdit.value, data)

            return redirect(Path.blueprintList)
    except Exception as ex:
        log.error(FuncCode.blueprintEdit.value, None, ex)

        return render(request, Html.blueprintEdit, {'blueprint': request.POST, "message": str(ex)})


def blueprintDelete(request, id):
    try:
        # -- URL and data set
        url = Url.blueprintDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.blueprintDelete.value, data)

        return redirect(Path.blueprintList)
    except Exception as ex:
        log.error(FuncCode.blueprintDelete.value, None, ex)

        return render(request, Html.blueprintDetail, {'blueprint': '', 'message': ex})

