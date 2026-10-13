"""A BDO stream encoder for the decompress tests, so they need no client.

Greedy, one candidate per 3-byte prefix: the point is streams that use every
back-reference encoding, not a small output. Layout, as `unpack_python` reads
it: a 32-bit group header before every 31 blocks (bit 0 first, 0 = literal
byte, 1 = back-reference, bit 31 set as the end marker), each block's bytes
inline after it.
"""

from __future__ import annotations

import random
import struct

_BLOCKS_PER_GROUP = 31
_GROUP_END_MARKER = 0x80000000
# The decoder copies the last 11 bytes one at a time, and a back-reference
# must end 4 bytes before the output does.
_TAIL_BYTES = 11
_MIN_REPEAT = 3
# The widest repeat field, 17 bits in the 3- and 4-byte encodings.
_MAX_REPEAT = (1 << 17) - 1
_MIN_LENGTH = 3
# The decoder reads 4 bytes at every block, so the stream ends with spare bytes.
_END_PADDING = bytes(4)


def encode(source: bytes) -> bytes:
    """`source` as a long-mode compressed payload, header included."""
    blocks = _blocks(source)
    body = bytearray()
    for start in range(0, len(blocks), _BLOCKS_PER_GROUP):
        group = blocks[start : start + _BLOCKS_PER_GROUP]
        header = _GROUP_END_MARKER
        for bit, (is_reference, _) in enumerate(group):
            header |= int(is_reference) << bit
        body += struct.pack("<I", header)
        for _, block in group:
            body += block
    if not blocks:
        body += struct.pack("<I", _GROUP_END_MARKER)
    body += _END_PADDING
    header_size = 9
    return struct.pack("<BII", 0x03, header_size + len(body), len(source)) + body


def _blocks(source: bytes) -> list[tuple[bool, bytes]]:
    blocks: list[tuple[bool, bytes]] = []
    last_seen: dict[bytes, int] = {}
    reference_end = len(source) - _TAIL_BYTES
    position = 0
    while position < len(source):
        prefix = source[position : position + _MIN_LENGTH]
        candidate = last_seen.get(prefix)
        last_seen[prefix] = position
        if (
            candidate is not None
            and _MIN_REPEAT <= position - candidate <= _MAX_REPEAT
            and position < reference_end
        ):
            repeat = position - candidate
            length = _match_length(source, candidate, position, reference_end + _TAIL_BYTES - 4)
            if length >= _MIN_LENGTH:
                block, length = _reference_block(repeat, length)
                blocks.append((True, block))
                position += length
                continue
        blocks.append((False, source[position : position + 1]))
        position += 1
    return blocks


def _match_length(source: bytes, candidate: int, position: int, limit: int) -> int:
    length = 0
    while position + length < limit and source[candidate + length] == source[position + length]:
        length += 1
    return length


def _reference_block(repeat: int, length: int) -> tuple[bytes, int]:
    """The shortest encoding for the copy, and the length it encodes."""
    if repeat < 1 << 6 and length == _MIN_LENGTH:
        return bytes([repeat << 2]), length
    if repeat < 1 << 14 and length == _MIN_LENGTH:
        return struct.pack("<H", repeat << 2 | 0x01), length
    if repeat < 1 << 10:
        length = min(length, 18)
        return struct.pack("<H", repeat << 6 | (length - 3) << 2 | 0x02), length
    if length <= 33:
        value = repeat << 7 | (length - 2) << 2 | 0x03
        return struct.pack("<I", value)[:3], length
    length = min(length, 258)
    return struct.pack("<I", repeat << 15 | (length - 3) << 7 | 0x03), length


def sample_data(size: int, seed: int) -> bytes:
    """Random bytes mixed with repeats near and far, some overlapping their copy."""
    rng = random.Random(seed)
    data = bytearray()
    while len(data) < size:
        choice = rng.random()
        if choice < 0.3 or len(data) < 64:
            data += rng.randbytes(rng.randint(1, 40))
        elif choice < 0.5:
            data += rng.randbytes(rng.randint(3, 8)) * rng.randint(2, 50)
        else:
            start = rng.randrange(len(data))
            data += data[start : start + rng.randint(3, 300)]
    return bytes(data[:size])
