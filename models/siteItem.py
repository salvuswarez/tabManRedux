
import models.tscItem as tscItem
import models.projectItem as projectItem
import models.groupItem as groupItem
import models.userItem as userItem

import logging
import tableauserverclient as tsc


# setup logger for module
_log = logging.getLogger(__name__)


class Site_Item(tscItem.TSC_Item):

    __content_url = str()
    __projects = list()
    __users = list()
    __groups = list()


    def __init__(self,server,site):
        """ Instantiates a new Site object and loads all its details.

            PARAMETERS
            -----
            server : SERVER_ITEM
                This is the instantiated server item.
            
            site : OBJECT
                The site object from rest api

        """
        
        self.__server = server
        self.__item = site
        self.__id = site.id
        self.__content_url = site.content_url
        self.__load_item()



    def __load_item(self):
        #this will load the inherited properties and the lists
        #first switch sites if needed
        switch_flg = False
        if self.__server.current_site.content_url != self.__content_url:
            self.__server.switch_current_site(self)
            switch_flg = True

        all_proj, page_item1 = self.__server.item.projects.get()
        all_groups, page_item2 = self.__server.item.groups.get()
        all_users, page_item3 = self.__server.item.users.get() 

        self.__projects = [projectItem.Project_Item(
                            self.__server,proj) for proj in all_proj]

        self.__groups = [groupItem.Group_Item(
                            self.__server,group) for group in all_groups]

        self.__users = [userItem.User_Item(
                            self.__server,user) for user in all_users]

        #now switch back
        if switch_flg is True:
            self.__server.switch_current_site(self.__server.prev_site)



    @property
    def content_url(self):
        return self.__content_url

    @property
    def projects(self):
        return self.__projects

    @property
    def users(self):
        return self.__users

    @property
    def groups(self):
        return self.__groups

    @property
    def is_current_site(self):
        if self.__server.current_site.id == self.id:
            return True
        else:
            return False



    def set_as_current_site(self):
        if not self.is_current_site:
            self.__server.switch_current_site(self)



    def add_user(self,username,site_role=''):
        switched_sites = False
        if site_role =='':
            site_role = 'ExplorerCanPublish'

        if self.is_current_site is False:
            self.__server.switch_current_site(self)
            switched_sites = True

        user = tsc.UserItem(username,site_role)
        user = self.__server.item.users.add(user)

        if switched_sites is True:
            self.__server.switch_current_site(self.__server.previous_site)

        return user
    

    
    def create_project(self,project_name,parent_id=None): 
        """ Create a new project on the current site or a specified site.

            PARAMETERS
            -----
            project_name : STRING
                Name of the new project.

            parent_id : STRING *optional
                ID of the Parent project if there is one

            RETURNS
            -----
            PROJECT_ITEM

        """

        switched_sites = False

        if self.is_current_site is False:
            switched_sites = True
            self.set_as_current_site()

        new_project = tsc.ProjectItem(
                            name=project_name,parent_id=parent_id)

        new_project = self.__server.item.projects.create(new_project)
        new_project = projectItem.Project_Item(self.__server,new_project)

        if switched_sites is True:
            self.__server.switch_current_site(self.__server.previous_site)


        return new_project



    def find_project_by_id(self,project_id):
        """ Find a project by its ID.

            PARAMETERS
            -----
            project_id : STRING
                The ID of the project to find.

            RETURNS
            -----
            PROJECT_ITEM

        """
        
        found_project = None

        for p in self.__projects:
            if p.id == project_id:
                found_project = p
        
        return found_project
        



    def find_project_by_name(self,project_name):
        """ Find a project by its name.

            PARAMETERS
            -----
            project_name : STRING
                The name of the project you are searching for.

            RETURNS 
            -----
            PROJECT_ITEM

        """

        found_project = None

        for p in self.__projects:
            if p.name == project_name:
                found_project = p

        return found_project



    def find_user_by_id(self,user_id):
        """ Find a user by their ID.

            PARAMETERS
            -----
            user_id : STRING
                The user's id to search by.

            RETURNS
            -----
            USER_ITEM

        """
        
        found_user = None

        for u in self.__users:
            if u.id == user_id:
                found_user = u

        return found_user



    def find_user_by_username(self,username):
        """ Find a user by their username. 

            PARAMETERS
            -----
            username : STRING
                The active directory / tableau username for the user.

            RETURNS
            -----
            USER_ITEM

        """

        found_user = None

        for u in self.__users:
            if u.name == username:
                found_user = u

        return found_user



    def create_group(self,group_name):
        """ Create a new group for the given server and site.

            PARAMETERS
            -----
            group_name : STRING
                The name of the new group.

            RETURNS
            -----
            GROUP_ITEM

        """
        
        sites_switched = False

        if self.id != self.__server.current_site.id:
            self.__server.switch_current_site(self)
            sites_switched = True

        new_group = tsc.GroupItem(group_name)
        new_group = self.__server.item.groups.create(new_group)
        new_group = groupItem.Group_Item(self.__server,new_group)

        self.__groups.append(new_group)

        if sites_switched is True:
            self.__server.switch_current_site(self.__server.previous_site)

        return  new_group



    def find_group_by_id(self,group_id):
        """ Find a group by its ID.

            PARAMETERS
            -----
            group_id : STRING
                ID of the group to search for.

            RETURNS
            -----
            GROUP_ITEM

        """

        found_group = None

        for g in self.__groups:
            if g.id == group_id:
                found_group = g

        return found_group



    def find_group_by_name(self,group_name):
        """ Find a group by its name.

            PARAMETERS
            -----
            server : SERVER_ITEM
                Logged in server to search within.
            
            group_name : STRING
                The group's name to search for.

            RETURNS
            -----
            GROUP_ITEM

        """
        
        found_group = None

        for g in self.__groups:
            if g.name == group_name:
                found_group = g

        return found_group