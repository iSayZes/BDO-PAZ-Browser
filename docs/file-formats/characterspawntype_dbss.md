# `characterspawntype.dbss` Format

## Purpose

Boolean flag table for in-world entity spawn types. Each record associates an entity ID (NPC, character, object, or item) with 44 independent boolean flags that encode spawn-type capabilities or interaction properties.

Example:

```text
entity_id: 47659  →  "Alper (Stable Keeper)"
flags set: flag_00, flag_02, flag_05, flag_08, flag_13, flag_29
```

## Graph

### Tags

- file format
- dbss
- npc
- spawn type

### Connections

- [languagedata_en.loc](languagedata_loc.md) — NPC names (str_type=6, str_id1=entity_id)

---

## Companion Files

| File                            | Required | Role                                         |
| ------------------------------- | -------- | -------------------------------------------- |
| `characterspawntypeoffset.dbss` | Required | Maps entity IDs to byte offsets in this file |

All multi-byte values are little-endian.

---

## File Layout

### Header (4 bytes)

| Offset  | Type | Field | Notes                                      |
| ------- | ---- | ----- | ------------------------------------------ |
| `+0x00` | u32  | count | Number of records (24017 in observed data) |

### Record (48 bytes, repeated `count` times)

| Offset  | Type   | Field     | Notes                                                     |
| ------- | ------ | --------- | --------------------------------------------------------- |
| `+0x00` | u32    | entity_id | Full entity identifier (see Entity ID Namespaces below)   |
| `+0x04` | u8[44] | flags     | 44 independent boolean bytes, each 0 or 1; see flag table |

#### Entity ID Namespaces

IDs are 32-bit values. The upper 16 bits indicate the entity namespace:

| Upper 16 bits | Range            | Observed Count | Entity Category          |
| ------------- | ---------------- | -------------- | ------------------------ |
| `0x0000`      | 0 – 65,535       | 2,404          | Standard NPCs/characters |
| `0x0001`      | 65,536 – 131,071 | 21,561         | World objects / items    |
| `0x0100`      | 16,777,216+      | 52             | Special entity types     |

The lower 16 bits are unique across all records (no collisions across namespaces).

#### Flag Layout (bytes `+0x04` – `+0x2F`)

The 44 flag bytes are stored as 11 contiguous groups of 4, aligned to 4-byte boundaries. Each byte is independently 0 (unset) or 1 (set) — no bitmask packing.

| Group | Byte Offsets in Record | Flag Indices      |
| ----- | ---------------------- | ----------------- |
| 0     | `+0x04` – `+0x07`      | flag_00 – flag_03 |
| 1     | `+0x08` – `+0x0B`      | flag_04 – flag_07 |
| 2     | `+0x0C` – `+0x0F`      | flag_08 – flag_11 |
| 3     | `+0x10` – `+0x13`      | flag_12 – flag_15 |
| 4     | `+0x14` – `+0x17`      | flag_16 – flag_19 |
| 5     | `+0x18` – `+0x1B`      | flag_20 – flag_23 |
| 6     | `+0x1C` – `+0x1F`      | flag_24 – flag_27 |
| 7     | `+0x20` – `+0x23`      | flag_28 – flag_31 |
| 8     | `+0x24` – `+0x27`      | flag_32 – flag_35 |
| 9     | `+0x28` – `+0x2B`      | flag_36 – flag_39 |
| 10    | `+0x2C` – `+0x2F`      | flag_40 – flag_43 |

---

## Enum Values

### Known Flag Identities

Identified from isolated single-flag records, cross-referenced with in-game NPC roles (confirmed unless noted):

