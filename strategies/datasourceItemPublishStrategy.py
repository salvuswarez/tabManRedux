
import tableauserverclient as tsc
import strategies.contentItemPublishStrategy as cips

import logging



# setup logger for module
_log = logging.getLogger(__name__)


class Datasource_Item_Publish_Strategy(cips.Content_Item_Publish_Strategy):
    def publish(self,server,ds_name,project_id,fpath):

        newDs = tsc.DatasourceItem(name=ds_name,project_id=project_id)

        newDs = server.item.datasources.publish(newDs,
                                            fpath,
                                            mode=tsc.Server.PublishMode.Overwrite)
    # TODO: needs to return some sort of message or result