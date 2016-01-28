# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from ..enum.LogType import Message
from ..enum.FunctionCode import FuncCode
from ..logs import log


def top(request):
    code = FuncCode.top.value
    log.info(code, None, None, '')
    return redirect('/ccgui/environment/list/')
