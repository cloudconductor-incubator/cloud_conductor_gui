import re
import json
import requests


class Path():
    top = "/ccgui/"
    projectList = "/ccgui/project/list/"
    projectCreate = "/ccgui/project/create/"
    projectDetail = lambda id: "/ccgui/project/{0}/".format(id)
    projectEdit = lambda id: "/ccgui/project/{0}/edit".format(id)

    cloudList = "/ccgui/cloud/list/"
    cloudCreate = "/ccgui/cloud/create/"
    cloudDetail = lambda id: "/ccgui/cloud/{0}/detail".format(id)
    cloudEdit = lambda id: "/ccgui/cloud/{0}/edit".format(id)

    baseImageList = "/ccgui/baseImage/list/"
    baseImageCreate = "/ccgui/baseImage/create/"
    baseImageDetail = lambda id: "/baseImage/project/{0}/".format(id)
    baseImageEdit = lambda id: "/ccgui/baseImage/{0}/edit".format(id)

class Html():
    login = 'gui_app/login.html'
    top = "/ccgui/"
    projectList = "gui_app/project/projectList.html"
    projectCreate = "gui_app/project/projectCreate.html"
    projectDetail = "gui_app/project/projectDetail.html"
    projectEdit = "gui_app/project/projectEdit.html"
    projectDelete = "gui_app/project/projectDetail.html"
    addUser = "gui_app/project/projectAddUser.html"

    cloudList = "gui_app/cloud/cloudList.html"
    cloudDetail = "gui_app/cloud/cloudDetail.html"
    cloudCreate = "gui_app/cloud/cloudCreate.html"
    cloudEdit = "gui_app/cloud/cloudEdit.html"

    baseImageList = "gui_app/baseImage/baseImageList.html"
    baseImageDetail = "gui_app/baseImage/baseImageDetail.html"
    baseImageCreate = "gui_app/baseImage/baseImageCreate.html"
    baseImageEdit = "gui_app/baseImage/baseImageEdit.html"

