
import strategies.contentItemPublishStrategy as cips

import logging
import tableauserverclient as tsc


# setup logger for module
_log = logging.getLogger(__name__)


class Workbook_Item_Publish_Strategy(cips.Content_Item_Publish_Strategy):
    def publish(self,server,wbk_name,project_id,fpath):
        
        newWbk = tsc.WorkbookItem(name=wbk_name,project_id=project_id)

        newWbk = server.item.workbooks.publish(newWbk,
                                            fpath,
                                            mode=tsc.Server.PublishMode.Overwrite)
        # TODO: needs to return some sort of message or result

