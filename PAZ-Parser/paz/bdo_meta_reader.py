from __future__ import annotations

from pathlib import Path
import struct

from bdo_models import MetaFile, PazTable


def read_bdo_meta(meta_path: Path) -> MetaFile:
    with meta_path.open("rb") as file:
        header: bytes = file.read(8)
        if len(header) != 8:
            raise ValueError(f"Invalid meta header: {meta_path}")

        version, paz_file_count = struct.unpack("<II", header)

        paz_files: list[PazTable] = []

        for _ in range(paz_file_count):
            entry_data: bytes = file.read(12)
            if len(entry_data) != 12:
                raise ValueError(f"Invalid PAZ table entry in: {meta_path}")

            paz_file_id, crc, size = struct.unpack("<III", entry_data)
            paz_files.append(
                PazTable(
                    paz_file_id=paz_file_id,
                    crc=crc,
                    size=size,
                )
            )

    return MetaFile(
        version=version,
        paz_file_count=paz_file_count,
        paz_files=paz_files,
    )