| Flag Index | Proposed Name        | Evidence / Example Entity                                                          |
| ---------- | -------------------- | ---------------------------------------------------------------------------------- |
| flag_01    | `villa_vendor`       | Villa Keepers in Valencia (sell Villa Invitations); id=45351                       |
| flag_12    | `quest_variant`      | Quest-specific NPC variants (e.g. quest version of Maestio); id=49724              |
| flag_14    | `battlefield_vendor` | Red Battlefield potion vendor; id=40743                                            |
| flag_15    | `wandering_merchant` | Wandering Merchant NPC type; id=62223                                              |
| flag_18    | `specialty_shop`     | Single-item specialty vendors (e.g. Manny — Empty Bottles only); id=40771          |
| flag_22    | `guild_vendor`       | Guild item vendors (e.g. Olympia); id=47144                                        |
| flag_30    | `event_npc`          | Time-limited event NPCs (e.g. Great Expedition Secret Shop, now removed); id=59110 |
| flag_32    | `timed_spawn`        | NPCs with a restricted spawn window (e.g. Morco: 2:00–22:00); id=47024             |
| flag_43    | `main_quest`         | Main story quest NPCs; id=58134                                                    |

Flags still unidentified (no isolated example found — only appear alongside others):

- flag_00, flag_02, flag_03, flag_05, flag_08–flag_11, flag_13, flag_16–flag_17, flag_19–flag_21, flag_23–flag_29, flag_31, flag_33–flag_42

**Notes on common flags:**

- flag_02 and flag_08 appear together on almost every interactive NPC (vendors, managers, stable keepers). Likely foundational "has interaction UI" flags.
- flag_29 appears on both Stable Keepers and placeholder entity 9999; possibly `stable_system` or a horse-related flag.

### Observed Flag Patterns by NPC Type

| NPC Role                  | Flags Set                                            |
| ------------------------- | ---------------------------------------------------- |
| Imperial Fishing Delivery | flag_02                                              |
| Villa Keeper              | flag_01                                              |
| Imperial Auction Manager  | flag_08                                              |
| Node Manager              | flag_02, flag_08, flag_10                            |
| General Goods Vendor      | flag_02, flag_08, flag_18                            |
| Trade Manager             | flag_02, flag_03, flag_08                            |
| Arms Dealer               | flag_00, flag_02, flag_08, flag_15                   |
| Stable Keeper             | flag_00, flag_02, flag_05, flag_08, flag_13, flag_29 |

---

## characterspawntypeoffset.dbss

A parallel lookup index with one entry per main file record.

### Header (8 bytes)

| Offset  | Type  | Field | Notes                                            |
| ------- | ----- | ----- | ------------------------------------------------ |
| `+0x00` | u8[4] | magic | `PABR` (ASCII)                                   |
| `+0x04` | u32   | count | Number of index records; matches main file count |

### Index Record (10 bytes, repeated `count` times)

| Offset  | Type | Field    | Notes                                                               |
| ------- | ---- | -------- | ------------------------------------------------------------------- |
| `+0x00` | u16  | id_low16 | Lower 16 bits of `entity_id`; unique across all records in the file |
| `+0x02` | u32  | offset   | Byte offset into `characterspawntype.dbss`                          |
| `+0x06` | u32  | size     | Record byte count; always 48                                        |

### Trailer (12 bytes)

Follows the last index record. Appears to be a sentinel:

| Offset  | Type | Value  | Notes                                      |
| ------- | ---- | ------ | ------------------------------------------ |
| `+0x00` | u32  | 0      | —                                          |
| `+0x04` | u32  | varies | Byte offset of end-of-records in this file |
| `+0x08` | u32  | 0      | —                                          |

---

## Suggested UI Layout

| Column    | Type | Notes                                                             |
| --------- | ---- | ----------------------------------------------------------------- |
| entity_id | num  | Right-aligned; also show as hex in a tooltip                      |
| Name (EN) | text | LOC str_type=6, str_id1=entity_id; type=0 or 50 for objects/items |
| flag_00   | bool | 0/1; hide all-zero columns by default to reduce noise             |
| …         | bool | One column per flag                                               |

Rows with all flags = 0 can be hidden by default — most world objects and invisible spawn proxies fall in this category.

---

## Notes

- 95 unique flag patterns across 24017 records; the all-zeros pattern covers 21,563 records (89.8%).
- Records are stored in the order indexed by `characterspawntypeoffset.dbss` — not sorted by entity ID.
- The majority of all-zeros records are world objects, items, and invisible system NPCs used for spawn logic and interaction proxies.
- 9 of the 44 flags have been identified from in-game observation. The remaining 35 are still unknown.
- Values outside {0, 1} have not been observed in flag bytes.
