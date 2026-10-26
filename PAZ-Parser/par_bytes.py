"""Bounds-checked little-endian reads shared by the PAR file parsers.

`par_mesh.py` (`.pam`, `.pcm`, `.pac`), `par_skeleton.py` (`.pab`) and
`par_animation.py` (`.paa`) read through these, so a short file raises a
ValueError that names the offset instead of a struct.error.
"""
from __future__ import annotations

import struct

PAR_MAGIC = b"PAR "
# Bytes 0x00 to 0x0F of every PAR file: the magic, the kind, the version and ten more.
PAR_HEADER_SIZE = 0x10
# Byte 4 of a PAR header: what the file holds.
KIND_PAB = 0x01
KIND_PAA = 0x02
KIND_PAC = 0x03
KIND_PAM = 0x06
KIND_PCM = 0x11


def check_par(data: bytes, kind: int, what: str) -> int:
    """The version byte of a PAR file of `kind`; ValueError when `data` is not one."""
    if data[:4] != PAR_MAGIC or len(data) < PAR_HEADER_SIZE:
        raise ValueError("no PAR magic")
    if data[4] != kind:
        raise ValueError(f"PAR kind 0x{data[4]:02x} is not {what}")
    return data[5]


def need(data: bytes, offset: int, size: int) -> None:
    if offset + size > len(data):
        raise ValueError(f"file ends at 0x{len(data):x}, needs 0x{offset + size:x}")


def u8(data: bytes, offset: int) -> int:
    need(data, offset, 1)
    return data[offset]


def u16(data: bytes, offset: int) -> int:
    need(data, offset, 2)
    return struct.unpack_from("<H", data, offset)[0]


def u32(data: bytes, offset: int) -> int:
    need(data, offset, 4)
    return struct.unpack_from("<I", data, offset)[0]


def i32(data: bytes, offset: int) -> int:
    need(data, offset, 4)
    return struct.unpack_from("<i", data, offset)[0]


def f32(data: bytes, offset: int) -> float:
    need(data, offset, 4)
    return struct.unpack_from("<f", data, offset)[0]


def cp949_name(raw: bytes) -> str:
    """Text up to the first NUL, decoded as the client writes names."""
    return raw.split(b"\0", 1)[0].decode("cp949", errors="replace")


def expect_end(data: bytes, offset: int) -> None:
    if offset != len(data):
        raise ValueError(f"layout ends at 0x{offset:x}, file at 0x{len(data):x}")
