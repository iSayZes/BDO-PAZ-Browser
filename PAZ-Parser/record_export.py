"""Parsed records as CSV, shared by the GUI export and `browser.py --records --csv`."""
from __future__ import annotations

import csv
import io
from pathlib import PurePosixPath

from record_fields import data_fields


def records_to_csv(records: list[dict]) -> str:
    """CSV text with one column per key of the first record, in file order.

    Display-only fields (`_` keys) are left out. Empty when there are no
    records. Lines end in CRLF, the csv module default.
    """
    buf = io.StringIO()
    if records:
        writer = csv.DictWriter(buf, fieldnames=data_fields(records[0]), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
    return buf.getvalue()


def csv_export_name(file_name: str, client_version: int | None, handler_version: str | None) -> str:
    """The GUI export's default file name: `buffsimply_3464_2026.10.12.csv`.

    The client and handler versions say which game data and which parser the
    rows came from; a version that is unknown is left out of the name.
    """
    parts = [PurePosixPath(file_name).stem, client_version, handler_version]
    return "_".join(str(part) for part in parts if part is not None) + ".csv"
