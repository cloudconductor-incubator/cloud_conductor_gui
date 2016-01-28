# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect,render_to_response
import json
import requests
import ast
from collections import OrderedDict
from ..forms import w_applicationForm
from ..forms import w_environmentForm
from ..forms import systemForm
from ..utils import RoleUtil
from ..utils import ValiUtil
from ..utils import ApiUtil
from ..utils import ApplicationUtil
from ..utils import EnvironmentUtil
from ..utils.BlueprintUtil import get_blueprint_version
from ..utils import StringUtil
from ..utils.PathUtil import Path
from ..utils.PathUtil import Html
from ..utils.ApiUtil import Url
from ..utils.ErrorUtil import ApiError
from ..utils import SessionUtil
from ..enum import ResponseType
from ..enum.LogType import Message
from ..enum.CloudType import CloudType
from ..enum.OSVersion import OSVersion
from ..enum.FunctionCode import FuncCode
from ..logs import log


def applicationSelect(request):
    try:
        session = request.session
        code = FuncCode.appDep_application.value
        token = session.get('auth_token')
        project_id = session.get('project_id')

        list = ApplicationUtil.get_application_list2(code, token, project_id=None)
        print(list)

        if request.method == "GET":
            application = request.session.get('application')
            print(application)
            return render(request, Html.appdeploy_applicationSelect, {'list': list, 'application': application, 'message': ''})
        elif request.method == "POST":
            param = request.POST

            # -- Session add
            application = applicationPut(param)
            request.session['application'] = application

            return redirect(Path.appdeploy_environmentSelect)
    except Exception as ex:
        log.error(FuncCode.appDep_application.value, None, ex)

        return render(request, Html.appdeploy_applicationSelect, {'application': '', 'message': str(ex)})


def environmentSelect(request):
    try:
        code = FuncCode.appDep_environment.value
        session = request.session
        environment = session.get('environment')

        if request.method == "GET":
            token = session['auth_token']
            project_id = session['project_id']

            list = EnvironmentUtil.get_environment_list2(code, token, project_id)

            return render(request, Html.appdeploy_environmentSelect, {"list": list, 'environment': environment, 'message': ''})
        elif request.method == "POST":
            param = request.POST

            environment = environmentPut(param)
            request.session['environment'] = environment

            return redirect(Path.appdeploy_confirm)
    except Exception as ex:
        log.error(FuncCode.appDep_environment.value, None, ex)

        return render(request, Html.appdeploy_environmentSelect, {"list": '', 'environment': '', 'message': str(ex)})



def confirm(request):
    try:
        code = FuncCode.appDep_confirm.value
        session = request.session
        app_session = session.get('application')
        env_session = session.get('environment')

        if request.method == "GET":

            return render(request, Html.appdeploy_confirm, {'application': app_session, 'environment': env_session, 'message': ''})
        elif request.method == "POST":
            session = request.session
            code = FuncCode.newapp_confirm.value
            token = session.get('auth_token')
            project_id = ''

            env_id = env_session.get('id')
            app_id = app_session.get('id')


            # -- environment create

            # -- application deploy
            ApplicationUtil.deploy_application(code, token, env_id, app_id)

            # -- session delete
            sessionDelete(session)

            return redirect(Path.top)
    except Exception as ex:
        log.error(FuncCode.newapp_confirm.value, None, ex)
        session = request.session

        return render(request, Html.appdeploy_confirm, {"application": session.get('application'),
                                                        'environment': session.get('environment'), 'message': str(ex)})


def environmentPut(req):
    if StringUtil.isEmpty(req):
        return None

    env = req.get('id', None)
    if StringUtil.isNotEmpty(env):
        env = ast.literal_eval(env)

        environment = {
            'id': str(env.get('id')),
            'name': env.get('name'),
        }
        return environment
    else:
        return env


def applicationPut(req):
    if StringUtil.isEmpty(req):
        return None

    app = req.get('id', None)
    if StringUtil.isNotEmpty(app):
        app = ast.literal_eval(app)

        application = {
            'id': str(app.get('id')),
            'name': app.get('name'),
        }
        return application
    else:
        return app


def putBlueprint(param):

    blueprint = param.get('blueprint', None)
    if blueprint != None and blueprint != '':
        blueprint = ast.literal_eval(blueprint)

        param['blueprint_id'] = blueprint.get('id')
        param['version'] = blueprint.get('version')

    return param


def sessionDelete(session):

    if 'environment' in session:
        del session['environment']

    if 'application' in session:
        del session['application']