"""The BDO payload decompressor, compiled or in Python.

`bdo_decompress` reads the header and hands the stream to `UNPACK`: the
compiled `_bdo_native.unpack` (Rust, `PAZ-Parser/native/`) when it is
installed, else `unpack_python`. A header with the LZ4 flag goes to
`bdo_lz4.unpack_lz4` instead, in Python on both backends. The Python version is the reference, the
format has no public spec, and the two must return the same bytes and error
codes (`tests/test_decompress.py`).
"""

from __future__ import annotations

import struct
import sys
from dataclasses import dataclass

from . import native_backend
from .bdo_lz4 import unpack_lz4
from .native_backend import NativeUnpack

# (data, input_start, input_end, decompressed_length) -> decompressed bytes.
# Raises ValueError for a bad stream.
Unpack = NativeUnpack

# Lookup: how many literal bytes to copy when the group-header LSBs are zero.
# Indexed by (uiBlockGroupHeader & 0xF).  Only even indices are reachable
# (LSB must be 0 to reach the literal path).
_BDO_TABLE: list[int] = [4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0]

_U32_LE = struct.Struct("<I")
_SHORT_HEADER_SIZE = 3
_LONG_HEADER_SIZE = 9
_FLAG_COMPRESSED = 0x01
_FLAG_LONG = 0x02
_FLAG_LZ4 = 0x80


@dataclass(frozen=True)
class _Header:
    """Byte 0 = flags: 0x01 compressed, 0x02 long mode (4-byte lengths),
    0x80 LZ4 block instead of the BDO stream (private server repacks only,
    `bdo_lz4.py`).

    Long mode:  bytes 1-4 = compressed_length, bytes 5-8 = decompressed_length
    Short mode: byte 1 = compressed_length,    byte 2    = decompressed_length
    `compressed_length` counts the header.
    """

    is_compressed: bool
    is_lz4: bool
    size: int
    compressed_length: int
    decompressed_length: int


def _read_header(data: bytes) -> _Header:
    if not data:
        raise ValueError("BDO payload is empty.")
    flags = data[0]
    is_long = bool(flags & _FLAG_LONG)
    size = _LONG_HEADER_SIZE if is_long else _SHORT_HEADER_SIZE
    if len(data) < size:
        raise ValueError(f"BDO payload header is truncated: {len(data)} of {size} bytes.")
    if is_long:
        compressed_length: int = _U32_LE.unpack_from(data, 1)[0]
        decompressed_length: int = _U32_LE.unpack_from(data, 5)[0]
    else:
        compressed_length = data[1]
        decompressed_length = data[2]
    return _Header(
        is_compressed=bool(flags & _FLAG_COMPRESSED),
        is_lz4=bool(flags & _FLAG_LZ4),
        size=size,
        compressed_length=compressed_length,
        decompressed_length=decompressed_length,
    )


def has_lz4_header(data: bytes, expected_size: int) -> bool:
    """True when `data` opens with a long LZ4 header whose lengths fit it.

    UTF-8 text with a byte order mark also starts with 0xEF, so the flags
    alone do not tell; the decompressed length must equal `expected_size`
    and the compressed length must fit in `data`.
    """
    lz4_flags = _FLAG_LZ4 | _FLAG_LONG | _FLAG_COMPRESSED
    if len(data) < _LONG_HEADER_SIZE or data[0] & lz4_flags != lz4_flags:
        return False
    header = _read_header(data)
    return header.decompressed_length == expected_size and header.compressed_length <= len(data)


def bdo_decompress(data: bytes, expected_size: int | None = None, unpack: Unpack | None = None) -> bytes:
    """
    Decompress a BDO payload.

    expected_size: when provided (from PAZ entry metadata), overrides the
    decompressed_length field in the header if they differ.
    unpack: the backend, `UNPACK` when None; the parity tests pass each one.
    """
    header = _read_header(data)
    if expected_size is not None and expected_size != header.decompressed_length:
        print(
            f"[bdo_decompress] header decompressed_length={header.decompressed_length} "
            f"doesn't match expected_size={expected_size}; using expected_size",
            file=sys.stderr,
        )
    decompressed_length = expected_size if expected_size is not None else header.decompressed_length

    if not header.is_compressed:
        return data[header.size : header.size + decompressed_length]

    # A header claiming more bytes than the payload holds ends the stream at
    # the payload's end, so a truncated payload fails with an error code.
    input_end = min(header.compressed_length, len(data))
    if header.is_lz4:
        return unpack_lz4(data, header.size, input_end, decompressed_length)
    return (unpack or UNPACK)(data, header.size, input_end, decompressed_length)


# ── Python reference ──────────────────────────────────────────────────────────

def unpack_python(data: bytes, input_start: int, input_end: int, decompressed_length: int) -> bytes:
    """`data[input_start:input_end]` decompressed; the reference for `_bdo_native`."""
    output = bytearray(decompressed_length)
    result = _blackdesert_unpack_core(data, output, input_start, min(input_end, len(data)) - 1)
    if result < 0:
        raise ValueError(f"BDO decompression failed with error code {result}.")
    return bytes(output[:result])


