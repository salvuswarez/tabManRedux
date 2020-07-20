
import models.tscItem as tscItem
import models.workbookItem as wbk
import models.datasourceItem as dts

import logging
#import tableauserverclient as tsc


# setup logger for module
_log = logging.getLogger(__name__)


class Project_Item(tscItem.TSC_Item):

    __workbooks = list()
    __datasources = list()
    __parent = tscItem.TSC_Item()
    __children = list()
    __has_children = False
    __has_parent = False


    def __init__(self,server,project):
        self.__server = server
        self.__item = project
        self.__id = project.id
        self.__name = project.name
        self.__parent = None
        self.__load_item()


    @property
    def workbooks(self):
        return self.__workbooks

    @property
    def datasources(self):
        return self.__datasources

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children

    @property
    def has_children(self):
        return self.__has_children

    @property
    def has_parent(self):
        return self.__has_parent

    
    def __load_item(self):
        #possibly load the lists
        self.__load_content()
        self.__check_for_relatives()
        

    def __check_for_relatives(self):
        plist , pagination_item = self.__server.item.projects.get()

        # loop through all projects for server and get the parent
        # and get the children all in one loop
        for p in plist:
            if self.__item.parent_id is not None and p.id == self.__item.parent_id:
                self.__has_parent = True
                self.__parent = Project_Item(self.__server,p)
            elif p.parent_id == self.id:
                self.__children.append(Project_Item(self.__server,p))

        if len(self.children)>0:
            self.__has_children = True        
        

    def __load_content(self):
        all_wbs, pagination_item = self.__server.item.workbooks.get()   
        all_dss, pagination_item2 = self.__server.item.datasources.get()

        self.__workbooks = [wbk.Workbook_Item(self.__server,wb) for wb in all_wbs 
                                if wb.project_id == self.id]  
        self.__datasources = [ds for ds in all_dss
                                if ds.project_id == self.id]


    def add_content_item(self,content_item):
        #this essentially "moves" the provided workbook to this project
        content_item.update_project(self.id)

    
    