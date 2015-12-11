# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from api.views.projectViews import project_list
from ..forms import projectForm
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
from django.core.exceptions import ValidationError

# CloudConductor add
def projectList(request):
    try:
        projects = None
        # -- Get a project list, API call
        url = Url.projectList
        data = {'auth_token': request.session['auth_token']}
        p = ApiUtil.requestGet(url, FuncCode.projectList.value, data)
        projects = p['projects']

        return render(request, Html.projectList, {'projects': projects,
                                                  'message': ''})
    except Exception as ex:
        log.error(FuncCode.projectList.value, None, ex)

        return render(request, Html.projectList, {"projects": '', 'message': str(ex)})


def projectCreate(request):
    try:
        if request.method == "GET":
            p = {'auth_token': request.session['auth_token']}

            return render(request, Html.projectCreate, {'project': p, 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = projectForm(p)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.projectCreate, {'project': p, 'message': msg})

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

        return render(request, Html.projectCreate, {'project': request.POST, "message": str(ex)})


def projectEdit(request, id=None):
    try:
        if request.method == "GET":
            token = request.session['auth_token']
            url = Url.projectDetail(id, Url.url)
            data = {
                    'auth_token': token
                    }
            p = ApiUtil.requestGet(url, FuncCode.projectEdit.value, data)
            p.update(data)

            return render(request, Html.projectEdit, {'project': p, 'message': ''})
        else:
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check
            form = projectForm(request.POST)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                return render(request, Html.projectEdit, {'project': p, 'message': msg})

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

        return render(request, Html.projectEdit, {'project': request.POST, 'message': ex})


def projectDetail(request, id):
    try:
        # -- project DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.projectDetail(id, Url.url)
        data = {
                'auth_token': token
                }
        p = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)

        # -- AccountAPI call, get a response
        url2 = Url.assignmentList
        data = {
                'auth_token': token,
                'project_id': requestsession['project_id'],
#                 'account_id': requestsession['accout_id']
                }
        a = ApiUtil.requestGet(url2, FuncCode.projectDetail.value,data)

        return render(request, Html.projectDetail, {'project': p, 'accounts': a['lists'], 'message': ''})
    except Exception as ex:
        log.error(FuncCode.projectDetail.value, None, ex)

        return render(request, Html.projectDetail, {'project': '', 'accounts': '', 'message': str(ex)})


def projectDelete(request, id):
    try:
        # -- URL and data set
        url = Url.projectDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.projectDelete.value, data)

        return redirect(Path.projectList)
    except Exception as ex:
        log.error(FuncCode.projectDelete.value, None, ex)

        return render(request, Html.projectDetail, {'project': '', 'accounts': '', 'message': ex})


def projectAddUser(request, id):

    return render(request, Html.addUser)
