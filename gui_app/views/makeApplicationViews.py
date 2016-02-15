# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
import json
import ast
from ..forms import w_applicationForm
from ..forms import w_environmentForm
from ..forms import environmentForm
from ..forms import environmentSelectForm
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
from ..utils import SessionUtil
from ..enum.FunctionCode import FuncCode
from ..enum.ApplicationType import ApplicaionType
from ..enum.ProtocolType import ProtocolType
from ..enum.MessageCode import Info
from ..logs import log


def systemSelect(request):
    try:
        session = request.session

        id = session.get('project_id')
        token = session.get('auth_token')
        code = FuncCode.newapp_system.value
        list = SystemUtil.get_system_list(code, token, id)

        if request.method == "GET":
            system = session.get('w_sys_select')

            return render(request, Html.newapp_systemSelect,
                          {"list": list, 'system': system, 'message': '',
                           'wizard_code': Info.WizardSystem.value})
        elif request.method == "POST":
            p = request.POST
            cpPost = p.copy()
            system = putSystem(cpPost)
            form = environmentSelectForm(system)
            if not form.is_valid():

                return render(request, Html.newapp_systemSelect,
                              {"list": list, 'system': system, 'form': form,
                               'message': '',
                               'wizard_code': Info.WizardSystem.value})

            session['w_sys_select'] = system

            return redirect(Path.newapp_applicationCreate)
    except Exception as ex:
        log.error(FuncCode.newapp_system.value, None, ex)

        return render(request, Html.newapp_systemSelect,
                      {"system": '', 'message': str(ex),
                       'wizard_code': Info.WizardSystem.value})


def systemCreate(request):
    try:
        code = FuncCode.newapp_system.value
        if request.method == "GET":

            return render(request, Html.newapp_systemCreate,
                          {'message': ''})
        elif request.method == "POST":
            param = request.POST

            # -- Validate check
            form = systemForm(param)
            if not form.is_valid():

                return render(request, Html.newapp_systemCreate,
                              {"system": param, 'form': form, 'message': ''})

            system = SystemUtil.create_system(
                code, request.session.get('auth_token'),
                request.session.get('project_id'),
                form.data)

            # -- Session add

            request.session['w_sys_select'] = {
                "id": system.get("id"), "name": system.get("name")}

            return redirect(Path.newapp_applicationCreate)
    except Exception as ex:
        log.error(FuncCode.newapp_system.value, None, ex)

        return render(request, Html.newapp_systemCreate,
                      {"application": '', 'message': str(ex)})


def applicationCreate(request):
    try:
        code = FuncCode.newapp_application.value
        if request.method == "GET":
            application = request.session.get('w_app_create')

            return render(request, Html.newapp_applicationCreate,
                          {"app": application,
                           "history": application,
                           'apptype': list(ApplicaionType),
                           'protocol': list(ProtocolType), 'message': ''})
        elif request.method == "POST":
            param = request.POST

            # -- Validate check
            form = w_applicationForm(param)
            if not form.is_valid():

                return render(request, Html.newapp_applicationCreate,
                              {"app": param,
                               "history": param,
                               'apptype': list(ApplicaionType),
                               'protocol': list(ProtocolType), 'form': form,
                               'message': ''})

            # -- Session add
            application = applicationPut(param)
            request.session['w_app_create'] = application

            return redirect(Path.newapp_environmentSelect)
    except Exception as ex:
        log.error(FuncCode.newapp_application.value, None, ex)

        return render(request, Html.newapp_applicationCreate,
                      {"application": '', 'apptype': list(ApplicaionType),
                       'protocol': list(ProtocolType), 'message': str(ex)})


