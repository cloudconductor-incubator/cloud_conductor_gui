# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from ..forms import applicationForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import ApplicationUtil
from ..utils import ApplicationHistoryUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..enum.ApplicationType import ApplicaionType
from ..enum.ProtocolType import ProtocolType
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
        token = request.session['auth_token']
        project_id = request.session['project_id']
        code = FuncCode.applicationCreate.value
        data = {
            'auth_token': token,
            'project_id': project_id
        }
        url = Url.systemList
        systems = ApiUtil.requestGet(url, code, data)

        if request.method == "GET":

            data.update({
                'systems': systems,
            })

            return render(request, Html.applicationCreate, {'app': data, 'apptype': list(ApplicaionType),
                                                            'protocol': list(ProtocolType), 'message': '',
                                                            'systems': systems, 'save': True})
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
                return render(request, Html.applicationCreate, {'app': cpPost, 'apptype': list(ApplicaionType),
                                                                'protocol': list(ProtocolType), 'message': form.errors,
                                                                'save': True})

            # -- Create a application, api call
            app = ApplicationUtil.create_application(
                code, token, p['system_id'], p['name'], p['description'], p['domain'])
            ApplicationHistoryUtil.create_history(code, token, app.get('id'), p.get('url'), p.get('type'),
                                                  p.get('protocol'),  p.get('revision'), p.get('pre_deploy'),
                                                  p.get('post_deploy'), p.get('parameters'))

            return redirect(Path.applicationList)
    except Exception as ex:
        log.error(FuncCode.applicationCreate.value, None, ex)

        return render(request, Html.applicationCreate, {'app': request.POST, "message": str(ex), 'save': True})


def applicationEdit(request, id):
    try:
        code = FuncCode.systemList.value
        token = request.session['auth_token']
        project_id = request.session['project_id']
        if request.method == "GET":

            url = Url.applicationDetail(id, Url.url)

            data = {
                'auth_token': token,
                'project_id': project_id
            }
            p = ApiUtil.requestGet(url, FuncCode.applicationEdit.value, data)
            data.update(p)

            url2 = Url.systemList
            systems = ApiUtil.requestGet(url2, code, data)
            data.update({
                'systems': systems,
            })
            print(data)
            newhis = ApplicationHistoryUtil.get_new_history(code, token, id)
            history = ApplicationHistoryUtil.get_history_detail(code, token, newhis.get('id'))
            print(history)

            return render(request, Html.applicationEdit, {'app': data, 'history': history, 'message': '', 'save': True})
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
                return render(request, Html.applicationEdit, {'app': p, 'message': msg, 'save': True})

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

        return render(request, Html.applicationEdit, {'app': request.POST, "message": str(ex), 'save': True})


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
