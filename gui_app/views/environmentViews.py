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
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..utils.BlueprintUtil import get_blueprint_version
from ..enum.FunctionCode import FuncCode
from ..logs import log


def environmentList(request):
    try:
        envs = None
        # -- Get a environment list, API call
        url = Url.environmentList
        print(url)

        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }
        envs = ApiUtil.requestGet(url, FuncCode.environmentList.value, data)

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
        p = request.POST
        code = FuncCode.environmentCreate.value
        data = {
            'auth_token': request.session['auth_token'],
            'project_id': request.session['project_id']
        }

        clouds = ApiUtil.requestGet(Url.cloudList, code, data)
        systems = ApiUtil.requestGet(Url.systemList, code, data)
        blueprints = get_blueprint_version(code, data)

        if request.method == "GET":

            return render(request, Html.environmentCreate, {'env': data, 'clouds': clouds, 'systems': systems,
                                                            'blueprints': blueprints, 'message': '', 'save': True})
        else:
            # -- Get a value from a form
            msg = ''
            p = request.POST
            # -- Validate check
            cpPost = p.copy()
            param = putBlueprint(cpPost)
#             form = environment_form(cpPost)

            form = environmentForm(param)
            form.full_clean()
            if not form.is_valid():
                msg = ValiUtil.valiCheck(form)

                return render(request, Html.environmentCreate, {'env': cpPost, 'clouds': clouds, 'systems': systems,
                                                                'blueprints': blueprints, 'message': form.errors, 'save': True})

            # -- Create a environment, api call
            url = Url.environmentCreate
            # -- API call, get a response
            a = ApiUtil.requestPost(
                url, FuncCode.environmentCreate.value, addEnvironmentParam(cpPost))

            return redirect(Path.environmentList)
    except Exception as ex:
        log.error(FuncCode.environmentCreate.value, None, ex)

        return render(request, Html.environmentCreate, {'env': request.POST, 'clouds': '', 'systems': '',
                                                        'blueprints': '', 'message': str(ex), 'save': True})


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
        systems = ApiUtil.requestGet(Url.systemList, code, data)
        blueprints = get_blueprint_version(code, data)

        if request.method == "GET":
            p.update({
                'clouds': clouds,
                'systems': systems,
                'blueprints': blueprints,
            })

            return render(request, Html.environmentEdit, {'env': data, 'clouds': clouds, 'systems': systems,
                                                          'blueprints': blueprints, 'message': '', 'save': True})
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

                return render(request, Html.environmentEdit, {'env': cpPost, 'clouds': clouds, 'systems': systems,
                                                              'blueprints': blueprints, 'message': form.errors, 'save': True})

            # -- Create a environment, api call
            url = Url.environmentEdit(id, Url.url)
            data = addEnvironmentParam(p)
            # -- API call, get a response
            ApiUtil.requestPut(url, code, data)

            return redirect(Path.environmentList)
    except Exception as ex:
        log.error(code, None, ex)

        return render(request, Html.environmentEdit, {'env': request.POST, 'clouds': '', 'systems': '',
                                                      'blueprints': '', 'message': str(ex), 'save': True})


def putBlueprint(param):

    blueprint = param.get('blueprint', None)
    if blueprint != None and blueprint != '':
        blueprint = ast.literal_eval(blueprint)

        param['blueprint_id'] = blueprint.get('id')
        param['version'] = blueprint.get('version')

    return param


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
    candidates_attributes = []
    dic = {
        'cloud_id': int(param.get('candidates_attributes_1')), 'priority': 1}
    candidates_attributes.append(dic)

    if param.get('candidates_attributes_2'):
        dic = {
            'cloud_id': int(param.get('candidates_attributes_2')), 'priority': 2}
        candidates_attributes.append(dic)

    if param.get('candidates_attributes_3'):
        dic = {
            'cloud_id': int(param.get('candidates_attributes_3')), 'priority': 3}
        candidates_attributes.append(dic)

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
