"""Sequential reader over the body of a PABR action chart (`.paac`).

Every count is a u64 or u32 before its items, every sized block a u64 size
before its bytes, and every string a u32 index into the PABR string table at
the end of the file (docs/file-formats/other/actionchart_paac.md). The body
ends with a u32 version `1` right before the string table.
"""

from __future__ import annotations

import struct

from _common.pabr_strings import check_pabr, read_string_table, string_table_start
from _common.record_reader import RecordReader

_U8 = struct.Struct("<B")
_U16 = struct.Struct("<H")
_U32 = struct.Struct("<I")
_I32 = struct.Struct("<i")
_U64 = struct.Struct("<Q")
_F32 = struct.Struct("<f")

FORMAT_VERSION = 1
_VERSION_SIZE = 4
# A sized block larger than this means the layout is wrong; the largest in client
# 1784 and 3483 files is an element's 0x158-byte parameter block.
_MAX_BLOCK = 0x10000


class ChartReader(RecordReader):
    """Reads the fields between the PABR header and the trailing version."""

    def __init__(self, data: bytes, file_name: str) -> None:
        check_pabr(data, file_name)
        body_end = string_table_start(data) - _VERSION_SIZE
        super().__init__(data, 4, body_end, file_name)
        self.strings = read_string_table(data)
        if self.u32() != FORMAT_VERSION:
            raise ValueError(f"{file_name} is not action chart version {FORMAT_VERSION}")
        (end_version,) = _U32.unpack_from(data, body_end)
        if end_version != FORMAT_VERSION:
            raise ValueError(f"{file_name} has version {end_version} before its string table")

    def u8(self) -> int:
        return self.unpack(_U8)[0]

    def u16(self) -> int:
        return self.unpack(_U16)[0]

    def u32(self) -> int:
        return self.unpack(_U32)[0]

    def i32(self) -> int:
        return self.unpack(_I32)[0]

    def u64(self) -> int:
        return self.unpack(_U64)[0]

    def f32(self) -> float:
        return self.unpack(_F32)[0]

    def raw(self, size: int) -> bytes:
        return self._take(size)

    def string(self) -> str:
        """The string a u32 table index names; an index past the table is empty, as in the client."""
        index = self.u32()
        return self.strings[index] if index < len(self.strings) else ""

    def block(self) -> bytes:
        """A u64 size, then that many bytes."""
        size = self.u64()
        if size > _MAX_BLOCK:
            raise ValueError(f"a {size:,}-byte block at 0x{self.pos - 8:X} is too large")
        return self._take(size)

    def count(self) -> int:
        """A u64 item count, checked against the bytes left."""
        value = self.u64()
        if value > self.remaining():
            raise ValueError(f"count {value:,} at 0x{self.pos - 8:X} exceeds the bytes left")
        return value

    def short_count(self) -> int:
        """A u32 item count, checked against the bytes left."""
        value = self.u32()
        if value > self.remaining():
            raise ValueError(f"count {value:,} at 0x{self.pos - 4:X} exceeds the bytes left")
        return value

    def u32_list(self) -> list[int]:
        """A u64 count, then that many u32."""
        count = self.count()
        return list(struct.unpack(f"<{count}I", self._take(4 * count)))
