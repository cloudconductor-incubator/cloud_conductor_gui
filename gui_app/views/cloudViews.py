# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from ..forms import cloudForm
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.CloudType import CloudType
from ..enum.FunctionCode import FuncCode
from ..utils import ApiUtil
from ..utils import ValiUtil
from ..utils import CloudUtil
from ..utils import BaseimageUtil
from ..utils import SessionUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..logs import log
from logging import getLogger
logger = getLogger('app')
clouds = None


# Create your views here.
def cloudList(request):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'cloud','list') == False:
            return render_to_response(Html.error_403)

        code = FuncCode.cloudList.value
        token = request.session['auth_token']
        # -- Get a cloud list, API call
        clouds = CloudUtil.get_cloud_list(code, token)
        print(request.session.get('cloud'))
        print(request.session.get('cloud').get('manage'))

        return render(request, Html.cloudList, {'cloud': clouds, 'message': ''})
    except Exception as ex:

        log.error(FuncCode.cloudList.value, None, ex)
        return render(request, Html.cloudList, {'cloud': '', 'message': ex})


def cloudDetail(request, id):
    cloud = None
    baseimages = None
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'cloud','read') == False:
            return render_to_response(Html.error_403)

        code = FuncCode.cloudDetail.value
        token = request.session['auth_token']
        # -- Get a cloud list, API call
        cloud = CloudUtil.get_cloud_detail(code, token, id)

        # -- Get a baseImage list, API call
        baseimages = BaseimageUtil.get_baseimege_list(code, token)
        return render(request, Html.cloudDetail, {'cloud': cloud, 'baseImage': baseimages, 'message': ''})
    except Exception as ex:

        log.error(FuncCode.cloudList.value, None, ex)
        return render(request, Html.cloudDetail, {'cloud': '', 'baseImage': '', 'message': ex})


def cloudCreate(request):
    cloudType = None
    code = FuncCode.cloudList.value
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'cloud','create') == False:
            return render_to_response(Html.error_403)

        token = request.session['auth_token']
        project_id = request.session['project_id']
        cloudType = list(CloudType)

        if request.method == "GET":

            return render(request, Html.cloudCreate, {'cloud': '', 'form': '', 'message':'',
                                                      'cloudType': cloudType, 'save': True})

        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = cloudForm(p)
            if not form.is_valid():

                return render(request, Html.cloudCreate, {'cloud': p, 'form': form, 'message': '',
                                                          'cloudType': cloudType, 'save': True})


            cloud = CloudUtil.create_cloud2(code, token, project_id, form.data.copy())

            # -- Create a cloud, api call
#             url = Url.cloudCreate
#             data = {
#                 'auth_token': token,
#                 'project_id': project_id,
#                 'name': p['name'],
#                 'type': p['type'],
#                 'key': p['key'],
#                 'secret': p['secret'],
#                 'entry_point': p['entry_point'],
#                 'tenant_name': p['tenant_name'],
#                 'description': p['description']
#             }
#             # -- API call, get a response
#             ApiUtil.requestPost(url, FuncCode.projectCreate.value, data)


            return redirect(Path.cloudList)

    except Exception as ex:
        log.error(FuncCode.cloudList.value, None, ex)

        return render(request, Html.cloudCreate, {'cloud': request.POST, 'form': '', 'message': ex,
                                                  'cloudType': cloudType, 'save': True})


def cloudEdit(request, id):
    cloudType = list(CloudType)
    code = FuncCode.cloudEdit.value
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'cloud','update') == False:
            return render_to_response(Html.error_403)

        token = request.session['auth_token']
        project_id = request.session['project_id']

        if request.method == "GET":

            url = Url.cloudDetail(id, Url.url)
            data = {
                'auth_token': token,
                'project_id': project_id,
                'cloudType': cloudType,
            }
            cloud = ApiUtil.requestGet(url, code, data)
            cloud.update(data)

            return render(request, "gui_app/cloud/cloudEdit.html", {'cloud': cloud, 'form': '', 'message': '',
                                                                    'cloudType': cloudType, 'save': True})
        elif request.method == "POST":
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check
            form = cloudForm(request.POST)
            form.full_clean()
            if not form.is_valid():

                return render(request, Html.cloudEdit, {'cloud': p, 'form': form, 'message': '',
                                                        'cloudType': cloudType, 'save': True})

            # -- URL set
            url = Url.cloudEdit(id, Url.url)
            # -- Set the value to the form
            data = {
                'auth_token': token,
                'project_id': project_id,
                'name': p['name'],
                'type': p['type'],
                'key': p['key'],
                'secret': p['secret'],
                'entry_point': p['entry_point'],
                'tenant_name': p['tenant_name'],
                'description': p['description']
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, code, data)

            return redirect(Path.cloudList)
        else:
            url = None
            return redirect(Path.list)
    except Exception as ex:
        log.error(code, None, ex)

        return render(request, Html.cloudEdit, {'cloud': request.POST, 'form': '', 'message': ex,
                                                'cloudType': cloudType, 'save': True})


def cloudDelete(request, id):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'cloud','destroy') == False:
            return render_to_response(Html.error_403)

        # -- URL and data set
        url = Url.cloudDetail(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.projectDelete.value, data)

        return redirect(Path.cloudList)
    except Exception as ex:
        log.error(FuncCode.cloudDelete.value, None, ex)

        return render(request, Html.cloudDelete, {'cloud': '', 'message': ex})
