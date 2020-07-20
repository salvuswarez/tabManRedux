import strategies.contentItemDownloadStrategy as cids

import os
import logging

# setup logger for module
_log = logging.getLogger(__name__)


class Workbook_Item_Download_Strategy(cids.Content_Item_Download_Strategy):
    def download(self,wbk,path,include_extract=False):
        download_path = wbk.server.item.workbooks.download(
                            wbk.id,path,include_extract)
        
        return os.path.abspath(download_path)