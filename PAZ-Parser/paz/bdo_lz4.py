"""The LZ4 block decoder for payloads whose header sets flag 0x80.

Pearl Abyss archives never set the flag; a private server's repack tool
does (client 376350: 159 payloads, all in archives it rewrote, from logos
to `.bss` tables). The client reads them, so the browser does too.

The stream after the header is one raw LZ4 block (no frame, no checksum):
a sequence is a token (high nibble literal count, low nibble match length
minus 4, 15 meaning more length bytes follow, each added until one is not
255), the literals, then a u16 back-reference offset. The last sequence
holds literals only and ends the block.
"""

from __future__ import annotations

_NIBBLE_MAX = 15
_LENGTH_BYTE_MAX = 255
_MIN_MATCH = 4
_OFFSET_SIZE = 2


def unpack_lz4(data: bytes, input_start: int, input_end: int, decompressed_length: int) -> bytes:
    """`data[input_start:input_end]` as an LZ4 block of `decompressed_length` bytes.

    Raises ValueError for a stream that runs out early, copies from before
    the output's start, or does not fill the output exactly.
    """
    output = bytearray()
    position = input_start
    while position < input_end:
        token = data[position]
        position += 1

        literals, position = _read_length(data, position, input_end, token >> 4)
        if position + literals > input_end:
            raise ValueError("BDO LZ4 block: literals run past the end of the stream.")
        output += data[position : position + literals]
        position += literals
        if position == input_end:
            break

        if position + _OFFSET_SIZE > input_end:
            raise ValueError("BDO LZ4 block: back-reference offset runs past the end of the stream.")
        offset = data[position] | data[position + 1] << 8
        position += _OFFSET_SIZE
        match, position = _read_length(data, position, input_end, token & _NIBBLE_MAX)
        _copy_match(output, offset, match + _MIN_MATCH)
        if len(output) > decompressed_length:
            break

    if len(output) != decompressed_length:
        raise ValueError(
            f"BDO LZ4 block decodes to {len(output):,} bytes, expected {decompressed_length:,}."
        )
    return bytes(output)


def _read_length(data: bytes, position: int, input_end: int, nibble: int) -> tuple[int, int]:
    """The length a token nibble starts, plus its extra bytes; and the next position."""
    length = nibble
    if nibble != _NIBBLE_MAX:
        return length, position
    while True:
        if position >= input_end:
            raise ValueError("BDO LZ4 block: a length runs past the end of the stream.")
        extra = data[position]
        position += 1
        length += extra
        if extra != _LENGTH_BYTE_MAX:
            return length, position


def _copy_match(output: bytearray, offset: int, length: int) -> None:
    """Append `length` bytes copied from `offset` back; an overlapping copy repeats."""
    if offset == 0 or offset > len(output):
        raise ValueError(
            f"BDO LZ4 block: back-reference {offset} at output {len(output):,} points before the start."
        )
    start = len(output) - offset
    if offset >= length:
        output += output[start : start + length]
    else:
        pattern = output[start:]
        output += (pattern * (length // offset + 1))[:length]
