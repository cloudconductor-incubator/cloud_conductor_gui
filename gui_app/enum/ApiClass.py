from enum import Enum

class u():
    url = 'http://127.0.0.1:8000/api/v1/'

class Token(Enum):
    token = u.url + 'tokens'

class Project(Enum):
#     url = 'http://127.0.0.1:8000/api/v1/'
#     projectList = u.url + 'project/list/'
    list = u.url + 'projects/'
    detail = u.url + 'projects/detail/'
    create = u.url + 'projects/create/'
    update = u.url + 'projects/update/'
    delete = u.url + 'projects/delete/'

class Account(Enum):
    list = u.url + 'account/list/'
    detail = u.url + 'account/detail/'
    create = u.url + 'account/create/'
    update = u.url + 'account/update/'
    delete = u.url + 'account/delete/'

class Cloud(Enum):
    list = u.url + 'cloud/list/'
    detail = u.url + 'cloud/detail/'
    create = u.url + 'cloud/create/'
    update = u.url + 'cloud/update/'
    delete = u.url + 'cloud/delete/'

class BaseImage(Enum):
    list = u.url + 'baseImage/list/'
    detail = u.url + 'baseImage/detail/'
    create = u.url + 'baseImage/create/'
    update = u.url + 'baseImage/update/'
    delete = u.url + 'baseImage/delete/'

class Blueprint(Enum):
    list = u.url + 'blueprint/list/'
    detail = u.url + 'blueprint/detail/'
    create = u.url + 'blueprint/create/'
    update = u.url + 'blueprint/update/'
    delete = u.url + 'blueprint/delete/'
    parameters = u.url + 'blueprint/parameters/'

class Pattern(Enum):
    list = u.url + 'pattern/list/'
    detail = u.url + 'pattern/detail/'
    create = u.url + 'pattern/create/'
    update = u.url + 'pattern/update/'
    delete = u.url + 'pattern/delete/'

class System(Enum):
    list = u.url + 'system/list/'
    detail = u.url + 'system/detail/'
    create = u.url + 'system/create/'
    update = u.url + 'system/update/'
    delete = u.url + 'system/delete/'
    switch = u.url + 'system/switch/'

class Environment(Enum):
    list = u.url + 'environment/list/'
    detail = u.url + 'environment/detail/'
    create = u.url + 'environment/create/'
    update = u.url + 'environment/update/'
    delete = u.url + 'environment/delete/'
    eventList = u.url + 'environment/eventList/'
    event = u.url + 'environment/event/'
    sendEvent = u.url + 'environment/sendEvent/'
    rebuild = u.url + 'environment/rebuild/'

class Application(Enum):
    list = u.url + 'application/list/'
    detail = u.url + 'application/detail/'
    create = u.url + 'application/create/'
    update = u.url + 'application/update/'
    delete = u.url + 'application/delete/'
    deploy = u.url + 'application/deploy/'

class ApplicationHistory(Enum):
    list = u.url + 'application_history/list/'
    detail = u.url + 'application_history/detail/'
    create = u.url + 'application_history/create/'
    update = u.url + 'application_history/update/'
    delete = u.url + 'application_history/delete/'

