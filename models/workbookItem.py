
import models.tscItem as tscItem
import models.userItem as userItem
import models.contentItemLocation as contentItemLocation
import strategies.workbookItemPublishStrategy as pws
import strategies.workbookItemDownloadStrategy as wids

import logging

# setup logger for module
_log = logging.getLogger(__name__)


class Workbook_Item(tscItem.TSC_Item):

    def __init__(self,server,workbook):
        self.__item = workbook
        self.__server = server
        self.__load_item()

    
    def __load_item(self):
        self.__set_location()
        self.__set_owner()
        self.__publish_strategy = pws.Workbook_Item_Publish_Strategy()
        self.__download_strategy = wids.Workbook_Item_Download_Strategy()



    def __set_location(self):
        site = self.__server.current_site
        project = None
        
        for p in site.projects:
            if p.id == self.__item.project_id:
                project = p
        
        self.__location = contentItemLocation.Content_Item_Location(site,project)


    def __set_owner(self):
        user = tscItem.TSC_Item()

        for u in self.__server.current_site.users:
            if u.id == self.__item.owner_id:
                user = userItem.User_Item(self.__server,u)

        self.__owner = user


    def update_owner(self,user_id):
        self.__item.owner_id = user_id
        self.__server.item.workbooks.update(self.__item)


    def update_project(self,project_id):
        self.__item.project_id = project_id
        self.__server.item.workbooks.update(self.__item)