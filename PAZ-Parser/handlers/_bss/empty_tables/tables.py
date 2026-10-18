from __future__ import annotations

# PABR tables the client ships with a count of 0 and an empty string table
# (docs/file-formats/empty_bss.md). Each file is 20 bytes.
EMPTY_PABR_TABLES: tuple[str, ...] = (
    "enchantlightstone.bss",
    "lightstoneenchantgroup.bss",
    "normalgroupquest.bss",
)
