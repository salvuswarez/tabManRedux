

import models.tscItem as tscItem
import models.projectItem as projectItem
#import models.permissionItem as permissionItem



class Workspace_Container():

    __project = tscItem.TSC_Item()
    __permissions = list()


    def __init__(self,project,permissions):
        self.__project = project
        self.__permissions = permissions


    @property
    def project(self):
        return self.__project

    @property
    def permissions(self):
        return self.__permissions

    
    def add_permission(self,permission_item):
        self.__permissions.append(permission_item)
