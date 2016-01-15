# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
import ast
from collections import OrderedDict
from ..forms import environmentForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import FileUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..utils.BlueprintUtil import get_blueprint_version
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..logs import log


def environmentList(request):
    try:
        envs = None
        # -- Get a environment list, API call
#         url = Url.environmentList
#         print(url)
#
#         data = {
#             'auth_token': request.session['auth_token'],
#             'project_id': request.session['project_id']
#         }
#         envs = ApiUtil.requestGet(url, FuncCode.environmentList.value, data)

        return render(request, Html.environmentList, {'envs': envs, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.environmentList.value, None, ex)

        return render(request, Html.environmentList, {"environment": '', 'message': str(ex)})


def environmentDetail(request, id):
    try:
        # -- environment DetailAPI call, get a response
        token = request.session['auth_token']
        url = Url.environmentDetail(id, Url.url)
        data = {
            'auth_token': token
        }
        p = ApiUtil.requestGet(url, FuncCode.environmentDetail.value, data)

        return render(request, Html.environmentDetail, {'env': p, 'message': ''})
    except Exception as ex:
        log.error(FuncCode.environmentDetail.value, None, ex)

        return render(request, Html.environmentDetail, {'env': '', 'message': str(ex)})


def environmentCreate(request):
    try:
        code = FuncCode.environmentCreate.value
        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }

        fileForm = UploadFileForm()
        clouds = ApiUtil.requestGet(Url.cloudList, code, data)
#         clouds = clouds['lists']
        systems = ApiUtil.requestGet(Url.systemList, code, data)
#         systems = systems['lists']
        blueprints = get_blueprint_version(code, data)

        if request.method == "GET":

            data.update({
                'clouds': clouds,
                'systems': systems,
                'blueprints': blueprints,
                'fileForm': fileForm,
            })

            return render(request, Html.environmentCreate, {'env': data, 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            cpPost = p.copy()
            form = environment_form(cpPost)
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                cpPost.update({
                    'clouds': clouds,
                    'systems': systems,
                    'blueprints': blueprints,
                })
                print(cpPost)

                return render(request, Html.environmentCreate, {'env': cpPost, 'message': form.errors})

            # -- Create a environment, api call
            url = Url.environmentCreate
            # -- API call, get a response
            ApiUtil.requestPost(
                url, FuncCode.environmentCreate.value, addEnvironmentParam(cpPost))

            print(1)
            #-- file download
            file = FileUtil.download(request)
#             file = FileUtil.download_file(request)
            print(file)

            return redirect(Path.environmentList)
    except Exception as ex:
        log.error(FuncCode.environmentCreate.value, None, ex)

        return render(request, Html.environmentCreate, {'env': request.POST, "message": str(ex)})


def environment_form(param):

    blueprint = param.get('blueprint', None)
    if blueprint != None and blueprint != '':
        blueprint = ast.literal_eval(blueprint)

        param['blueprint_id'] = blueprint.get('id')
        param['version'] = blueprint.get('version')

    form = environmentForm(param)

    return form


def environmentEdit(request, id):
    try:
        code = FuncCode.environmentEdit.value
        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }

        url = Url.environmentDetail(id, Url.url)
        p = ApiUtil.requestGet(url, code, data)
        p.update(data)

        clouds = ApiUtil.requestGet(Url.cloudList, code, data)
#         clouds = clouds['lists']
        systems = ApiUtil.requestGet(Url.systemList, code, data)
#         systems = systems['lists']
        blueprints = get_blueprint_version(code, data)

        if request.method == "GET":
            p.update({
                'clouds': clouds,
                'systems': systems,
                'blueprints': blueprints,
            })

            return render(request, Html.environmentEdit, {'env': p, 'message': ''})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            cpPost = p.copy()
            # -- Validate check
            form = environment_form(cpPost)
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)
                cpPost.update({
                    'clouds': clouds,
                    'systems': systems,
                    'blueprints': blueprints,
                })

                return render(request, Html.environmentEdit, {'env': cpPost, 'message': form.errors})

            # -- Create a environment, api call
            url = Url.environmentEdit(id, Url.url)
            data = addEnvironmentParam(p)
            # -- API call, get a response
            ApiUtil.requestPut(url, code, data)

            return redirect(Path.environmentList)
    except Exception as ex:
        log.error(code, None, ex)

        return render(request, Html.environmentEdit, {'env': request.POST, "message": str(ex)})


def environmentDelete(request, id):
    try:
        # -- URL and data set
        url = Url.environmentDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.environmentDelete.value, data)

        return redirect(Path.environmentList)
    except Exception as ex:
        log.error(FuncCode.environmentDelete.value, None, ex)

        return render(request, Html.environmentDetail, {'env': '', 'message': ex})


def addEnvironmentParam(param):

    # candidates_attributes
    candidates_attributes = [
        {"cloud_id": param.get('candidates_attributes_1'), "priority": 1},
        {"cloud_id": param.get('candidates_attributes_2'), "priority": 2},
        {"cloud_id": param.get('candidates_attributes_3'), "priority": 3}
    ]

    data = {
        'auth_token': param.get('auth_token'),
        'project_id': param.get('project_id'),
        'system_id': param.get('system_id'),
        'blueprint_id': param.get('blueprint_id'),
        'version': param.get('version'),
        'name': param.get('name'),
        'description': param.get('description'),
        'template_parameters': param.get('template_parameters'),
        'user_attributes': param.get('user_attributes'),
        'candidates_attributes': candidates_attributes,

    }

    return data


def fileUpload(request):
    form = UploadFileForm(request.POST, request.FILES)
    prit("ppppppppppppppppppppp")
    if form.is_valid():
        updir = r'c:\\website\\django\\mysite\\upload\\' + \
            form.cleaned_data['title']
        destination = open(updir, 'wb+')
        upfile = request.FILES['file']
        for chunk in upfile.chunks():
            destination.write(chunk)
        destination.close()
        msg = 'Uploaded.'

        t = loader.get_template('fileuptest/index.html')
        c = Context()
        c['form'] = form
        c['msg'] = msg
        return HttpResponse(t.render(c))
