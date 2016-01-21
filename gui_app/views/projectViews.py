# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from django.shortcuts import redirect
from ..forms import projectForm
from ..utils import RoleUtil
from ..utils import ProjectUtil
from ..utils import SessionUtil
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


def projectList(request):
    try:
        projects = None
        # -- Get a project list, API call
        code = FuncCode.projectList.value
        token = request.session['auth_token']
        projects = ProjectUtil.get_project_list(code, token)

        return render(request, Html.projectList, {'projects': projects, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.projectList.value, None, ex)

        return render(request, Html.projectList, {"projects": '', 'message': str(ex)})


def projectCreate(request):
    try:
        code = FuncCode.projectCreate.value
        token = request.session['auth_token']
        s = request.session

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
                'auth_token': token,
                'name': p['name'],
                'description': p['description']
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, code, data)

            SessionUtil.edit_project_session(code, token, request.session)

            return redirect(Path.projectList)
    except Exception as ex:
        log.error(FuncCode.projectCreate.value, None, ex)

        return render(request, Html.projectCreate, {'project': request.POST, "message": str(ex), 'save': True})


def projectEdit(request, id):
    try:
        code = FuncCode.projectEdit.value
        token = request.session['auth_token']

        if request.method == "GET":

            p = ProjectUtil.get_project_detail(code, token, id)

            return render(request, Html.projectEdit, {'project': p, 'message': '', 'save': True})
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

            # -- API call, get a response
            project = ProjectUtil.edit_project(code, token, id, p.get('name'), p.get('description'))
            SessionUtil.edit_project_session(code, token, request.session, id, project.get('name'))

            return redirect(Path.projectList)
    except Exception as ex:
        log.error(FuncCode.projectEdit.value, None, ex)

        return render(request, Html.projectEdit, {'project': request.POST, 'message': str(ex), 'save': True})


def projectDetail(request, id):
    try:
        code = FuncCode.projectDetail.value
        token = request.session['auth_token']

        # -- project DetailAPI call, get a response
        p = ProjectUtil.get_project_detail(code, token, id)

        # -- AccountAPI call, get a response
        url2 = Url.accountList
        data = {
                'auth_token': token,
                'project_id': id,
                }
        accounts = ApiUtil.requestGet(url2, FuncCode.projectDetail.value,data)

        accountList = []
        for account in accounts:
            url2 = Url.roleList
            data = {
                    'auth_token': token,
                    'project_id': id,
                    'account_id': account["id"]
                    }
            assignments = ApiUtil.requestGet(url2, FuncCode.projectDetail.value,data)
            role = ""
            for assignment in assignments:
                role = assignment["name"]

            accountList.append({'id':account["id"],
                                'name':account["name"],
                                'role':role,
                                'admin':account["admin"],
                                'email':account["email"],
                                })



        return render(request, Html.projectDetail, {'project': p, 'accounts': accountList, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.projectDetail.value, None, ex)

        return render(request, Html.projectDetail, {'project': '', 'accounts': '', 'message': str(ex)})


def projectDelete(request, id):
    try:
        # -- URL and data set
        code = FuncCode.projectDelete.value
        url = Url.projectDelete(id, Url.url)
        session = request.session
        token = session['auth_token']
        data = {'auth_token': token}
        ApiUtil.requestDelete(url, code, data)
        SessionUtil.edit_project_session(code, token, session, id)

        return redirect(Path.projectList)
    except Exception as ex:
        log.error(FuncCode.projectDelete.value, None, ex)

        return render(request, Html.projectDetail, {'project': '', 'accounts': '', 'message': str(ex)})


def projectChange(request, id):
    try:
        session = request.session
        code = FuncCode.projectChange.value
        token = session['auth_token']
        account_id = session['account_id']

        #-- ProjectAPI call, get a response
        url = Url.projectDetail(id, Url.url)
        data = {
                'auth_token': token
                }
        project = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)

        #-- RoleListAPI call, get a response
        role = RoleUtil.get_account_role(code, token, id, account_id)

        if not role:
            raise(Error.Authentication.value)
        #-- PermissionListAPI call, get a response
        permissions = PermissionUtil.get_permission_list(code, token, role.get('id'))

        if not permissions:
            raise(Error.Authentication.value)


        session['project_id'] = id
        session['project_name'] = project['name']

        RoleUtil.add_session_role(session, role, permissions)

        return redirect(Path.top)
    except Exception as ex:
        log.error(FuncCode.projectDelete.value, None, ex)

        request.session.clear()

        return render(request, Html.login, {'message': str(ex)})


def projectAddUser(request, id):

    return render(request, Html.addUser)
