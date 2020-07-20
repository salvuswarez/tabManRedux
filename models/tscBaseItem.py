

class TSC_Base_Item():

    __name = str()
    __id = str()
    __item = object()


    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def item(self):
        return self.__item

    