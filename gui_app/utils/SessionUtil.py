import re
from collections import OrderedDict
from ..utils import RoleUtil
from ..utils import ApiUtil
from ..utils import StringUtil
from ..utils import ProjectUtil
from ..utils.ApiUtil import Url
from ..enum import ResponseType
from ..enum.FunctionCode import FuncCode
from ..logs import log


def edit_project_session(code, token, session, id=None, name=None):

    project_list = ProjectUtil.get_project_list3(code, token)

    session['project_list'] = project_list

    if session.get('project_id') == id:

        if not name:
            session['project_id'] = ''
            session['project_name'] = ''
        else:
            session['project_id'] = id
            session['project_name'] = name
#         if id in project_list:
#             for project in project_list:
#                 project_id = project.get('id')
#                 project_name = project.get('name')
#                 break

