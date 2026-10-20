"""Preview of `solareetcoptionstaticstatus.bss`.

The columns and labels are those of the PABR option tables handler; only the
reading differs, since this file has no PABR magic or string table. No field
is confirmed, so the table shows the raw value bytes; the five `unknown_*`
values stay on the record for search and export.
"""

from __future__ import annotations

from bdo_models import PazEntry

from ..pabr_values.handler import PabrValuesBssHandler
from .parser import SOLARE_ETC_OPTION, parse_solare_etc_option


class SolareEtcOptionBssHandler(PabrValuesBssHandler):
    def __init__(self) -> None:
        super().__init__(SOLARE_ETC_OPTION)

    def get_records(
        self,
        data: bytes,
        entry: PazEntry,
        companions: dict[str, bytes],
    ) -> list[dict]:
        return [parse_solare_etc_option(data)]
