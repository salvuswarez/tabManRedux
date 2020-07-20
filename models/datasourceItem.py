
import models.tscItem as tscItem
import models.projectItem as projectItem
import models.contentItemLocation as contentItemLocation
import strategies.datasourceItemPublishStrategy as pds
import strategies.datasourceItemDownloadStrategy as dids

import logging

# setup logger for module
_log = logging.getLogger(__name__)


class Datasource_Item(tscItem.TSC_Item):

    def __init__(self,server,datasource):
        self.__server = server
        self.__item = datasource
        self.__name = datasource.name
        self.__id = datasource.id    
        self.__load_item()

    
    def __load_item(self):
        self.__set_location()
        self.__publish_strategy = pds.Datasource_Item_Publish_Strategy()
        self.__download_strategy = dids.Datasource_Item_Download_Strategy()
        


    def __set_location(self):
        site = self.__server.current_site
        project = None
        
        for p in site.projects:
            if p.id == self.__item.project_id:
                project = projectItem.Project_Item(self.server,p)
        
        self.__location = contentItemLocation.Content_Item_Location(site,project)


    
    def update_owner(self,user_id):
        self.__item.owner_id = user_id
        self.__server.item.datasources.update(self.__item)



    def update_project(self,project_id):
        self.__item.project_id = project_id
        self.__server.item.datasources.update(self.__item)