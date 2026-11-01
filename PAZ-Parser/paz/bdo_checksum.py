"""The Pearl Abyss checksum of `pad00000.meta` and the PAZ headers (docs/file-formats/other/pad00000_meta.md, Checksum).

Bob Jenkins' lookup3 `hashlittle` with its own start value and final mix. A
row's path hash is the checksum of the file's path; an archive's checksum is
the checksum of the archive file from byte 4 on.
"""

from __future__ import annotations

import struct

_MASK = 0xFFFFFFFF
_START = 0x2145E233
_BLOCK = struct.Struct("<III")


def _rol(x: int, k: int) -> int:
    return ((x << k) | (x >> (32 - k))) & _MASK


def _ror(x: int, k: int) -> int:
    return ((x >> k) | (x << (32 - k))) & _MASK


def pa_checksum(data: bytes | bytearray | memoryview) -> int:
    """The checksum of `data`; 0 for empty input."""
    length = len(data)
    if length == 0:
        return 0
    a = b = c = (length - _START) & _MASK
    # Every 12-byte block but the last goes through lookup3's mix; the last
    # 1 to 12 bytes are the tail.
    body = (length - 1) // 12 * 12
    for x, y, z in _BLOCK.iter_unpack(memoryview(data)[:body]):
        a = (a + x) & _MASK
        b = (b + y) & _MASK
        c = (c + z) & _MASK
        a = ((a - c) & _MASK) ^ _rol(c, 4)
        c = (c + b) & _MASK
        b = ((b - a) & _MASK) ^ _rol(a, 6)
        a = (a + c) & _MASK
        c = ((c - b) & _MASK) ^ _rol(b, 8)
        b = (b + a) & _MASK
        a = ((a - c) & _MASK) ^ _rol(c, 16)
        c = (c + b) & _MASK
        b = ((b - a) & _MASK) ^ _rol(a, 19)
        a = (a + c) & _MASK
        c = ((c - b) & _MASK) ^ _rol(b, 4)
        b = (b + a) & _MASK
    x, y, z = _BLOCK.unpack(bytes(data[body:]).ljust(12, b"\x00"))
    a = (a + x) & _MASK
    b = (b + y) & _MASK
    c = (c + z) & _MASK
    return _final(a, b, c)


def _final(a: int, b: int, c: int) -> int:
    """Pearl Abyss's final mix; it differs from lookup3's `final`."""
    p = ((b ^ c) - _rol(b, 14)) & _MASK
    q = ((a ^ p) - _rol(p, 11)) & _MASK
    r = ((q ^ b) - _ror(q, 7)) & _MASK
    s = ((r ^ p) - _rol(r, 16)) & _MASK
    t = ((q ^ s) - _rol(s, 4)) & _MASK
    u = ((t ^ r) - _rol(t, 14)) & _MASK
    return ((u ^ s) - _ror(u, 8)) & _MASK
