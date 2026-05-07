from __future__ import annotations

from _common.binary import u32_hi, u32_lo

# Do not treat these as confirmed color names.
# These are only observed numeric values until verified against in-game data.
STYLE_NAMES: dict[int, str] = {
    6: "Observed style 6",
    7: "Observed style 7",
    8: "Observed style 8",
    9: "Observed style 9",
    10: "Observed style 10",
    11: "Observed style 11",
}

U32_20_STYLE_MAP: dict[str, str] = {
    "65:80": "Gold-ish",
    "80:60": "Yellow-ish",
    "60:0": "Purple",
    "0:0": "Grey",
    "52:49436": "Special (sample)",
    "64:49436": "Normal (sample)",
}


def style_key(u32_20: int) -> str:
    return f"{u32_hi(u32_20)}:{u32_lo(u32_20)}"


def packed_word_cell(fields: dict[str, int], max_offset: int | None) -> str:
    parts: list[str] = []

    for name, value in fields.items():
        offset = int(name.split("_")[1], 16)

        if max_offset is not None and offset >= max_offset:
            continue

        if value == 0:
            continue

        hi = u32_hi(value)
        lo = u32_lo(value)

        if hi > 1000 and lo > 1000:
            continue

        parts.append(f"{name}=0x{value:08X} ({hi}:{lo})")

    return " ".join(parts) if parts else "—"
