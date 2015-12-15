from enum import Enum

class FuncCode(Enum):
    login = 'GO010'
    top = 'GO020'
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



class Common(Enum):
    top = 'GM020'

class Login(Enum):
    login = 'CO1110'

class Project(Enum):
    list = 'GM1110'
    detail ='GM1150'
    create ='GM1120'
    edit ='GM1130'
    delete ='GM1140'

class Cloud(Enum):
    list = 'GM1210'
    detail = 'GM1250'
    create = 'GM1220'
    edit = 'GM1230'
    delete = 'GM1240'

class System(Enum):
    list = 'GM2510'
    detail = 'GM2550'
    create = 'GM2520'
    edit = 'GM2530'
    delete = 'GM2540'

class Environment(Enum):
    list = 'GM2110'
    detail = 'GM2150'
    create = 'GM2120'
    edit = 'GM2130'
    delete = 'GM2140'

class Application(Enum):
    list = 'GM2310'
    detail = 'GM2350'
    create = 'GM2320'
    edit = 'GM2330'
    delete = 'GM2340'

class Blueprint(Enum):
    list = 'GM2410'
    detail = 'GM2450'
    create = 'GM2420'
    edit = 'GM2430'
    delete = 'GM2440'

class Pattern(Enum):
    list = 'GM2410'
    detail = 'GM2450'
    create = 'GM2420'
    edit = 'GM2430'
    delete = 'GM2440'

class GM24(Enum):
    list = 'GM2310'
    detail = 'GM2350'
    create = 'GM2320'
    edit = 'GM2330'
    delete = 'GM2340'
