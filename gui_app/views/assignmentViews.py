# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,render_to_response
import json
import requests
from django.shortcuts import redirect
from ..forms import projectForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import FileUtil
from ..utils import SessionUtil
from ..utils import PermissionUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..utils import SessionUtil
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..logs import log
from django.contrib.auth.decorators import login_required

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


def assignmentAdd(request, id=None):
    try:
        token = request.session['auth_token']
        if request.method == "GET":


            url = Url.accountList
            data = {
                    'auth_token': token,
                    }
            accounts = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)
            data = {
                    'auth_token': token,
                    'project_id': id,
                    }
            accountsByProject = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)

            for account in accountsByProject:
                accounts.remove(account)


            return render(request, Html.assignmentAdd, {'accounts': accounts,'project_id':id, 'message': '', 'save': True})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            #form = assignmentAddForm(p)
            #if not form.is_valid():
            #    msg = ValiUtil.valiCheck(form)
            #    return render(request, Html.projectCreate, {'project': p, 'message': msg, 'save': True})

            # -- Create a project, api call
            url = Url.assignmentAdd
            for param in p:
                if 'chk-' in param:
                    data = {
                        'auth_token': token,
                        'project_id': id,
                        'account_id': param.split('-')[1],
                    }
                    permission = ApiUtil.requestPost(url, FuncCode.projectDetail.value, data)

            return redirect(Path.assignmentEdit(id))
    except Exception as ex:
        log.error(FuncCode.projectCreate.value, None, ex)

        return render(request, Html.assignmentAdd, {'accounts': None,'project_id':id, "message": str(ex), 'save': True})


def assignmentEdit(request, id=None):

    if SessionUtil.check_login(request) ==False:
        return redirect('/ccgui/logout')

    try:
        test =  FileUtil.getUrlPath()
        code = FuncCode.projectEdit.value
        token = request.session['auth_token']
        account_id = request.session['account_id']
        if request.method == "GET":

            url = Url.assignmentList
            data = {
                    'auth_token': token,
                    'project_id': id,
                    }
            assignments = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)

            assignmentList = []
            for assignment in assignments:
                url = Url.roleList
                data = {
                        'auth_token': token,
                        'account_id': assignment["account_id"],
                        'project_id': id
                        }
                roleList = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)
                role = ""
                for item in roleList:
                    role = item["id"]

                url = Url.accountList
                data = {
                        'auth_token': token,
                        }
                accountList = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)
                accountName = ""
                for item in accountList:
                    if item["id"] == assignment["account_id"]:
                        accountName = item["name"]
                        break

                assignmentList.append({
                                    'id':assignment["id"],
                                    'account_id':assignment["account_id"],
                                    'name':accountName,
                                    'role':role,
                                    })



            url = Url.roleList
            data = {
                    'auth_token': token,
                    'project_id': id
                    }
            roleList = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)

            return render(request, Html.assignmentEdit, {'assignments': assignmentList, 'message': '',
                                                        'roleList':roleList,
                                                        'project_id':id,
                                                        'account_id':account_id,
                                                         'save': True})
        else:
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check

            url = Url.assignmentEdit
            data = {
                    'auth_token': token,
                    'project_id': id,
                    }
            assignments = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)

            for assignment in assignments:
                if 'chk-' + str(assignment['id']) in p:
                    if p['sel-' + str(assignment['id'])] != p['sel_old-' + str(assignment['id'])]:

                        if p['sel_old-' + str(assignment['id'])] == '':
                            url = Url.assignmentRoleAdd(str(assignment['id']),Url.url)
                            data = {
                                'auth_token': token,
                                'role_id': p['sel-' + str(assignment['id'])],
                                }
                            ApiUtil.requestPost(url, FuncCode.projectDetail.value,data)

                        else:

                            url = Url.assignmentRoleList(str(assignment['id']),Url.url)
                            data = {
                                'auth_token': token,
                                }
                            assignmentRoleList = ApiUtil.requestGet(url, FuncCode.projectDetail.value,data)

                            for assignmentRole in assignmentRoleList:
                                if p['sel_old-' + str(assignment['id'])] == str(assignmentRole["role_id"]):
                                    url = Url.assignmentRoleDelete(str(assignment['id']),assignmentRole["id"],Url.url)
                                    data = {'auth_token': token}
                                    ApiUtil.requestDelete(url, FuncCode.projectDetail.value,{'auth_token': token})
                                    break

                            if p['sel-' + str(assignment['id'])] !='':
                                url = Url.assignmentRoleAdd(str(assignment['id']),Url.url)
                                data = {
                                    'auth_token': token,
                                    'role_id': p['sel-' + str(assignment['id'])],
                                    }
                                ApiUtil.requestPost(url, FuncCode.projectDetail.value,data)


                else:
                    url = Url.assignmentDelete(assignment["id"], Url.url)
                    data = {
                        'auth_token': token,
                    }
                    ApiUtil.requestDelete(url, code, data)

            return redirect(Path.projectDetail(id))
    except Exception as ex:
        log.error(FuncCode.projectEdit.value, None, ex)

        return render(request, Html.assignmentEdit, {'project': request.POST,
                                                     'project_id':id,
                                                     'message': str(ex), 'save': True})


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

