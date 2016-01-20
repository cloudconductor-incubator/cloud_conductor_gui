from enum import Enum

class FuncCode(Enum):
    login = 'GO010'
    top = 'GO020'
    projectChange = 'GO030'
    projectList = 'GM1110'
    projectDetail ='GM1150'
    projectCreate ='GM1120'
    projectEdit ='GM1130'
    projectDelete ='GM1140'

    cloudList = 'GM1210'
    cloudDetail = 'GM1250'
    cloudCreate = 'GM1220'
    cloudEdit = 'GM1230'
    cloudDelete = 'GM1240'

    baseImageList = 'GM1310'
    baseImageDetail = 'GM1320'
    baseImageCreate = 'GM1330'
    baseImageEdit = 'GM1340'
    baseImageDelete = 'GM1350'

    environmentList = 'GM2110'
    environmentDetail = 'GM2120'
    environmentCreate = 'GM2130'
    environmentEdit = 'GM2140'
    environmentDelete = 'GM2150'

    applicationList = 'GM2210'
    applicationDetail = 'GM2220'
    applicationCreate = 'GM2230'
    applicationEdit = 'GM2240'
    applicationDelete = 'GM2250'

    patternList = 'GM2310'
    patternDetail = 'GM2320'
    patternCreate = 'GM2330'
    patternEdit = 'GM2340'
    patternDelete = 'GM2350'

    blueprintList = 'GM2410'
    blueprintDetail = 'GM2420'
    blueprintCreate = 'GM2430'
    blueprintEdit = 'GM2440'
    blueprintDelete = 'GM2450'

    systemList = 'GM2510'
    systemDetail = 'GM2520'
    systemCreate = 'GM2530'
    systemEdit = 'GM2540'
    systemDelete = 'GM2550'

    accountList = 'GM3510'
    accountDetail = 'GM3520'
    accountCreate = 'GM3530'
    accountEdit = 'GM3540'
    accountDelete = 'GM3550'

    roleList = 'GM3210'
    roleDetail = 'GM3220'
    roleCreate = 'GM3230'
    roleEdit = 'GM3240'
    roleDelete = 'GM3250'

    cloudReg_project = 'GW420-1'
    cloudReg_cloud = 'GW420-2'
    cloudReg_baseimage = 'GW420-3'
    cloudReg_confirm = 'GW420-4'

    newapp_system = 'GW120-1'
    newapp_application = 'GW120-2'
    newapp_environment = 'GW120-3'
    newapp_confirm = 'GW120-4'

    appenv_system = 'GW250-1'
    appenv_blueprint = 'GW250-2'
    appenv_environment = 'GW250-3'
    appenv_confirm = 'GW250-4'

    appDep_application = 'GW350-1'
    appDep_environment = 'GW350-2'
    appDep_confirm = 'GW350-3'


