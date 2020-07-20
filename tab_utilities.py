

import models.serverItem as server
import models.siteItem as site
import models.projectItem as project
import models.userItem as user
import models.groupItem as group
import models.datasourceItem as datasource
import models.workbookItem as workbook
import models.permissionItem as permission
import models.roleItem as role
import models.permissionMode as permissionMode
import models.permissionResource as permissionResource

import tableauserverclient as tsc

import logging
import tempfile as tempfile

# setup logger for module
_log = logging.getLogger(__name__)


#provides added server funtionality
#this should hold functions like migrate content, ones that dialogs 
# are built for as well as other easy tools. 



def new_server_instance(server_url,name=''):
    """ Create a new server instance

        PARAMETERS
        -----
        server_url : STRING
            The server url address to log in to.

        name : STRING
            An alias string you can provide for quick reference.

        RETURNS
        -----
        SERVER_ITEM

    """
    
    s = server.Server_Item(server_url,name)
    
    return s



def migrate_content(server,content_items,target_location):
    #should take list of content items and download each one, then 
    #publish it to the target location
    #this function should always be started from the source site

    #TODO: need to determine if it uses same owner or uses current admin
    #TODO: possible use of a preference / setting of where to download temp files to
    site_changed = False
    batch_limit = 4
    i = 0
    published = []
    downloaded = []
    for item in content_items:
        #might need to  be a while loop so i can reset the i and not miss the current item
        if i < batch_limit:
            item.download(tempfile.mkdtemp())
            downloaded.append(item)
            i +=1
        else:
            #publish all files in downloaded list, reset i , reset list
            #need to switch to target site
            if server.current_site.content_url != target_location.site.content_url:
                server.switch_current_site(target_location.site)
                site_changed = True

            for d_item in downloaded:
                d_item.publish(target_location.project.id)
            
            i = 0
            downloaded = []
            if site_changed is True:
                server.switch_current_site(server.previous_site)
        

        #need to check to see how it should update the owner for the content
        #if attempt to keep original owner:
        #   user = target_location.site.add_user(item.owner.name)
        