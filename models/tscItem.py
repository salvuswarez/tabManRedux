
import models.tscBaseItem as tscBaseItem

import logging


# setup logger for module
_log = logging.getLogger(__name__)


class TSC_Item(tscBaseItem.TSC_Base_Item):
    __server = tscBaseItem.TSC_Base_Item()
    __item = object()
    __name = str()
    __id = str()
    
    


    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id
        
    @property
    def item(self):
        return self.__item

    @property
    def server(self):
        return self.__server
