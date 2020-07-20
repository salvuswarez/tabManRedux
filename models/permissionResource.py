
import logging 

# setup logger for module
_log = logging.getLogger(__name__)


class Permission_Resource():

    PROJECTS = 'projects'
    WORKBOOKS = 'workbooks'
    DATASOURCES = 'datasources'
    DATAROLES = 'dataroles'