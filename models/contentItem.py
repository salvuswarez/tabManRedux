
import models.tscItem as tscItem
import models.contentItemLocation as contentItemLocation
import strategies.contentItemDownloadStrategy as cids
import strategies.contentItemPublishStrategy as cips

import logging

# setup logger for module
_log = logging.getLogger(__name__)


class Content_Item(tscItem.TSC_Item):

    __download_strategy = cids.Content_Item_Download_Strategy()
    __publish_strategy = cips.Content_Item_Publish_Strategy()
    __location = object()
    __download_path = str()
    __owner = tscItem.TSC_Item()

    @property
    def owner(self):
        return self.__owner

    
    @property
    def location(self):
        return self.__location


    @property
    def download_path(self):
        return self.__download_path

    
    def download(self,path):
        self.__download_path = path
        self.__download_strategy.download(self,path)


    def publish(self,project_id=None):
        if project_id is None:
            project_id = self.item.project_id
        self.__publish_strategy.publish(self.server,self.name,project_id,self.download_path)


    def update_owner(self,user_id):
        pass


    def update_project(self,project_id):
        pass
    