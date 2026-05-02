from __future__ import annotations

from .constants import PA_COLOR_MARKER


def first_pa_color_offset(block: bytes) -> int | None:
    index = block.find(PA_COLOR_MARKER)

    if index == -1:
        return None

    return index


def extract_pa_colors(block: bytes) -> list[str]:
    colors: list[str] = []
    pos = 0

    while True:
        idx = block.find(PA_COLOR_MARKER, pos)

        if idx == -1:
            break

        p = idx + len(PA_COLOR_MARKER)
        hex_chars: list[str] = []

        while p + 2 <= len(block):
            codepoint = int.from_bytes(block[p:p + 2], "little")

            if codepoint in (0x3E, 0):
                break

            hex_chars.append(chr(codepoint))
            p += 2

        if hex_chars:
            colors.append("".join(hex_chars))

        pos = idx + len(PA_COLOR_MARKER)

    return colors
