import strategies.contentItemDownloadStrategy as cids

import os
import logging

# setup logger for module
_log = logging.getLogger(__name__)


class Datasource_Item_Download_Strategy(cids.Content_Item_Download_Strategy):
    def download(self,ds,path,include_extract=False):
        download_path = ds.server.item.datasources.download(
                            ds.id,path,include_extract)
    
        return os.path.abspath(download_path)