def _bd_copy_tail(
    data: bytes | bytearray,
    output: bytearray,
    pInputIndex: int,
    pLastInputIndex: int,
    pOutputIndex: int,
    pLastOutputIndex: int,
    uiBlockGroupHeader: int,
) -> int:
    """Copy remaining bytes one at a time until the output buffer is full.

    Returns final pOutputIndex, or -4 if input is exhausted prematurely.
    """
    pEndOfInput = pLastInputIndex + 1
    while True:
        if uiBlockGroupHeader == 1:
            pInputIndex += 4
            uiBlockGroupHeader = 0x80000000

        if pInputIndex >= pEndOfInput:
            return -4

        output[pOutputIndex] = data[pInputIndex]
        pOutputIndex += 1
        pInputIndex += 1
        uiBlockGroupHeader >>= 1

        if pOutputIndex > pLastOutputIndex:
            return pOutputIndex


def _blackdesert_unpack_core(
    data: bytes | bytearray,
    output: bytearray,
    pInputIndex: int,
    pLastInputIndex: int,
) -> int:
    """
    Custom BDO decompressor, ported from kukdh1/PAZ-Unpacker Crypt.cpp

    Reads data[pInputIndex : pLastInputIndex + 1]; pLastInputIndex must be
    inside `data`. Returns the number of bytes written to `output`, or a
    negative error code.
    """
    pOutputIndex = 0
    uiBlockGroupHeader = 1
    pLastOutputIndex = len(output) - 1
    pLiteralEnd = max(0, pLastOutputIndex - 10)
    unpack_u32 = _U32_LE.unpack_from

    while True:
        # ── Inner loop: process one bit from the group header ─────────────
        while True:
            if uiBlockGroupHeader == 1:
                if pInputIndex + 3 > pLastInputIndex:
                    return -1
                uiBlockGroupHeader = unpack_u32(data, pInputIndex)[0]
                pInputIndex += 4

            if pInputIndex + 3 > pLastInputIndex:
                return -2

            uiBlockHeader: int = unpack_u32(data, pInputIndex)[0]

            if not (uiBlockGroupHeader & 1):
                break  # literal run

            # ── Back-reference block ──────────────────────────────────────
            # The low 2 bits pick the encoding: how far back the copy starts
            # (uiRepeatIndex), how many bytes it copies (uiBlockLength) and
            # how many input bytes the block header takes. Decoded inline,
            # not in a helper: this runs once per back-reference, over a
            # million times on a large texture, and the call cost 12%.
            header_low2 = uiBlockHeader & 0x03
            if header_low2 == 0x03:
                if (uiBlockHeader & 0x7F) == 3:
                    uiRepeatIndex = uiBlockHeader >> 15
                    uiBlockLength = ((uiBlockHeader >> 7) & 0xFF) + 3
                    pInputIndex += 4
                else:
                    uiRepeatIndex = (uiBlockHeader >> 7) & 0x1FFFF
                    uiBlockLength = ((uiBlockHeader >> 2) & 0x1F) + 2
                    pInputIndex += 3
            elif header_low2 == 0x02:
                uiRepeatIndex = (uiBlockHeader & 0xFFFF) >> 6   # uint16_t cast
                uiBlockLength = ((uiBlockHeader >> 2) & 0xF) + 3
                pInputIndex += 2
            elif header_low2 == 0x01:
                uiRepeatIndex = (uiBlockHeader & 0xFFFF) >> 2   # uint16_t cast
                uiBlockLength = 3
                pInputIndex += 2
            else:
                uiRepeatIndex = (uiBlockHeader & 0xFF) >> 2     # uint8_t cast
                uiBlockLength = 3
                pInputIndex += 1

            # Mimic C++ unsigned arithmetic for the length bound check. It
            # never wraps here: a back-reference needs pOutputIndex >= 3, and
            # every earlier block ended at pLastOutputIndex - 3 or before, so
            # the slice copy below always stays inside the output.
            remaining_unsigned = (pLastOutputIndex - pOutputIndex - 3) & 0xFFFFFFFF
            if (
                pOutputIndex - uiRepeatIndex < 0
                or uiRepeatIndex < 3
                or uiBlockLength > remaining_unsigned
            ):
                return -3
            pBlockEnd = pOutputIndex + uiBlockLength

            # LZSS back-reference copy, equal to a forward byte-by-byte copy
            # (the C++ 4-byte-write / advance-by-3 loop). A source that
            # overlaps the destination repeats its first uiRepeatIndex bytes.
            pSource = pOutputIndex - uiRepeatIndex
            if uiRepeatIndex >= uiBlockLength:
                output[pOutputIndex:pBlockEnd] = output[pSource : pSource + uiBlockLength]
            else:
                pattern = output[pSource:pOutputIndex]
                output[pOutputIndex:pBlockEnd] = (pattern * (uiBlockLength // uiRepeatIndex + 1))[:uiBlockLength]

            uiBlockGroupHeader >>= 1
            pOutputIndex = pBlockEnd

        # ── Literal run ───────────────────────────────────────────────────
        # The -2 check above leaves 4 input bytes, the most a run copies.
        if pOutputIndex >= pLiteralEnd:
            break

        valid_len = _BDO_TABLE[uiBlockGroupHeader & 0xF]
        output[pOutputIndex : pOutputIndex + valid_len] = data[pInputIndex : pInputIndex + valid_len]
        uiBlockGroupHeader >>= valid_len
        pOutputIndex += valid_len
        pInputIndex += valid_len

    # ── Tail: copy remaining bytes one at a time ──────────────────────────
    if pOutputIndex <= pLastOutputIndex:
        return _bd_copy_tail(
            data, output, pInputIndex, pLastInputIndex,
            pOutputIndex, pLastOutputIndex, uiBlockGroupHeader,
        )

    return pOutputIndex


NATIVE_UNPACK: Unpack | None = native_backend.UNPACK
UNPACK: Unpack = NATIVE_UNPACK or unpack_python
