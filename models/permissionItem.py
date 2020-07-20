
import models.permissionResource as pr
import models.permissionMode as pm

import logging

# setup logger for module
_log = logging.getLogger(__name__)


class Permission_Item():
    __name = str()
    __mode = pm.Permission_Mode()
    __resource = pr.Permission_Resource()
    

    def __init__(self,name,mode,resource):
        self.__name = name
        self.__mode = mode
        self.__resource = resource


    @property
    def name(self):
        return self.__name

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self,mode):
        self.__mode = mode
        return self.__mode

    @property
    def resource(self):
        return self.__resource
