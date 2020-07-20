


class Workspace_Structure():
    #contains a list of "containers" that hold a project and the permissions for that project
    __containers = list()
    __name = str()


    def __init__(self,name):
        self.__name = name


    @property
    def containers(self):
        return self.__containers

    @containers.setter
    def containers(self,containers):
        self.__containers = containers

    @property
    def name(self):
        return self.__name

    
    def add_container(self,container):
        self.__containers.append(container)

    