# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,render_to_response
import json
import ast
from ..forms import w_applicationForm
from ..forms import w_environmentForm
from ..forms import environmentSelectForm
from ..forms import systemSelectForm
from ..forms import systemForm
from ..utils import ApiUtil
from ..utils import SystemUtil
from ..utils import ApplicationUtil
from ..utils import EnvironmentUtil
from ..utils import ApplicationHistoryUtil
from ..utils.BlueprintUtil import get_blueprint_version
from ..utils import StringUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..utils import SessionUtil
from ..enum.FunctionCode import FuncCode
from ..enum.ApplicationType import ApplicaionType
from ..enum.ProtocolType import ProtocolType
from ..logs import log


def systemSelect(request):
    try:
        session = request.session

        id = session.get('project_id')
        token = session.get('auth_token')
        code = FuncCode.newapp_system.value
        list = SystemUtil.get_system_list2(code, token, id)

        if request.method == "GET":
            system = session.get('system')

            return render(request, Html.newapp_systemSelect, {"list": list, 'system': system, 'message': ''})
        elif request.method == "POST":
            p = request.POST
            cpPost = p.copy()
            system = putSystem(cpPost)
            form = environmentSelectForm(system)
            if not form.is_valid():

                return render(request, Html.newapp_systemSelect, {"list": list, 'system': system,'form': form, 'message': form.errors})

            session['system'] = system

            return redirect(Path.newapp_applicationCreate)
    except Exception as ex:
        log.error(FuncCode.newapp_system.value, None, ex)

        return render(request, Html.newapp_systemSelect, {"system": '', 'message': str(ex)})


def systemCreate(request):
    try:
        code = FuncCode.newapp_system.value
        if request.method == "GET":
            system = request.session.get('system')

            return render(request, Html.newapp_systemCreate, {"system": system, 'message': ''})
        elif request.method == "POST":
            param = request.POST

            # -- Validate check
            form = systemForm(param)
            if not form.is_valid():

                return render(request, Html.newapp_systemCreate, {"system": param,'form': form, 'message': ''})

            # -- Session add
            system = systemPut(param)
            request.session['system'] = system

            return redirect(Path.newapp_applicationCreate)
    except Exception as ex:
        log.error(FuncCode.newapp_system.value, None, ex)

        return render(request, Html.newapp_systemCreate, {"application": '', 'message': str(ex)})


def applicationCreate(request):
    try:
        code = FuncCode.newapp_application.value
        if request.method == "GET":
            application = request.session.get('application')

            return render(request, Html.newapp_applicationCreate, {"app": application, 'apptype': list(ApplicaionType),
                                                                   'protocol': list(ProtocolType), 'message': ''})
        elif request.method == "POST":
            param = request.POST

            # -- Validate check
            form = w_applicationForm(param)
            if not form.is_valid():

                return render(request, Html.newapp_applicationCreate, {"application": param, 'apptype': list(ApplicaionType),
                                                                       'protocol': list(ProtocolType),'form': '', 'message': form.errors})

            # -- Session add
            application = applicationPut(param)
            request.session['application'] = application

            return redirect(Path.newapp_environmentSelect)
    except Exception as ex:
        log.error(FuncCode.newapp_application.value, None, ex)

        return render(request, Html.newapp_applicationCreate, {"application": '', 'apptype': list(ApplicaionType),
                                                               'protocol': list(ProtocolType), 'message': str(ex)})


