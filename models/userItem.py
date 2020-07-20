
import models.tscItem as tscItem
import models.groupItem as groupItem

import logging
import tableauserverclient as tsc


# setup logger for module
_log = logging.getLogger(__name__)


class User_Item(tscItem.TSC_Item):
    
    __assigned_groups = list()
    __site_role = str()


    def __init__(self,server,user):
        self.__item = user
        self.__server = server
        self.__id = user.id
        self.__name = user.name
        self.__load_item()


    @property
    def assigned_groups(self):
        return self.__assigned_groups

    @property
    def email(self):
        return self.__item.email

    @property
    def site_role(self):
        return self.__item.site_role

    @site_role.setter
    def site_role(self,role):
        self.__site_role = role

        return self.__site_role



    def __load_item(self):
        #find groups user belongs to and pass to __assigned_groups
        #load any other properties here
        self.__load_assigned_groups()
    
    
    def __load_assigned_groups(self):
        groups, page_item = self.__server.item.groups.get()

        for g in groups:
            for u in g.users:
                if u.id == self.id:
                    self.__assigned_groups.append(
                            groupItem.Group_Item(self.__server,g))

        


        