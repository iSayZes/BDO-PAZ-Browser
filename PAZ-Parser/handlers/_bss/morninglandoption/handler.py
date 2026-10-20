"""Preview of `morninglandoption.bss`.

The columns and labels are those of the PABR option tables handler; only the
reading differs, since this file has no PABR magic or string table.
"""

from __future__ import annotations

from bdo_models import PazEntry

from ..pabr_values.handler import PabrValuesBssHandler
from .parser import MORNING_LAND_OPTION, parse_morning_land_option


class MorningLandOptionBssHandler(PabrValuesBssHandler):
    def __init__(self) -> None:
        super().__init__(MORNING_LAND_OPTION)

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [parse_morning_land_option(data)]