def environmentSelect(request):
    try:
        code = FuncCode.newapp_environment.value
        session = request.session
        token = session['auth_token']
        project_id = session['project_id']
        list = EnvironmentUtil.get_environment_list2(code, token, project_id)

        if request.method == "GET":
            environment = session.get('environment')

            return render(request, Html.newapp_environmentSelect, {"list": list, 'environment': environment, 'message': ''})
        elif request.method == "POST":
            p = request.POST
            cpPost = p.copy()
            environment = putEnvironment(cpPost)
            form = environmentSelectForm(environment)
            if not form.is_valid():

                return render(request, Html.newapp_environmentSelect, {"list": list, 'environment': environment,'form': form,
                                                                       'message': ''})

            request.session['environment'] = environment

            return redirect(Path.newapp_confirm)
    except Exception as ex:
        log.error(FuncCode.newapp_environment.value, None, ex)

        return render(request, Html.newapp_environmentSelect, {"list": '', 'environment': '', 'message': ''})


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
            environment = request.session.get('environment')

            return render(request, Html.newapp_environmentCreate, {'clouds': clouds, 'systems': systems,
                                                                   'blueprints': blueprints, 'env': environment,
                                                                   'message': ''})
        elif request.method == "POST":
            param = request.POST
            # -- Validate check
            form = w_environmentForm(param)
            if not form.is_valid():

                return render(request, Html.newapp_environmentCreate, {'clouds': clouds, 'systems': systems,
                                                                       'blueprints': blueprints, 'env': param,
                                                                       'message': form.errors})

            # -- Session add
            application = applicationPut(param)
            request.session['environment'] = environment

            return redirect(Path.newapp_environmentCreate)
    except Exception as ex:
        log.error(FuncCode.newapp_environment.value, None, ex)

        return render(request, Html.newapp_environmentCreate, {"env": '', 'message': str(ex)})


def confirm(request):
    #     try:
    session = request.session
    sys_session = session.get('system')
    app_session = session.get('application')
    env_session = session.get('environment')

    if request.method == "GET":

        return render(request, Html.newapp_confirm, {"system": sys_session, 'application': app_session, 'environment': env_session, 'message': ''})
    elif request.method == "POST":
        session = request.session
        code = FuncCode.newapp_confirm.value
        token = session.get('auth_token')
        project_id = ''

        # -- application createt
        application = ApplicationUtil.create_application(code, token, sys_session.get('id'),
                        app_session.get('name'), app_session.get('description'), app_session.get('domain'))

        # -- applicationHistory create
        history = ApplicationHistoryUtil.create_history(code, token, application.get('id'), app_session.get('url'),
                        app_session.get('type'), app_session.get('protocol'), app_session.get('revision'),
                        app_session.get('pre_deploy'), app_session.get('post_deploy'), app_session.get('parameters'))

        # -- application deploy
        deploy = ApplicationUtil.deploy_application(
            code, token, env_session.get('id'), application.get('id'))

        # -- session delete
        sessionDelete(session)

        return redirect(Path.top)
#     except Exception as ex:
#         log.error(FuncCode.newapp_confirm.value, None, ex)
#         session = request.session
#
#         return render(request, Html.newapp_confirm, {"project": session.get('project'),'cloud': session.get('cloud'),
#                                                           'baseImage': session.get('baseimage'), 'message': str(ex)})


def putEnvironment(param):

    environment = param.get('environment', None)
    if environment != None and environment != '':
        environment = ast.literal_eval(environment)

        param['id'] = blueprint.get('id')
        param['name'] = blueprint.get('name')

    return param


def putSystem(param):

    system = param.get('id', None)
    if system != None and system != '':
        system = ast.literal_eval(system)

        param['id'] = system.get('id')
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


def applicationPut(req):
    if StringUtil.isEmpty(req):
        return None

    application = {
        'name': req.get('name'),
        'description': req.get('description'),
        'domain': req.get('domain'),
        'url': req.get('url'),
        'type': req.get('type'),
        'protocol': req.get('protocol'),
        'revision': req.get('revision'),
        'pre_deploy': req.get('pre_deploy'),
        'post_deploy': req.get('post_deploy'),
        'parameters': req.get('parameters'),
    }
    return application


def sessionDelete(session):

    if 'system' in session:
        del session['system']

    if 'environment' in session:
        del session['environment']

    if 'application' in session:
        del session['application']
