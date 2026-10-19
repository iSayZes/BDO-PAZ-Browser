from __future__ import annotations

# PABR tables the client ships with a count of 0 and an empty string table
# (docs/file-formats/empty_bss.md). Each file is 20 bytes.
EMPTY_PABR_TABLES: tuple[str, ...] = (
    "audiorenewal.bss",
    "beginnerroadmaplinkurldata.bss",
    "cashproduct_discountperiodcheck.bss",
    "commonskill.bss",
    "dropuiurlinfo.bss",
    "enchantlightstone.bss",
    "fishinginfo.bss",
    "instancefieldenteroption.bss",
    "instancefieldmanagement.bss",
    "itembundle.bss",
    "lightstoneenchantgroup.bss",
    "normalgroupquest.bss",
    "openuiwhennak.bss",
    "preloadpcactioncharacter.bss",
    "shadowarenalist.bss",
    "skillselectuiinfo.bss",
    "spawngroup.bss",
    "tempcashstaticstatus.bss",
)
