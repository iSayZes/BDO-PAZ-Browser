from __future__ import annotations

import struct
import sys
from pathlib import Path

from .bdo_ice import BDO_ICE_KEY, IceCipher
from bdo_models import PazEntry

_CIPHER: IceCipher = IceCipher(BDO_ICE_KEY)

# Lookup: how many literal bytes to copy when the group-header LSBs are zero.
# Indexed by (uiBlockGroupHeader & 0xF).  Only even indices are reachable
# (LSB must be 0 to reach the literal path).
_BDO_TABLE: list[int] = [4, 0, 1, 0, 2, 0, 1, 0, 3, 0, 1, 0, 2, 0, 1, 0]


# ── ICE decrypt ───────────────────────────────────────────────────────────────

def _pad8(data: bytes) -> bytes:
    rem = len(data) % 8
    return data if rem == 0 else data + b"\x00" * (8 - rem)


def ice_decrypt_bytes(data: bytes, key: bytes = BDO_ICE_KEY) -> bytes:
    """Decrypt `data` with the ICE cipher.  Input is zero-padded to 8 bytes."""
    cipher = _CIPHER if key == BDO_ICE_KEY else IceCipher(key)
    padded = _pad8(data)
    return cipher.decrypt(padded)[: len(data)]


# ── BDO decompression ─────────────────────────────────────────────────────────

def _bd_parse_header(data: bytes | bytearray) -> tuple[int, int]:
    """Read the BDO compression header flags and return (pInputIndex, pLastInputIndex)."""
    flags = data[0]
    if flags & 0x02:
        uiCompressedLength: int = struct.unpack_from("<I", data, 1)[0]
        pInputIndex = 9
    else:
        uiCompressedLength = data[1]
        pInputIndex = 3
    return pInputIndex, uiCompressedLength - 1


def _bd_decode_backref(
    data: bytes | bytearray,
    pInputIndex: int,
    uiBlockHeader: int,
) -> tuple[int, int, int]:
    """Decode a back-reference block and return (uiRepeatIndex, uiBlockLength, new_pInputIndex)."""
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
    return uiRepeatIndex, uiBlockLength, pInputIndex


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
    decompressed_length: int,
) -> int:
    """
    Custom BDO decompressor — ported from kukdh1/PAZ-Unpacker Crypt.cpp

    Returns the number of bytes written to `output`, or a negative error code.
    """
    pOutputIndex = 0
    uiBlockGroupHeader = 1
    pLastOutputIndex = decompressed_length - 1

    pInputIndex, pLastInputIndex = _bd_parse_header(data)

    while True:
        # ── Inner loop: process one bit from the group header ─────────────
        while True:
            if uiBlockGroupHeader == 1:
                if pInputIndex + 3 > pLastInputIndex:
                    return -1
                uiBlockGroupHeader = struct.unpack_from("<I", data, pInputIndex)[0]
                pInputIndex += 4

            if pInputIndex + 3 > pLastInputIndex:
                return -2

            uiBlockHeader: int = struct.unpack_from("<I", data, pInputIndex)[0]

            if not (uiBlockGroupHeader & 1):
                break  # literal run

            # ── Back-reference block ──────────────────────────────────────
            uiRepeatIndex, uiBlockLength, pInputIndex = _bd_decode_backref(
                data, pInputIndex, uiBlockHeader
            )

            # Mimic C++ unsigned arithmetic for the length bound check.
            remaining_unsigned = (pLastOutputIndex - pOutputIndex - 3) & 0xFFFFFFFF
            if (
                pOutputIndex - uiRepeatIndex < 0
                or uiRepeatIndex < 3
                or uiBlockLength > remaining_unsigned
            ):
                return -3

            # LZSS back-reference copy (byte-by-byte equivalent of the C++
            # 4-byte-write / advance-by-3 loop).
            for k in range(uiBlockLength):
                output[pOutputIndex + k] = output[pOutputIndex + k - uiRepeatIndex]

            uiBlockGroupHeader >>= 1
            pOutputIndex += uiBlockLength

        # ── Literal run ───────────────────────────────────────────────────
        if pOutputIndex >= max(0, pLastOutputIndex - 10):
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


