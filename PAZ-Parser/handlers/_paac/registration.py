from __future__ import annotations

from bdo_preview import register_handler

from .actionchart.handler import ActionChartHandler
from .actionchartheader.handler import ActionChartHeaderHandler
from .actionchartheader.parser import FILE_NAME as HEADER_FILE_NAME
from .parser import SHARED_TABLES_NAME
from .sharedtables.handler import SharedTablesHandler


def register_paac_handlers() -> None:
    # Every chart shares one layout per client; the shared tables file has its own.
    register_handler(".paac", ActionChartHandler())
    register_handler(SHARED_TABLES_NAME, SharedTablesHandler())
    register_handler(HEADER_FILE_NAME, ActionChartHeaderHandler())
