from __future__ import annotations

import struct
from pathlib import Path

from bdo_ice import BDO_ICE_KEY, IceCipher
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

def _blackdesert_unpack_core(
    data: bytes | bytearray,
    output: bytearray,
    decompressed_length: int,
) -> int:
    """
    Custom BDO decompressor — ported from kukdh1/PAZ-Unpacker Crypt.cpp
    (originally from quickbms).

    Returns the number of bytes written to `output`, or a negative error code.
    """
    pOutputIndex = 0
    uiBlockGroupHeader = 1
    pLastOutputIndex = decompressed_length - 1

    flags = data[0]
    if flags & 0x02:
        uiCompressedLength: int = struct.unpack_from("<I", data, 1)[0]
        pInputIndex = 9
    else:
        uiCompressedLength = data[1]
        pInputIndex = 3

    pLastInputIndex = uiCompressedLength - 1

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

    return pOutputIndex


def bdo_decompress(data: bytes) -> bytes:
    """
    Decompress a BDO payload.

    Header layout (byte 0 = flags):
      bit 0 (0x01) — data is compressed
      bit 1 (0x02) — long mode (4-byte lengths), else short mode (1-byte lengths)

    Long mode:  bytes 1-4 = compressed_length, bytes 5-8 = decompressed_length
    Short mode: byte 1 = compressed_length,    byte 2    = decompressed_length
    """
    flags = data[0]
    is_long = bool(flags & 0x02)
    is_compressed = bool(flags & 0x01)

    if is_long:
        decompressed_length: int = struct.unpack_from("<I", data, 5)[0]
        raw_offset = 9
    else:
        decompressed_length = data[2]
        raw_offset = 3

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

    Encryption is skipped for .dbss files (matches C++ CheckEncrypt logic).
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
    needs_decompress = (
        entry.uncompressed_size > entry.compressed_size
        or (len(decrypted) > 0 and decrypted[0] == 0x6E)
    )

    if needs_decompress:
        return bdo_decompress(decrypted)

    return decrypted
