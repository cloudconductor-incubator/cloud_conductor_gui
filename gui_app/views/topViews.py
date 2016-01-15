# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..logs import log

def top(request):
    code = FuncCode.top.value
    log.info(code, None, None, '')
    return redirect('/ccgui/environment/list/')

