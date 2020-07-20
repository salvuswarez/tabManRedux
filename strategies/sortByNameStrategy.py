
import strategies.tscItemsSortStrategy as sorting

import logging


# setup logger for module
_log = logging.getLogger(__name__)


class Sort_By_Name_Strategy(sorting.TSCItems_Sort_Strategy):
    def sort(self,items_list):
        n = len(items_list)

        for i in range(n-1):
            for j in range(0,n-i-1):
                if items_list[j].name > items_list[j+1].name:
                    items_list[j], items_list[j+1] = items_list[j+1],items_list[j]

        return items_list
        