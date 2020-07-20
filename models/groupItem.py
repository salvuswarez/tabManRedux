
import models.tscItem as tscItem
import models.userItem as userItem

import logging
import tableauserverclient as tsc


# setup logger for module
_log = logging.getLogger(__name__)

class Group_Item(tscItem.TSC_Item):

    __users = list()


    def __init__(self,server,group):
        self.__server = server
        self.__item = group
        self.__id = group.id
        self.__name = group.name
        self.__users = None
        self.__load_item()


    @property
    def users(self):
        return self.__users

    
    def __load_item(self):
        self.__server.item.groups.populate_users(self)
        self.__users = [userItem.User_Item(
                            self.__server,user) 
                                for user in self.__item.users]


    def add_user(self,user):
        self.__server.item.groups.add_user(self,user)

