import models.tscItem as tscItem


class Content_Item_Location():
    __site = tscItem.TSC_Item()
    __project = tscItem.TSC_Item()

    def __init__(self,site,project):
        self.__site = site
        self.__project = project

    
    @property
    def site(self):
        return self.__site

    @property
    def project(self):
        return self.__project

        