# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
import json
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404, redirect
from ..enum import ApiClass
from ..enum import ResponseType

class Path():
    top = "/ccgui/top/"
    list = "/ccgui/account/list/"

def index(request):
        #-- AccountAPI call, get a response
        url = ApiClass.Account.list.value
        data = {'token' : 'tokenken'}
        r = requests.get(url, data)
        #-- get response
        if r.status_code == ResponseType.Response.OK.value:
            a = json.loads(r.text)
            accounts = a['lists']
            return render(request, "gui_app/account/accountList.html", {'accounts':accounts })
        else:

            return render(request, "gui_app/login.html")

def accountDetail(request, id):

    url = 'http://127.0.0.1:8000/api/v1/account/' +id+ '/detail/'
    data = {'token' : 'toke'}
    r = requests.get(url, data)

    if r.status_code == ResponseType.Response.OK.value:
        account = json.loads(r.text)

        return render(request, "gui_app/account/accountDetail.html",{'ac':account} )
    else:

        return render(request, "gui_app/account/accountDetail.html")

def accountCreate(request):

    if request.method == "POST":
        url = 'http://127.0.0.1:8000/api/v1/account/create/'
        r = requests.get(url)
        p = json.loads(r.text)

        return redirect(Path.list)

    else:

        return render(request, "gui_app/account/accountCreate.html" )
def accountEdit(request, id):
    msg = ''
    if request.method == 'POST':
        account = request.POST
        print(account)
        url = 'http://127.0.0.1:8000/api/v1/account/' +id+ '/update/'
        data = {'token' : 'toke'}
        r = requests.get(url, data)

        if r.status_code == ResponseType.Response.OK.value:
            account = json.loads(r.text)

            return redirect(Path.list)
        else:

            return render(request, "gui_app/account/accountEdit.html",{'ac':account, 'message':msg} )
    else:
        url = 'http://127.0.0.1:8000/api/v1/account/' +id+ '/detail/'
        data = {'token' : 'toke'}
        r = requests.get(url, data)
        account = json.loads(r.text)

        return render(request, "gui_app/account/accountEdit.html",{'ac':account, 'message':msg} )


def accountDelete(request, id):

    url = 'http://127.0.0.1:8000/api/v1/account/'+id+'/delete/'
    r = requests.get(url)
    p = json.loads(r.text)

    return redirect(Path.list)
