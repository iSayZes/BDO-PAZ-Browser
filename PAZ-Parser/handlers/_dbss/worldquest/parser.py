from __future__ import annotations

import struct


def parse_worldquest_records(data: bytes) -> list[dict]:
    if len(data) < 4:
        raise ValueError("worldquest.dbss is too short to contain a record-count header.")

    count = struct.unpack_from("<I", data, 0)[0]
    extra_bytes = len(data) - 4

    if count == 0:
        return [
            {
                "count": count,
                "status": "No world quest records",
                "extra_bytes": extra_bytes,
            }
        ]

    raise ValueError(
        "worldquest.dbss has non-empty records, but only the empty placeholder layout is documented."
    )
