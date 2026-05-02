from dataclasses import dataclass

@dataclass(frozen=True)
class PazEntry:
    archive_name: str
    internal_path: str
    offset: int
    compressed_size: int
    uncompressed_size: int
    compression_type: int
    encryption_type: int


@dataclass(frozen=True)
class PazTable:
    paz_file_id: int
    crc: int
    size: int


@dataclass(frozen=True)
class MetaFile:
    version: int
    paz_file_count: int
    paz_files: list[PazTable]
