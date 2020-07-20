
import logging


# setup logger for module
_log = logging.getLogger(__name__)


class Role_Item():
    
    __role_name = str()
    __name = str()
    __description = str()
    __permissions = list()

    def __init__(self,name,permissions,dscr=""):
        self.__name = name
        self.__description = dscr
        self.__permissions = permissions
        self.__load_item()


    @property
    def permissions(self):
        return self.__permissions

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,dscr):
        self.__description = dscr


    def __load_item(self):
        #load default settings here. 
        pass


    def add_permission(self,permission):
        self.__permissions.append(permission)

    
    def remove_permission(self,permission):
        pass


    def reset_permissions(self):
        pass


    # def apply_to(self,recipient):
    #     #this will likely need to apply to either a user or a group item
    #     pass
