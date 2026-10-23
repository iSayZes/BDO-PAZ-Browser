"""`eventguidess.bss`: the events of the Event Guide window, with their periods and rewards.

    u32 count | count x row
    row: str16 main_title_kr | str16 main_desc_kr | str16 sub_desc_kr
         | str16 period_desc_kr | str8 icon | str8 texture_bg
         | u64 start_time | u64 end_time | str8 web_keyword | str8 web_hash_id
         | str8 function | str16 function_desc_kr | u8 tag | u32 event_key
         | u32 reward_count | u32[reward_count] rewards

No PABR magic and no string table. `start_time` and `end_time` are UTC Unix
seconds; `rewards` are item keys. Layout 1 in
docs/file-formats/eventguidess_bss.md.
"""

from __future__ import annotations

import struct

from _common.counted_rows import read_counted_records
from _common.record_reader import RecordReader


FILE_NAME = "eventguidess.bss"
KEY_FIELD = "event_key"

_TIMES = struct.Struct("<QQ")
_TAIL = struct.Struct("<BII")
_REWARD_SIZE = 4


def _read_row(reader: RecordReader) -> dict:
    main_title_kr = reader.text(wide=True)
    main_desc_kr = reader.text(wide=True)
    sub_desc_kr = reader.text(wide=True)
    period_desc_kr = reader.text(wide=True)
    icon = reader.text(wide=False)
    texture_bg = reader.text(wide=False)
    start_time, end_time = reader.unpack(_TIMES)
    web_keyword = reader.text(wide=False)
    web_hash_id = reader.text(wide=False)
    function = reader.text(wide=False)
    function_desc_kr = reader.text(wide=True)
    tag, event_key, reward_count = reader.unpack(_TAIL)
    if reward_count * _REWARD_SIZE > reader.remaining():
        raise ValueError(f"{FILE_NAME} event {event_key} reward count {reward_count:,} runs past the file")
    rewards = list(reader.unpack(struct.Struct(f"<{reward_count}I")))
    return {
        KEY_FIELD: event_key,
        "main_title_kr": main_title_kr,
        "main_desc_kr": main_desc_kr,
        "sub_desc_kr": sub_desc_kr,
        "period_desc_kr": period_desc_kr,
        "icon": icon,
        "texture_bg": texture_bg,
        "start_time": start_time,
        "end_time": end_time,
        "web_keyword": web_keyword,
        "web_hash_id": web_hash_id,
        "function": function,
        "function_desc_kr": function_desc_kr,
        "tag": tag,
        "rewards": rewards,
    }


def parse_eventguidess_records(data: bytes) -> list[dict]:
    """Every event in file order. Raises ValueError when a row runs past the file or the rows end early."""
    return read_counted_records(data, _read_row, FILE_NAME)
