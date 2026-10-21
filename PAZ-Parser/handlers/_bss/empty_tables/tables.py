from __future__ import annotations

# PABR tables the client ships with a count of 0 and an empty string table
# (docs/file-formats/empty_bss.md). Each file is 20 bytes on the live client;
# cashproductcachedata, charactertrigger, equipitemchanage and naktype hold
# records on an older client, which this handler rejects.
EMPTY_PABR_TABLES: tuple[str, ...] = (
    "audiorenewal.bss",
    "beginnerroadmaplinkurldata.bss",
    "cashproduct_discountperiodcheck.bss",
    "cashproductcachedata.bss",
    "charactertrigger.bss",
    "commonskill.bss",
    "dropuiurlinfo.bss",
    "enchantlightstone.bss",
    "equipitemchanage.bss",
    "fishinginfo.bss",
    "instancefieldenteroption.bss",
    "instancefieldmanagement.bss",
    "itembundle.bss",
    "lightstoneenchantgroup.bss",
    "naktype.bss",
    "normalgroupquest.bss",
    "openuiwhennak.bss",
    "preloadpcactioncharacter.bss",
    "shadowarenalist.bss",
    "skillselectuiinfo.bss",
    "spawngroup.bss",
    "tempcashstaticstatus.bss",
)
