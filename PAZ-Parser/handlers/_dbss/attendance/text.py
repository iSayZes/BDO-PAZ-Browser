"""Attendance event texts from LOC type 49.

Keyed `(attendance_key, 0, service code, field)`: field 0 is the title, 1 the
period text, 2 the claim deadline text. The service code in `str_id3` is `12`
on every event of the en file; keys 1 to 25 also have rows under code `0`
(key 1 under `26`). The code most events use wins, else the lowest one, as
for the Pearl Shop texts of LOC type 50. See Notes in
docs/file-formats/dbss/attendance_dbss.md.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from _common.loc import loc_type_entries

LOC_ATTENDANCE = 49
_FIELD_TITLE = 0
_FIELD_PERIOD = 1
_FIELD_EXPIRED = 2


@dataclass(frozen=True)
class AttendanceText:
    """An event's tagged title, period and claim deadline texts; "" where LOC has no row."""

    title: str
    period: str
    expired: str


def attendance_texts() -> dict[int, AttendanceText]:
    """Attendance key -> its LOC texts, or empty when LOC is not loaded."""
    entries = loc_type_entries(LOC_ATTENDANCE)
    codes_by_key: dict[int, set[int]] = {}
    for _, key, _, code, _ in entries:
        codes_by_key.setdefault(key, set()).add(code)
    if not codes_by_key:
        return {}

    code_counts = Counter(code for codes in codes_by_key.values() for code in codes)
    main_code = code_counts.most_common(1)[0][0]
    texts: dict[int, AttendanceText] = {}
    for key, codes in codes_by_key.items():
        code = main_code if main_code in codes else min(codes)
        title, period, expired = (
            entries.get((LOC_ATTENDANCE, key, 0, code, field), "").strip()
            for field in (_FIELD_TITLE, _FIELD_PERIOD, _FIELD_EXPIRED)
        )
        texts[key] = AttendanceText(title=title, period=period, expired=expired)
    return texts
