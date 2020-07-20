

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

    #need to determine if it uses same owner or uses current admin
    #possible use of a preference / setting of where to download temp files to

    for item in content_items:
        item.download(tempfile.mkdtemp())

        #might need a check here to make sure there is something to publish
        if item.download_path is not None:
            #need to figure out how and where to change the location of an item. 
            item.location = target_location
            item.publish()

        #need to check to see how it should update the owner for the ontent
        #if attempt to keep original owner:
        #   user = target_location.site.add_user(item.owner.name)
        