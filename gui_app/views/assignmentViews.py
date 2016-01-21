# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from django.shortcuts import redirect
from ..forms import projectForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import PermissionUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..logs import log

# CloudConductor add
def assignmentList(request):
    try:
        projects = None
        # -- Get a project list, API call
        url = Url.projectList
        data = {'auth_token': request.session['auth_token']}
        projects = ApiUtil.requestGet(url, FuncCode.projectList.value, data)
#         projects = p['projects']

        return render(request, Html.projectList, {'projects': projects,
                                                  'message': ''})
    except Exception as ex:
        log.error(FuncCode.projectList.value, None, ex)

        return render(request, Html.projectList, {"projects": '', 'message': str(ex)})


def assignmentCreate(request):
    try:
        if request.method == "GET":
            p = {'auth_token': request.session['auth_token']}

            return render(request, Html.projectCreate, {'project': p, 'message': '', 'save': True})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = projectForm(p)
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.projectCreate, {'project': p, 'message': msg, 'save': True})

            # -- Create a project, api call
            url = Url.projectCreate
            data = {
                'auth_token': request.session['auth_token'],
                'name': p['name'],
                'description': p['description']
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.projectCreate.value, data)

            return redirect(Path.projectList)
    except Exception as ex:
        log.error(FuncCode.projectCreate.value, None, ex)

        return render(request, Html.projectCreate, {'project': request.POST, "message": str(ex), 'save': True})


def assignmentEdit(request, id=None):


    try:
        code = FuncCode.projectEdit.value
        if request.method == "GET":
            token = request.session['auth_token']
            url = Url.assignmentEdit
            data = {
                    'auth_token': token,
                    'project_id': id,
                    }
            assignments = ApiUtil.requestGet(url, code, data)

            list = RoleUtil.get_role_list(code, token, project_id=id)

            return render(request, Html.assignmentEdit, {'assignments': assignments, 'message': '',
                                                        'roleList':list,
                                                         'save': True})
        else:
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check
            form = projectForm(request.POST)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.projectEdit, {'project': p, 'message': msg, 'save': True})

            # -- URL set
            url = Url.projectEdit(id, Url.url)
            # -- Set the value to the form
            data = {
                    'auth_token': request.session['auth_token'],
                    'name': p['name'],
                    'description': p['description']
                    }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.projectEdit.value, data)

            return redirect(Path.projectList)
    except Exception as ex:
        log.error(FuncCode.projectEdit.value, None, ex)

        return render(request, Html.assignmentEdit, {'project': request.POST, 'message': str(ex), 'save': True})


def assignmentDelete(request, id):
    try:
        # -- URL and data set
        url = Url.projectDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.projectDelete.value, data)

        return redirect(Path.projectList)
    except Exception as ex:
        log.error(FuncCode.projectDelete.value, None, ex)

        return render(request, Html.projectDetail, {'project': '', 'accounts': '', 'message': str(ex)})

