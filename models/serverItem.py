
import models.tscBaseItem as tscBaseItem
import models.tscItem as tscItem
import models.siteItem as siteItem
import namespaces

import requests
import xml.etree.ElementTree as ET
import tableauserverclient as tsc
import logging


# setup logger for module
_log = logging.getLogger(__name__)


class Server_Item(tscBaseItem.TSC_Base_Item):

    __address = str()
    __sites = list()
    __is_logged_in = False
    __auth = object()
    __current_site = tscItem.TSC_Item()
    __prev_site = tscItem.TSC_Item()


    def __init__(self,address,name=''):
        self.__address = address
        self.__name = name
        self.__item = tsc.Server(self.address)


    @property
    def address(self):
        return self.__address

    @property
    def sites(self):
        return self.__sites

    @property
    def current_site(self):
        self.__current_site = self.__item.sites.get_by_id(
                                                    self.__item.site_id)
        return siteItem.Site_Item(self,self.__current_site)

    @property
    def previous_site(self):
        return self.__prev_site

    @property
    def auth(self):
        return self.__auth

    @property
    def is_logged_in(self):
        return self.__is_logged_in
    

    def __load_item(self):
        # get all the sites 
        all_sites, page_item = self.__item.sites.get()

        # pass to the property
        self.__sites = [siteItem.Site_Item(self,s) 
                            for s in all_sites]
        

    def sign_in(self,username,pw):
        """ Sign into Tableau Server with credentials

            PARAMETERS
            -----
            username : STRING
                The username you want to sign in with
            
            pw : STRING
                The password for the given username

            RETURNS
            -----
            SERVER_ITEM

        """
        self.__auth = tsc.TableauAuth(username,pw)
        self.__item.auth.sign_in(self.__auth)
        self.__load_item()
 

    def sign_out(self):
        """ Sign out of the server.

        """
        self.__item.auth.sign_out()



    def find_site_by_id(self,site_id): 
        """ Find a site_item object by it's ID

            PARAMETERS
            -----
            site_id : STRING
                The actual ID of the site, not the content url.

            RETURNS
            -----
            SITE_ITEM

        """

        found_site = None

        for s in self.__sites:
            if s.id == site_id:
                found_site = s

        return found_site
    


    def find_site_by_content_url(self,content_url): 
        """ Find a site_item object by its content url string

            PARAMETERS
            -----
            content_url : STRING
                The content url string of the site you are searching for.

            RETURNS
            -----
            SITE_ITEM

        """

        found_site = None
        for s in self.__sites:
            if s.content_url == content_url:
                found_site = s

        return found_site



    def switch_current_site(self,to_site):
        """ Switch to the given site from the current site. This will 
            reload all item lists

            PARAMETERS
            -----
            to_site : SITE_ITEM
                This should be a site_item object that you want to 
                switch to.
                
        """
        #TODO: need to break this function down into several smaller ones
        #####################################################################
        if self.current_site.content_url != to_site.content_url:
            self.__prev_site = self.current_site

            # setup url to post
            url = str(self.address) + '/api/{0}/auth/switchSite'.format(
                self.__item.version)
            xml_request = ET.Element('tsRequest')
            ET.SubElement(xml_request,'site',contentUrl=to_site)
            xml_request = ET.tostring(xml_request)

            _log.debug('Switching to Site | {0}'.format(to_site))
            # create full request body and submit request
            server_request = requests.post(url, data=xml_request, 
                                        headers={'x-tableau-auth': 
                                                    self.__item.auth_token},verify=False)

            _log.debug('Switch Sites Response: \n{0}'.format(server_request))
            #serverResponse.check_status(server_request, 200)

            # clean up response from server
            server_request = server_request.text.encode(
                'ascii', errors="backslashreplace").decode('utf-8')
            server_request = ET.fromstring(server_request)

            # get the authToken tags to for the new site
            authToken = server_request.findall(
                './/t:credentials',namespaces=namespaces.namespace)[0].attrib.get('token')

            # grab the dest site id
            siteID = server_request.findall('.//t:site',namespaces=namespaces.namespace)

            # set the new auth object back with the given server obj
            self.__item._set_auth(siteID[0].attrib.get('id'),self.__item.user_id,authToken)
    