"""`yachtclasstypetextureinfo.dbss`: the Yar! profile icon of each class type.

    u32 count | count x (u32 class_type | u32 class_type_dup | str8 texture_id)

`yachtclasstypetextureinfooffset.dbss` points at `class_type_dup`. Layout in
docs/file-formats/dbss/yachtclasstypetextureinfo_dbss.md.
"""

from __future__ import annotations

from _common.record_reader import RecordReader
from _dbss.yacht_common.keyed_rows import parse_keyed_rows


FILE_NAME = "yachtclasstypetextureinfo.dbss"
OFFSET_FILE = "yachtclasstypetextureinfooffset.dbss"
KEY_FIELD = "class_type"


def _read_texture(reader: RecordReader) -> dict:
    return {"texture_id": reader.text(wide=False)}


def parse_yachtclasstypetextureinfo_records(data: bytes) -> list[dict]:
    """Every class type in file order. Raises ValueError when a row runs past the file or the rows do not fill it."""
    return parse_keyed_rows(data, FILE_NAME, KEY_FIELD, _read_texture)
