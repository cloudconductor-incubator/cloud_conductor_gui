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
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..logs import log
from logging import getLogger
logger = getLogger('app')


# Create your views here.
def cloudList(request):
    try:
        # -- Get a cloud list, API call
        url = Url.cloudList
        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }
        clouds = ApiUtil.requestGet(url, FuncCode.cloudList.value, data)
#         clouds = clouds['lists']

        return render(request, Html.cloudList, {'cloud': clouds, 'message': ''})
    except Exception as ex:

        log.error(FuncCode.cloudList.value, None, ex)
        return render(request, Html.cloudList, {'cloud': '', 'message': ex})


def cloudDetail(request, id):
    try:
        # -- Get a cloud list, API call
        url = Url.cloudDetail(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        cloud = ApiUtil.requestGet(url, FuncCode.cloudDetail.value, data)

        # -- Get a baseImage list, API call
        url2 = Url.baseImageList
        data = {'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id'],
                'cloud_id': id,
                }
        baseImages = ApiUtil.requestGet(url2, FuncCode.baseImageList.value, data)
#         baseImages = baseImages['lists']

        return render(request, Html.cloudDetail, {'cloud': cloud, 'baseImage': baseImages, 'message': ''})
    except Exception as ex:

        log.error(FuncCode.cloudList.value, None, ex)
        return render(request, Html.cloudDetail, {'cloud': '', 'baseImage': '', 'message': ex})


def cloudCreate(request):
    try:

        cloudType = list(CloudType)

        if request.method == "GET":

            p = {
                'auth_token': request.session['auth_token'],
                'project_id': request.session['project_id'],
                'cloudType': cloudType
            }

            return render(request, Html.cloudCreate, {'cloud': p, 'message':'', 'cloudType': list(CloudType), 'save': True})

        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            cpPost = p.copy()

            print(p)
            # -- Validate check
            form = cloudForm(p)
            if not form.is_valid():
                cpPost.update({'cloudType': cloudType})
                return render(request, Html.cloudCreate, {'cloud': cpPost, 'message': form.errors, 'cloudType': list(CloudType), 'save': True})

            # -- Create a cloud, api call
            url = Url.cloudCreate
            data = {
                'auth_token': p['auth_token'],
                'project_id': p['project_id'],
                'name': p['name'],
                'type': p['type'],
                'key': p['key'],
                'secret': p['secret'],
                'entry_point': p['entry_point'],
                'tenant_name': p['tenant_name'],
                'description': p['description']
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.projectCreate.value, data)

            return redirect(Path.cloudList)

    except Exception as ex:
        log.error(FuncCode.cloudList.value, None, ex)

        return render(request, Html.cloudCreate, {'cloud': request.POST, 'message': ex, 'cloudType': list(CloudType), 'save': True})


def cloudEdit(request, id):
    cloudType = list(CloudType)
    code = FuncCode.cloudEdit.value
    try:
        if request.method == "GET":
            token = request.session['auth_token']
            url = Url.cloudDetail(id, Url.url)
            data = {
                'auth_token': token,
                'project_id': request.session['project_id'],
                'cloudType': cloudType,
            }
            cloud = ApiUtil.requestGet(url, code, data)
            cloud.update(data)

            return render(request, "gui_app/cloud/cloudEdit.html", {'cloud': cloud, 'message': '', 'cloudType': list(CloudType), 'save': True})
        elif request.method == "POST":
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check
            form = cloudForm(request.POST)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                cpPost.update({'cloudType': cloudType})
                return render(request, Html.cloudEdit, {'cloud': cpPost, 'message': form.errors, 'cloudType': list(CloudType), 'save': True})

            # -- URL set
            url = Url.cloudEdit(id, Url.url)
            # -- Set the value to the form
            data = {
                'auth_token': p['auth_token'],
                'project_id': p['project_id'],
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

        return render(request, Html.cloudEdit, {'cloud': request.POST, 'message': ex, 'cloudType': list(CloudType), 'save': True})


def cloudDelete(request, id):
    try:
        # -- URL and data set
        url = Url.cloudDetail(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.projectDelete.value, data)

        return redirect(Path.cloudList)
    except Exception as ex:
        log.error(FuncCode.cloudDelete.value, None, ex)

        return render(request, Html.cloudDelete, {'cloud': '', 'message': ex})
