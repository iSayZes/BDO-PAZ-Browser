from __future__ import annotations

import logging
import struct
from pathlib import Path

from bdo_ice import BDO_ICE_KEY, IceCipher
from bdo_models import PazEntry, PazTable

# One cipher instance is shared — the key schedule is computed once at import.
_CIPHER: IceCipher = IceCipher(BDO_ICE_KEY)


def _pad8(data: bytes) -> bytes:
    """Pad data to a multiple of 8 bytes (ICE block size)."""
    rem = len(data) % 8
    return data if rem == 0 else data + b"\x00" * (8 - rem)


def _decrypt_path_block(encrypted: bytes) -> bytes:
    """Decrypt the ICE-encrypted path block and return the plaintext."""
    padded = _pad8(encrypted)
    decrypted = _CIPHER.decrypt(padded)
    return decrypted[: len(encrypted)]


def _parse_string_table(data: bytes, length: int) -> list[str]:
    """
    Parse the null-terminated string table from a decrypted path block.

    Each entry is a C string (null-terminated). The table is `length` bytes.
    """
    strings: list[str] = []
    offset = 0
    while offset < length:
        try:
            end = data.index(b"\x00", offset)
        except ValueError:
            # No null terminator — take remainder as last string.
            strings.append(data[offset:length].decode("utf-8", errors="replace"))
            break
        strings.append(data[offset:end].decode("utf-8", errors="replace"))
        offset = end + 1
    return strings


def parse_paz_file(paz_path: Path, paz_table: PazTable) -> list[PazEntry]:  # noqa: ARG001
    entries: list[PazEntry] = []

    with paz_path.open("rb") as file:
        header_data: bytes = file.read(12)
        if len(header_data) != 12:
            raise ValueError(f"Invalid PAZ header: {paz_path}")

        crc, file_count, path_length = struct.unpack("<III", header_data)

        logging.debug(
            "PAZ header | file=%s crc=%08x file_count=%d path_length=%d",
            paz_path.name,
            crc,
            file_count,
            path_length,
        )

        raw_infos_size: int = file_count * 24
        raw_infos: bytes = file.read(raw_infos_size)
        if len(raw_infos) != raw_infos_size:
            raise ValueError(f"Invalid file table in: {paz_path}")

        path_block_encrypted: bytes = file.read(path_length)
        if len(path_block_encrypted) != path_length:
            raise ValueError(f"Invalid path block in: {paz_path}")

    # Decrypt and parse the path block.
    path_block = _decrypt_path_block(path_block_encrypted)
    strings = _parse_string_table(path_block, path_length)

    for index in range(file_count):
        start: int = index * 24
        chunk: bytes = raw_infos[start : start + 24]

        (
            _file_crc,
            folder_id,
            file_id,
            offset,
            compressed_size,
            original_size,
        ) = struct.unpack("<IIIIII", chunk)

        # Reconstruct path: strings[folder_id] acts as the directory,
        # strings[file_id] acts as the filename.
        try:
            internal_path: str = strings[folder_id] + strings[file_id]
        except IndexError:
            logging.warning(
                "PAZ path out of range | file=%s index=%d folder_id=%d file_id=%d strings=%d",
                paz_path.name,
                index,
                folder_id,
                file_id,
                len(strings),
            )
            internal_path = (
                f"unknown/{paz_path.stem}_{index}"
                f"_c{compressed_size}_u{original_size}.bin"
            )

        entries.append(
            PazEntry(
                archive_name=paz_path.name,
                internal_path=internal_path,
                offset=offset,
                compressed_size=compressed_size,
                uncompressed_size=original_size,
                compression_type=0,
                encryption_type=0,
            )
        )

        logging.debug(
            "PAZ entry | file=%s index=%d path=%s offset=%d compressed=%d original=%d",
            paz_path.name,
            index,
            internal_path,
            offset,
            compressed_size,
            original_size,
        )

    return entries
