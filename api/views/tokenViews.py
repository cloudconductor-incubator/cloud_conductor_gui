from django.shortcuts import render

# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from django.http import HttpResponse
from gui_app.models import t_project
from api.views.commonViews import render_json_response

def token(request):

    dict = OrderedDict([
        ('auth_token', "1ozvZ5BU1GMy5sMNrykq"),

    ])

    return render_json_response(request, dict)