def bdo_decompress(data: bytes, expected_size: int | None = None) -> bytes:
    """
    Decompress a BDO payload.

    Header layout (byte 0 = flags):
      bit 0 (0x01) — data is compressed
      bit 1 (0x02) — long mode (4-byte lengths), else short mode (1-byte lengths)

    Long mode:  bytes 1-4 = compressed_length, bytes 5-8 = decompressed_length
    Short mode: byte 1 = compressed_length,    byte 2    = decompressed_length

    expected_size: when provided (from PAZ entry metadata), overrides the
    decompressed_length field in the header if they differ.
    """
    flags = data[0]
    is_long = bool(flags & 0x02)
    is_compressed = bool(flags & 0x01)

    if is_long:
        header_size: int = struct.unpack_from("<I", data, 5)[0]
        raw_offset = 9
    else:
        header_size = data[2]
        raw_offset = 3

    if expected_size is not None and expected_size != header_size:
        print(
            f"[bdo_decompress] header decompressed_length={header_size} "
            f"doesn't match expected_size={expected_size}; using expected_size",
            file=sys.stderr,
        )
    decompressed_length = expected_size if expected_size is not None else header_size

    if not is_compressed:
        return data[raw_offset : raw_offset + decompressed_length]

    output = bytearray(decompressed_length)
    result = _blackdesert_unpack_core(data, output, decompressed_length)
    if result < 0:
        raise ValueError(f"BDO decompression failed with error code {result}.")
    return bytes(output[:result])


# ── Entry payload reader ──────────────────────────────────────────────────────

def read_entry_payload(archive_path: Path, entry: PazEntry) -> bytes:
    """
    Read, decrypt, and decompress a single PAZ entry.

    Encryption is skipped for .dbss files.
    Decompression is applied when original_size > compressed_size OR when the
    first byte of the decrypted data is 0x6E.
    """
    with archive_path.open("rb") as paz_stream:
        paz_stream.seek(entry.offset)
        raw_payload: bytes = paz_stream.read(entry.compressed_size)

    if len(raw_payload) != entry.compressed_size:
        raise ValueError(
            f"Unexpected payload length for {entry.internal_path}: "
            f"expected {entry.compressed_size}, got {len(raw_payload)}"
        )

    # .dbss files are stored without ICE encryption.
    skip_decrypt = entry.internal_path.endswith(".dbss")

    if skip_decrypt:
        decrypted = raw_payload
    else:
        decrypted = ice_decrypt_bytes(raw_payload)

    # Decompress when flagged by size mismatch or the 0x6E magic byte.
    # Skip the 0x6E check when the raw bytes already equal the expected
    # uncompressed size — those bytes are stored raw, not compressed.
    needs_decompress = (
        entry.uncompressed_size > entry.compressed_size
        or (
            len(decrypted) > 0
            and decrypted[0] == 0x6E
            and len(decrypted) != entry.uncompressed_size
        )
    )

    if needs_decompress:
        decompressed = bdo_decompress(decrypted, expected_size=entry.uncompressed_size)
        if len(decompressed) != entry.uncompressed_size and len(decrypted) == entry.uncompressed_size:
            print(
                f"[read_entry_payload] decompressed size {len(decompressed)} != "
                f"expected {entry.uncompressed_size} for {entry.internal_path}; "
                f"using raw payload instead",
                file=sys.stderr,
            )
            return decrypted
        return decompressed

    return decrypted


# ── Range / page read ─────────────────────────────────────────────────────────

def can_range_read(entry: PazEntry) -> bool:
    """True when bytes can be sliced directly from the archive without full decode.

    Requires both conditions:
    - .dbss extension: no ICE encryption applied
    - compressed_size == uncompressed_size: no compression applied
    """
    return (
        entry.internal_path.endswith(".dbss")
        and entry.compressed_size == entry.uncompressed_size
    )


def read_entry_range(archive_path: Path, entry: PazEntry, offset: int, length: int) -> bytes:
    """Read `length` decoded bytes starting at `offset` within the entry payload.

    Seeks directly for range-readable entries (no encryption, no compression).
    Falls back to full decode + slice for compressed or encrypted entries.
    """
    if can_range_read(entry):
        available = max(0, entry.uncompressed_size - offset)
        to_read = min(length, available)
        if to_read <= 0:
            return b""
        with archive_path.open("rb") as f:
            f.seek(entry.offset + offset)
            return f.read(to_read)
    data = read_entry_payload(archive_path, entry)
    return data[offset : offset + length]
