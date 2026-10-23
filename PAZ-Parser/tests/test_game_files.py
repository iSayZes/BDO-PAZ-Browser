"""Which copy the doc check reads when several PAZ paths share a file name."""
from __future__ import annotations

from bdo_models import PazEntry
from cli.game_files import base_copies


def _entry(path: str) -> PazEntry:
    return PazEntry("pad00001.paz", path, 0, 0, 0, 0, 0)


def test_the_base_copy_wins_over_a_language_folder_copy() -> None:
    base = _entry("gamecommondata/binary/regioninfo_linkandcheckvalid2.bss")
    language = _entry("gamecommondata/binary/en/regioninfo_linkandcheckvalid2.bss")

    assert base_copies([language, base]) == [base]


def test_copies_at_the_same_depth_stay_ambiguous() -> None:
    first = _entry("mapdata_real/spawnplacementfieldgrid/1/fileinfo.bss")
    second = _entry("mapdata_real/spawnplacementfieldgrid/2/fileinfo.bss")

    assert base_copies([first, second]) == [first, second]
