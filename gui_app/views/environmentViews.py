# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import html
import requests
import ast
from collections import OrderedDict
from ..forms import environmentForm
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import BlueprintHistoryUtil
from ..utils import SessionUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..utils.BlueprintUtil import get_blueprint_version
from ..enum.FunctionCode import FuncCode
from ..logs import log
PATRITION = '/'


def environmentList(request):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'environment','list') == False:
            return render_to_response(Html.error_403)

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
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'environment','read') == False:
            return render_to_response(Html.error_403)

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
    clouds = None
    systems = None
    blueprints = None
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'environment','create') == False:
            return render_to_response(Html.error_403)

        p = request.POST
        code = FuncCode.environmentCreate.value
        token = request.session['auth_token']
        project_id = request.session['project_id']
        data = {
            'auth_token': token,
            'project_id': project_id
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
                                                                'blueprints': blueprints, 'form': form,
                                                                'message': '', 'save': True})
            # -- add
            inputs = createJson(param)
#             env = addEnvironmentParam(cpPost, inputs)

            # -- Create a environment, api call
            url = Url.environmentCreate
            # -- API call, get a response
            a = ApiUtil.requestPost(
                url, FuncCode.environmentCreate.value, addEnvironmentParam(cpPost, inputs))

            return redirect(Path.environmentList)
    except Exception as ex:
        log.error(FuncCode.environmentCreate.value, None, ex)

        return render(request, Html.environmentCreate, {'env': request.POST, 'clouds': clouds, 'systems': systems,
                                                        'blueprints': blueprints, 'form': '', 'message': str(ex), 'save': True})


def environmentEdit(request, id):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'environment','update') == False:
            return render_to_response(Html.error_403)

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
                                                          'blueprints': blueprints, 'form': '', 'message': '', 'save': True})
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
                                                              'blueprints': blueprints, 'form': form,
                                                              'message': '', 'save': True})

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


def environmentDelete(request, id):
    try:
        if SessionUtil.check_login(request) == False:
            return redirect(Path.logout)
        if SessionUtil.check_permission(request,'environment','destroy') == False:
            return render_to_response(Html.error_403)

        # -- URL and data set
        url = Url.environmentDelete(id, Url.url)
        data = {'auth_token': request.session['auth_token']}
        ApiUtil.requestDelete(url, FuncCode.environmentDelete.value, data)

        return redirect(Path.environmentList)
    except Exception as ex:
        log.error(FuncCode.environmentDelete.value, None, ex)

        return render(request, Html.environmentDetail, {'env': '', 'message': ex})


def createForm(js, keyParent):
    ''' json to HTML input field '''

    PATRITION = '/'
    inpt = []

    if isinstance(js, dict):
        for k in js.keys():
            v = js[k]
            kk = keyParent + PATRITION + k
            if keyParent == '':
                kk = k
            inpt.extend(createForm(v, kk))
    else:
        inpt.append((keyParent, js))

    return inpt


def environmentAjaxBlueprint(request):
    try:
        p = request.GET
        bp = putBlueprint(p.copy())

        code = FuncCode.environmentCreate.value
        token = request.session['auth_token']
        param = BlueprintHistoryUtil.get_blueprint_history_list(
            code, token, bp['blueprint_id'], bp['version'])

        ff = createForm(param, 'json')
        key = param.keys()
        value = param.values()

        return render(request, Html.environmentAjaxBlueprint, {'name': key,'blueprints': value })

    except Exception as ex:
        log.error(code, None, ex)

        return render(request, Html.environmentAjaxBlueprint, {})


# def environmentAjaxBlueprint2(request):
#     try:
#         p = request.GET
#         bp = putBlueprint(p.copy())
#
#         code = FuncCode.environmentCreate.value
#         token = request.session['auth_token']
#         param = BlueprintHistoryUtil.get_blueprint_history_list(
#             code, token, bp['blueprint_id'], bp['version'])
#
#         ff = createForm2(param, 'json')
#
#         return render(request, Html.environmentAjaxBlueprint, {'blueprint': param, 'inputs': ff})
#
#     except Exception as ex:
#         log.error(code, None, ex)
#
#         return render(request, Html.environmentAjaxBlueprint2, {})
#
#
# def createForm2(js, keyParent):
#     ''' json to HTML input field '''
#
#     PATRITION = '/'
#     inpt = []
#
#     if isinstance(js, dict):
#         for k in js.keys():
#             v = js[k]
#             kk = keyParent + PATRITION + k
#             if keyParent == '':
#                 kk = k
#             inpt.extend(createForm(v, kk))
#     else:
#         inpt.append((keyParent, js))
#
#     return inpt


def putBlueprint(param):

    blueprint = param.get('blueprint', None)
    if blueprint != None and blueprint != '':
        blueprint = ast.literal_eval(blueprint)

        param['blueprint_id'] = blueprint.get('id')
        param['version'] = blueprint.get('version')

    return param


def putMap(jmap, key, val):
    ''' KEY VALUE parameter to DICT '''
    if key.find(PATRITION) != -1:
        kf = key.find(PATRITION)
        k1 = key[0:kf]
        k2 = key[kf + 1:]
        if k1 not in jmap:
            jmap[k1] = {}
        putMap(jmap[k1], k2, val)
    else:
        jmap[key] = val

def createJson(prm):
    ''' HTTP parameter to DICT  '''
    pmap = {}
    for k in prm.keys():
        if k.find('json/') == 0:
            kp = k[5:]
            putMap(pmap, kp, prm[k])

    return pmap


def addEnvironmentParam(param, temp_param):
    # candidates_attributes
    print(param)
    candidates_attributes = []
    dic = {
        "cloud_id": param.get("candidates_attributes_1"), "priority": "1"}
    candidates_attributes.append(dic)

    if param.get("candidates_attributes_2"):
        dic = {
            "cloud_id": param.get("candidates_attributes_2"), "priority": "2"}
        candidates_attributes.append(dic)

    if param.get("candidates_attributes_3"):
        dic = {
            "cloud_id": param.get("candidates_attributes_3"), "priority": "3"}
        candidates_attributes.append(dic)

    print(candidates_attributes)
    data = {
        "auth_token": param.get("auth_token"),
        "project_id": param.get("project_id"),
        "system_id": param.get("system_id"),
        "blueprint_id": str(param.get("blueprint_id")),
        "version": str(param.get("version")),
        "name": param.get("name"),
        "description": param.get("description", ""),
        "candidates_attributes": candidates_attributes
    }

    if param.get("user_attributes"):
        data["user_attributes"] = param.get("user_attributes")

    print(str(temp_param).replace('\'', '\"'))
    if temp_param:
        data["template_parameters"] = str(temp_param).replace('\'', '\"')

    return data
