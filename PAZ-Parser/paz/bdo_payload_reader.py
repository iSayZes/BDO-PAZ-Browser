from __future__ import annotations

import sys
from collections.abc import Sequence
from pathlib import Path

from .bdo_decompress import bdo_decompress, has_lz4_header
from .bdo_ice import BDO_ICE_KEY, IceCipher
from bdo_models import PazEntry

_CIPHER: IceCipher = IceCipher(BDO_ICE_KEY)

# The long header in front of a compressed or header-only payload (`bdo_decompress._Header`).
_HEADER_SIZE = 9


# ── ICE decrypt ───────────────────────────────────────────────────────────────

def _pad8(data: bytes) -> bytes:
    rem = len(data) % 8
    return data if rem == 0 else data + b"\x00" * (8 - rem)


def ice_decrypt_bytes(data: bytes, key: bytes = BDO_ICE_KEY) -> bytes:
    """Decrypt `data` with the ICE cipher.  Input is zero-padded to 8 bytes."""
    cipher = _CIPHER if key == BDO_ICE_KEY else IceCipher(key)
    padded = _pad8(data)
    return cipher.decrypt(padded)[: len(data)]


def ice_decrypt_many(inputs: Sequence[bytes]) -> list[bytes]:
    """Each input decrypted as `ice_decrypt_bytes` would, in one cipher call.

    ICE has no chaining between blocks, so the padded inputs can be joined,
    decrypted together and cut apart again. Worth it for many small inputs,
    where numpy's per-call cost outweighs the decryption.
    """
    decrypted = _CIPHER.decrypt(b"".join(_pad8(data) for data in inputs))
    outputs: list[bytes] = []
    start = 0
    for data in inputs:
        outputs.append(decrypted[start : start + len(data)])
        start += len(data) + -len(data) % 8
    return outputs


# ── Entry payload reader ──────────────────────────────────────────────────────

def read_raw_payload(archive_path: Path, entry: PazEntry) -> bytes:
    """The entry's stored bytes, still encrypted and compressed."""
    with archive_path.open("rb") as paz_stream:
        paz_stream.seek(entry.offset)
        raw_payload: bytes = paz_stream.read(entry.compressed_size)

    if len(raw_payload) != entry.compressed_size:
        raise ValueError(
            f"Unexpected payload length for {entry.internal_path}: "
            f"expected {entry.compressed_size}, got {len(raw_payload)}"
        )
    return raw_payload


def is_encrypted(entry: PazEntry) -> bool:
    """False for .dbss files, which are stored without ICE encryption."""
    return not entry.internal_path.endswith(".dbss")


def needs_decompress(entry: PazEntry, decrypted: bytes) -> bool:
    """True when the decrypted payload starts with a BDO header.

    The sizes tell. A payload with a header is smaller than the file
    (compressed, flag 0x6F) or at least 9 bytes larger (stored behind the
    header, flag 0x6E). A plain payload is the file itself, padded to the
    8-byte ICE block at most. Its first byte does not tell: official plain
    files start with 0x6E or 0x6F too (`questgroup.dbss` on client 3482,
    `itemtrade.bss` on client 435, padded). The rule matches every
    non-empty file on clients 435, 1485, 2519, 3482 and 3483.
    """
    return (
        entry.uncompressed_size > entry.compressed_size
        or entry.compressed_size >= entry.uncompressed_size + _HEADER_SIZE
        # A private server repack stores small files as LZ4 even when that
        # makes them larger (client 376350: 2,160 bytes for a 2,140-byte
        # `.bss`), so the sizes do not flag them.
        or has_lz4_header(decrypted, entry.uncompressed_size)
    )


def read_entry_payload(archive_path: Path, entry: PazEntry) -> bytes:
    """
    Read, decrypt, and decompress a single PAZ entry.

    Encryption is skipped for .dbss files.
    Decompression is applied when `needs_decompress` flags the payload.
    Zero padding past the recorded size (the 8-byte ICE block of a stored
    entry) is trimmed, as extraction does.
    """
    raw_payload = read_raw_payload(archive_path, entry)
    decrypted = ice_decrypt_bytes(raw_payload) if is_encrypted(entry) else raw_payload

    if needs_decompress(entry, decrypted):
        decompressed = bdo_decompress(decrypted, expected_size=entry.uncompressed_size)
        if len(decompressed) != entry.uncompressed_size and len(decrypted) == entry.uncompressed_size:
            print(
                f"[read_entry_payload] decompressed size {len(decompressed)} != "
                f"expected {entry.uncompressed_size} for {entry.internal_path}; "
                f"using raw payload instead",
                file=sys.stderr,
            )
            return decrypted
        return _trim_zero_padding(decompressed, entry.uncompressed_size)

    return _trim_zero_padding(decrypted, entry.uncompressed_size)


def _trim_zero_padding(payload: bytes, expected_size: int) -> bytes:
    """`payload` cut to `expected_size` when everything past it is zero.

    A stored entry is padded to the 8-byte ICE block (a 631-byte file reads as
    632), and a trailer read from the end of the file would land in that
    padding. Unlike extraction, a short payload or non-zero surplus is returned
    as it is, so the preview still shows what was decoded.
    """
    if len(payload) <= expected_size or any(payload[expected_size:]):
        return payload
    return payload[:expected_size]


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
