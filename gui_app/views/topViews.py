# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import django.contrib.auth as auth
import json
import requests
from django.contrib.auth.decorators import login_required
from ..enum.FunctionCode import Common
from ..enum.LogType import Message
from ..logs import log

def top(request):
    log.info(Common.top.value, None, None, '')
    return redirect('/ccgui/environment/list/')

