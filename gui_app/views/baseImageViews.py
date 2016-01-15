# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from ..forms import baseImageForm
from ..enum import ResponseType
from ..enum.OSVersion import OSVersion
from ..enum.FunctionCode import FuncCode
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..logs import log


# Create your views here.
def baseImageDetail(request, id):
    try:
        # -- baseImage DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.baseImageDetail(id, Url.url)
        data = {'auth_token': token}
        baseImage = ApiUtil.requestGet(
            url, FuncCode.baseImageDetail.value, data)

        return render(request, Html.baseImageDetail, {'baseImage': baseImage, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.baseImageDetail.value, None, ex)

        return render(request, Html.baseImageDetail, {'baseImage': '', 'message': str(ex)})


def baseImageCreate(request, cid):
    try:
        oSVersion = list(OSVersion)

        if request.method == "GET":
            p = {
                'auth_token': request.session['auth_token'],
                'cloud_id': cid,
            }

            return render(request, Html.baseImageCreate, {'baseImage': p, 'osversion': list(OSVersion), 'message': '', 'save': True})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            form = baseImageForm(p)
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                cpPost = p.copy()

                return render(request, Html.baseImageCreate, {'baseImage': cpPost, 'osversion': list(OSVersion), 'message': form.errors, 'save': True})

            # -- Create a project, api call
            url = Url.baseImageCreate
            data = {
                'auth_token': p.get('auth_token'),
                'cloud_id': p.get('cloud_id'),
                'ssh_username': p.get('ssh_username'),
                'source_image': p.get('source_image'),
                'os_version': p.get('os_version'),
            }
            # -- API call, get a response
            ApiUtil.requestPost(url, FuncCode.baseImageCreate.value, data)

            return redirect(Path.cloudDetail(cid))
    except Exception as ex:
        log.error(FuncCode.baseImageCreate.value, None, ex)

        return render(request, Html.baseImageCreate, {'baseImage': request.POST, 'osversion': list(OSVersion), "message": str(ex), 'save': True})


def baseImageEdit(request, id):
    try:
        if request.method == "GET":
            token = request.session['auth_token']
            url = Url.baseImageDetail(id, Url.url)
            data = {
                'auth_token': token,
            }
            p = ApiUtil.requestGet(url, FuncCode.baseImageEdit.value, data)
            p.update(data)

            return render(request, Html.baseImageEdit, {'baseImage': p, 'osversion': list(OSVersion), 'message': '', 'save': True})
        else:
            # -- Get a value from a form
            p = request.POST
            msg = ''
            # -- Validate check
            form = baseImageForm(request.POST)
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                cpPost = p.copy()

                return render(request, Html.baseImageEdit, {'baseImage': p, 'osversion': list(OSVersion), 'message': form.errors, 'save': True})

            # -- URL set
            url = Url.baseImageEdit(id, Url.url)
            # -- Set the value to the form
            data = {
                'auth_token': request.session['auth_token'],
                'cloud_id': p['cloud_id'],
                'source_image': p['source_image'],
                'ssh_username': p['ssh_username'],
                'os_version': p['os_version']
            }
            # -- API call, get a response
            ApiUtil.requestPut(url, FuncCode.baseImageEdit.value, data)

            return redirect(Path.cloudDetail(p['cloud_id']))
    except Exception as ex:
        log.error(FuncCode.baseImageEdit.value, None, ex)

        return render(request, Html.baseImageEdit, {'baseImage': request.POST, 'osversion': list(OSVersion), 'message': ex, 'save': True})


def baseImageDelete(request, id):
    try:
        data = {'auth_token': request.session['auth_token']}
        # -- Get a baseImage
        urlb = Url.baseImageDetail(id, Url.url)
        detail = ApiUtil.requestGet(urlb, FuncCode.baseImageDetail.value, data)

        # -- Delete a baseImage, api call
        url = Url.baseImageDelete(id, Url.url)
        ApiUtil.requestDelete(url, FuncCode.baseImageDelete.value, data)

        return redirect(Path.cloudDetail('1'))
    except Exception as ex:
        log.error(FuncCode.baseImageDelete.value, None, ex)

        return render(request, Html.baseImageDetail, {'baseImage': '', 'message': ex})