def environmentSelect(request):
    try:
        code = FuncCode.newapp_environment.value
        session = request.session
        token = session['auth_token']
        project_id = session['project_id']
        list = EnvironmentUtil.get_environment_list_system_id(
            code, token, project_id, session['w_sys_select']['id'])

        if request.method == "GET":
            environment = session.get('w_env_select')

            env = None
            if environment is not None:
                env = ast.literal_eval(environment["id"])

            return render(request, Html.newapp_environmentSelect,
                          {"list": list, 'environment': env,
                           'message': '',
                           'wizard_code': Info.WizardSystem.value})
        elif request.method == "POST":
            p = request.POST
            cpPost = p.copy()
            environment = putEnvironment(cpPost)
            form = environmentSelectForm(environment)
            if not form.is_valid():

                return render(request, Html.newapp_environmentSelect,
                              {"list": list, 'environment': environment,
                               'form': form, 'message': '',
                               'wizard_code': Info.WizardSystem.value})

            request.session['w_env_select'] = environment

            return redirect(Path.newapp_confirm)
    except Exception as ex:
        log.error(FuncCode.newapp_environment.value, None, ex)

        return render(request, Html.newapp_environmentSelect,
                      {"list": '', 'environment': '', 'message': '',
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
            # environment = request.session.get('w_env_create')

            return render(request, Html.newapp_environmentCreate,
                          {'clouds': clouds, 'systems': systems,
                           'blueprints': blueprints,
                           'create': True,
                           'message': ''})

        elif request.method == "POST":
            p = request.POST
            if p.get("env_id"):
                env = EnvironmentUtil.get_environment_detail(
                    FuncCode.newapp_environment.value,
                    request.session.get('auth_token'), p.get("env_id"))
                ret = 0
                if env["status"] == 'ERROR':
                    ret = 1
                elif env["status"] == 'CREATE_COMPLETE':
                    ret = 2

                return HttpResponse(json.dumps({'ret': ret}),
                                    content_type="application/json")

            # -- Validate check
            cpPost = p.copy()
            param = putBlueprint(cpPost)
            form = environmentForm(param)

            if not form.is_valid():

                return render(request, Html.newapp_environmentCreate,
                              {'clouds': clouds, 'systems': systems,
                               'blueprints': blueprints, 'env': param,
                               'form': form,
                               'create': True,
                               'message': ''})

            # -- Session add

            environment = EnvironmentUtil.create_environment(
                code, param, request.session)

            env = {}
            env = {"id": environment["id"], "name": environment["name"]}
            request.session['w_env_select'] = {"id": str(env)}

            return render(request, Html.newapp_environmentCreate,
                          {'clouds': clouds, 'systems': systems,
                           'blueprints': blueprints, 'env': param,
                           'env_id': environment.get("id"), 'create': True,
                           'message': ''})

    except Exception as ex:
        log.error(FuncCode.newapp_environment.value, None, ex)

        return render(request, Html.newapp_environmentCreate,
                      {"env": '', 'message': str(ex)})


def confirm(request):
    sys_session = None
    app_session = None
    env_session = None
    try:
        session = request.session
        sys_session = session.get('w_sys_select')
        app_session = session.get('w_app_create')
        env_session = session.get('w_env_select')

        if request.method == "GET":

            return render(request, Html.newapp_confirm,
                          {'system': sys_session, 'application': app_session,
                           'environment': ast.literal_eval(env_session["id"]),
                           'message': ''})
        elif request.method == "POST":
            session = request.session
            code = FuncCode.newapp_confirm.value
            token = session.get('auth_token')
            project_id = ''

            # -- application createt
            app_session['system_id'] = sys_session.get('id')
            application = ApplicationUtil.create_application(
                code, token, app_session)

            # -- applicationHistory create
            app_id = application.get('id')
            history = ApplicationHistoryUtil.create_history(
                code, token, application.get('id'), app_session)

            # -- application deploy
            env = ast.literal_eval(env_session["id"])
            deploy = ApplicationUtil.deploy_application(
                code, token, env.get('id'),
                app_id, history.get('id'))

            # -- application deploy
            ApplicationUtil.deploy_application(
                code, token, env.get('id'), app_id)

            # -- session delete
            sessionDelete(session)

            return redirect(Path.top)
    except Exception as ex:
        log.error(FuncCode.newapp_confirm.value, None, ex)
        session = request.session

        return render(request, Html.newapp_confirm,
                      {'system': sys_session, 'application': app_session,
                       'environment': env_session, 'message': str(ex)})


def putEnvironment(param):

    environment = param.get('environment', None)
    if environment is not None and environment != '':
        environment = ast.literal_eval(environment)

        param['id'] = blueprint.get('id')
        param['name'] = blueprint.get('name')

    return param


def putCreateEnvironment(param, env):
    param['id'] = env.get('id')
    param['name'] = env.get('name')

    return param


def putBlueprint(param):

    blueprint = param.get('blueprint', None)
    if blueprint is not None and blueprint != '':
        blueprint = ast.literal_eval(blueprint)

        param['blueprint_id'] = blueprint.get('id')
        param['version'] = blueprint.get('version')

    return param


def putSystem(param):

    system = param.get('id', None)
    if system is not None and system != '':
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

    if 'w_sys_select' in session:
        del session['w_sys_select']

    if 'w_env_select' in session:
        del session['w_env_select']

    if 'w_app_create' in session:
        del session['w_app_create']


def environmentAjaxBlueprint(request):
    try:
        p = request.GET
        bp = putBlueprint(p.copy())

        code = FuncCode.environmentCreate.value
        token = request.session['auth_token']
        param = BlueprintHistoryUtil.get_blueprint_parameters(
            code, token, bp['blueprint_id'], bp['version'])

        ff = createForm(param, 'json')
        key = param.keys()
        value = param.values()

        return render(request, Html.environmentAjaxBlueprint,
                      {'name': key, 'blueprints': param})

    except Exception as ex:
        log.error(code, None, ex)

        return render(request, Html.environmentAjaxBlueprint, {})
