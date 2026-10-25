"""The client's hash of a string key: Bob Jenkins' lookup3 `hashlittle`.

It runs over the key's UTF-16LE bytes with seed `0xC5EDE`. On client 3464 it
reproduces every `key_hash` and `sheet_hash` of `stringtable.bss` and the LOC
type 59 `str_id1` of every TextBind name (docs/file-formats/bss/stringtable_bss.md).
Action and file names are hashed over their ASCII bytes with the same seed
(`ascii_key_hash`): `manufacture.bss` actions, `collectresourcename.dbss`
file names and the `servantbuff.dbss` action names.
"""

from __future__ import annotations

from functools import lru_cache

_MASK = 0xFFFFFFFF
_GOLDEN = 0xDEADBEEF
_BLOCK = 12
KEY_HASH_SEED = 0xC5EDE


def _rot(value: int, bits: int) -> int:
    return ((value << bits) | (value >> (32 - bits))) & _MASK


def _words(block: bytes) -> tuple[int, int, int]:
    return (
        int.from_bytes(block[0:4], "little"),
        int.from_bytes(block[4:8], "little"),
        int.from_bytes(block[8:12], "little"),
    )


def _mix(a: int, b: int, c: int) -> tuple[int, int, int]:
    a = ((a - c) & _MASK) ^ _rot(c, 4)
    c = (c + b) & _MASK
    b = ((b - a) & _MASK) ^ _rot(a, 6)
    a = (a + c) & _MASK
    c = ((c - b) & _MASK) ^ _rot(b, 8)
    b = (b + a) & _MASK
    a = ((a - c) & _MASK) ^ _rot(c, 16)
    c = (c + b) & _MASK
    b = ((b - a) & _MASK) ^ _rot(a, 19)
    a = (a + c) & _MASK
    c = ((c - b) & _MASK) ^ _rot(b, 4)
    b = (b + a) & _MASK
    return a, b, c


def _final(a: int, b: int, c: int) -> int:
    c = ((c ^ b) - _rot(b, 14)) & _MASK
    a = ((a ^ c) - _rot(c, 11)) & _MASK
    b = ((b ^ a) - _rot(a, 25)) & _MASK
    c = ((c ^ b) - _rot(b, 16)) & _MASK
    a = ((a ^ c) - _rot(c, 4)) & _MASK
    b = ((b ^ a) - _rot(a, 14)) & _MASK
    return ((c ^ b) - _rot(b, 24)) & _MASK


def hashlittle(data: bytes, seed: int) -> int:
    """lookup3 `hashlittle()` of `data`, as the little-endian reference reads it."""
    a = b = c = (_GOLDEN + len(data) + seed) & _MASK
    pos = 0
    # Every full block but the last goes through mix(); the last, full or
    # short, through final(). Empty data returns the start value.
    while len(data) - pos > _BLOCK:
        x, y, z = _words(data[pos : pos + _BLOCK])
        a, b, c = _mix((a + x) & _MASK, (b + y) & _MASK, (c + z) & _MASK)
        pos += _BLOCK
    if pos == len(data):
        return c
    x, y, z = _words(data[pos:].ljust(_BLOCK, b"\0"))
    return _final((a + x) & _MASK, (b + y) & _MASK, (c + z) & _MASK)


@lru_cache(maxsize=4096)
def key_hash(key: str) -> int:
    """The hash the client stores for a string key, such as a TextBind name."""
    return hashlittle(key.encode("utf-16-le"), KEY_HASH_SEED)


def ascii_key_hash(name: str) -> int:
    """The hash the client stores for an ASCII name, such as an action name."""
    return hashlittle(name.encode("ascii"), KEY_HASH_SEED)
