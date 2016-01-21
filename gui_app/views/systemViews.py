# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from ..forms import systemForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import SystemUtil
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

        data = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id']
                }
        systems = ApiUtil.requestGet(url, FuncCode.systemList.value, data)
#         systems = systems['lists']

        return render(request, Html.systemList, {'system': systems, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.systemList.value, None, ex)

        return render(request, Html.systemList, {"system": '', 'message': str(ex)})

    return render(request, Html.systemList, {'system': '', 'baseImage':'', 'message':ex})


def systemDetail(request, id):
    try:
        # -- system DetailAPI call, get a response
        token = request.session.get('auth_token')
        code = FuncCode.systemDetail.value
        system = SystemUtil.get_system_detail(code, token, id)

        return render(request, Html.systemDetail, {'system': system, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.systemDetail.value, None, ex)

        return render(request, Html.systemDetail, {'system': '', 'message': str(ex)})


def systemCreate(request):
    try:
        if request.method == "GET":

            return render(request, Html.systemCreate, {'system': '', 'message': '', 'save': True})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = systemForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)

                return render(request, Html.systemCreate, {'system': p, 'message': msg, 'save': True})

            code = FuncCode.systemCreate.value

            SystemUtil.create_system(code, request.session.get('auth_token'), request.session.get('project_id')
                                     , p.get('name'), p.get('description'), p.get('domain'))

            return redirect(Path.systemList)
    except Exception as ex:
        p = request.POST
        log.error(FuncCode.systemCreate.value, None, ex)

        return render(request, Html.systemCreate, {'system': p, "message": str(ex), 'save': True})


def systemEdit(request, id):
    try:
        code = FuncCode.systemEdit.value
        token = request.session.get('auth_token')
        if request.method == "GET":
            system = SystemUtil.get_system_detail(code, token, id)

            return render(request, Html.systemEdit, {'system': system, 'message': '', 'save': True})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = systemForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.systemEdit, {'system': p, 'message': msg, 'save': True})

            # -- Edit a system, api call
            SystemUtil.edit_system(code, token, id, p.get('name'), p.get('description'), p.get('domain'))

            return redirect(Path.systemList)
    except Exception as ex:
        log.error(FuncCode.systemEdit.value, None, ex)

        return render(request, Html.systemEdit, {'system': request.POST, "message": str(ex), 'save': True})


def systemDelete(request, id):
    try:
        # -- URL and data set
        code = FuncCode.systemDelete.value
        SystemUtil.get_system_delete(code, request.session.get('auth_token'), id)

        return redirect(Path.systemList)
    except Exception as ex:
        log.error(FuncCode.systemDelete.value, None, ex)

        return render(request, Html.systemDetail, {'system': '', 'message': ex})

