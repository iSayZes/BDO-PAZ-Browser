"""The content key of a client: its meta version plus a digest of the `.meta` archive rows.

Each archive row holds the archive's checksum (`pa_checksum` of the file from
byte 4 on) and its size, so a change to any file inside an archive changes
the key, while a copy of the folder keeps it. Caches built from file contents
(thumbnails, world map tiles) key on it: a patch changes the version, and a
repack under the same version changes the digest. A writer that edits an
archive must write its new checksum and size into the `.meta` row, or these
caches stay on the old content.
"""
from __future__ import annotations

import hashlib
import struct

from bdo_models import MetaFile

_ROW = struct.Struct("<III")
# Hex characters of the digest kept in the key (64 bits).
_DIGEST_CHARS = 16


def content_key(meta: MetaFile) -> str:
    """`<version>-<digest>`, the digest over every archive row in `.meta` order."""
    rows = b"".join(_ROW.pack(row.paz_file_id, row.crc, row.size) for row in meta.paz_files)
    return f"{meta.version}-{hashlib.sha256(rows).hexdigest()[:_DIGEST_CHARS]}"
