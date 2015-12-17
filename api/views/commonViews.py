from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse

def render_json_response(request, data, status=None):
    json_str = json.dumps(data, ensure_ascii=False, indent=2)

    if request.method == 'GET':
        callback = request.GET.get('callback')
        if not callback:
            callback = request.REQUEST.get('callback')
        if callback:
            json_str = "%s(%s)" % (callback, json_str)
            response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
        else:
            response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)

    elif  request.method == 'POST':
        callback = request.POST.get('callback')
        if not callback:
            callback = request.REQUEST.post('callback')
        if callback:
            json_str = "%s(%s)" % (callback, json_str)
            response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
        else:
            response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)

    return response
