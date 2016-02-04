# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
import json
import requests
import ast
from collections import OrderedDict
from ..forms import w_appenv_environmentForm
from ..forms import systemSelectForm
from ..forms import blueprintSelectForm
from ..utils import ApiUtil
from ..utils import SystemUtil
from ..utils import EnvironmentUtil
from ..utils import BlueprintUtil
from ..utils.BlueprintUtil import get_blueprint_version
from ..utils import StringUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..enum.FunctionCode import FuncCode
from ..enum.MessageCode import Info
from ..logs import log


def systemSelect(request):
    try:
        session = request.session

        id = session.get('project_id')
        token = session.get('auth_token')
        code = FuncCode.appenv_system.value
        list = SystemUtil.get_system_list(code, token, id)

        if request.method == "GET":
            system = session.get('w_sys_select')

            return render(request, Html.envapp_systemSelect,
                          {"list": list, 'system': system, 'message': '',
                           'wizard_code': Info.WizardSystem.value})
        elif request.method == "POST":
            p = request.POST
            cpPost = p.copy()
            system = putSystem(cpPost)
            form = systemSelectForm(system)
            if not form.is_valid():

                return render(request, Html.envapp_systemSelect,
                              {"list": list, 'system': system,
                               'form': form,
                               'message': '',
                               'wizard_code': Info.WizardSystem.value})

            session['w_sys_select'] = system

            return redirect(Path.envapp_bluprintSelect)
    except Exception as ex:
        log.error(FuncCode.appenv_system.value, None, ex)

        return render(request, Html.envapp_systemSelect,
                      {"system": '', 'message': str(ex),
                       'wizard_code': Info.WizardSystem.value})


def blueprintSelect(request):
    try:
        code = FuncCode.appenv_blueprint.value
        session = request.session
        token = session['auth_token']
        project_id = session['project_id']
        list = BlueprintUtil.get_blueprint_list(code, token, project_id)
        print(list)

        if request.method == "GET":
            blueprint = session.get('w_bp_select')

            return render(request, Html.envapp_bluprintSelect,
                          {'list': list, 'blueprint': blueprint,
                           'message': '',
                           'wizard_code': Info.WizardSystem.value})
        elif request.method == "POST":
            p = request.POST
            cpPost = p.copy()
            blueprint = putBlueprint(cpPost)
            form = blueprintSelectForm(blueprint)
            if not form.is_valid():

                return render(request, Html.envapp_bluprintSelect,
                              {'list': list, 'blueprint': blueprint,
                               'form': form,
                               'wizard_code': Info.WizardSystem.value})

            request.session['w_bp_select'] = blueprint

            return redirect(Path.envapp_environmentCreate)
    except Exception as ex:
        log.error(FuncCode.appenv_blueprint.value, None, ex)

        return render(request, Html.envapp_bluprintSelect,
                      {'list': '', 'blueprint': '', 'message': str(ex),
                       'wizard_code': Info.WizardSystem.value})


def environmentCreate(request):
    try:
        code = FuncCode.newapp_environment.value
        session = request.session
        data = {
            'auth_token': session.get('auth_token'),
            'project_id': session.get('project_id')
        }

        clouds = ApiUtil.requestGet(Url.cloudList, code, data)
        systems = ApiUtil.requestGet(Url.systemList, code, data)
        blueprints = get_blueprint_version(code, data)

        if request.method == "GET":
            environment = request.session.get('w_env_create')

            return render(request, Html.envapp_environmentCreate,
                          {'clouds': clouds, 'systems': None,
                           'blueprints': blueprints, 'env': environment,
                           'message': '', 'create': True})
        elif request.method == "POST":
            param = request.POST
            # -- Validate check
            form = w_appenv_environmentForm(param)
            if not form.is_valid():

                return render(request, Html.envapp_environmentCreate,
                              {'clouds': clouds, 'systems': None,
                               'blueprints': blueprints, 'env': param,
                               'form': form, 'create': True})

            # -- Session add
            environment = environmentPut(param)
            request.session['w_env_create'] = environment

            return redirect(Path.envapp_confirm)
    except Exception as ex:
        log.error(FuncCode.appenv_environment.value, None, ex)

        return render(request, Html.envapp_environmentCreate,
                      {'clouds': clouds, 'systems': systems,
                       'blueprints': blueprints, 'env': request.POST,
                       'create': True, 'message': str(ex)})


def confirm(request):
    try:
        session = request.session
        sys_session = session.get('w_sys_select')
        bp_session = session.get('w_bp_select')
        env_session = session.get('w_env_create')

        if request.method == "GET":

            return render(request, Html.envapp_confirm,
                          {"system": sys_session, 'blueprint': bp_session,
                           'environment': env_session, 'message': ''})
        elif request.method == "POST":
            session = request.session
            code = FuncCode.appenv_confirm.value

            env_session.update(bp_session)
            env_session.update(sys_session)

            EnvironmentUtil.create_environment(code, env_session,
                                               request.session)

            # -- session delete
            sessionDelete(session)

            return redirect(Path.top)
    except Exception as ex:
        log.error(FuncCode.appenv_confirm.value, None, ex)
        session = request.session

        return render(request, Html.envapp_confirm,
                      {'system': sys_session, 'blueprint': bp_session,
                       'environment': env_session,
                       'message': str(ex)})


def putBlueprint(param):

    blueprint = param.get('id', None)
    if blueprint is not None and blueprint != '':
        blueprint = ast.literal_eval(blueprint)

        param['id'] = str(blueprint.get('id'))
        param['name'] = blueprint.get('name')

    return param


def putEnvironment(param):

    environment = param.get('id', None)
    if environment is not None and environment != '':
        environment = ast.literal_eval(environment)

        param['id'] = str(environment.get('id'))
        param['name'] = environment.get('name')

    return param


def putSystem(param):

    system = param.get('id', None)
    if system is not None and system != '':
        system = ast.literal_eval(system)

        param['id'] = str(system.get('id'))
        param['name'] = system.get('name')

    return param


def systemPut(req):
    if StringUtil.isEmpty(req):
        return None

    system = {
        'id': req.get('id'),
        'name': req.get('name'),
    }
    return system


def environmentPut(req):
    if StringUtil.isEmpty(req):
        return None

    environment = {
        'id': req.get('id'),
        'name': req.get('name'),
    }
    return environment


def sessionDelete(session):

    if 'w_sys_select' in session:
        del session['w_sys_select']

    if 'w_env_create' in session:
        del session['w_env_create']

    if 'w_bp_select' in session:
        del session['w_bp_select']
