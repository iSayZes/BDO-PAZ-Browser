# `characterstatic.dbss` Format

## Purpose

Variable-length character/NPC static data table. Each record is keyed by a character ID and stores a small fixed prefix, an inline action/script string, and a large numeric attribute block. Many observed records have a `getknowledge(<id>);` script, which links the character to a knowledge reward.

Example:

```text
character_id: 47759 -> "Edania Merchant"
script: getknowledge(14469);
```

## Graph

### Tags

- file format
- dbss
- character
- npc
- knowledge

### Connections

- [characterstaticoffset.dbss](#characterstaticoffsetdbss) - required offset table for `characterstatic.dbss`
- [languagedata_en.loc](languagedata_loc.md) - NPC/character names with `str_type=6`, `str_id1=character_id`
- [knowledgelearning.dbss](knowledgelearning_dbss.md) - related knowledge IDs referenced by observed `getknowledge(...)` scripts

---

## Companion Files

| File                    | Required | Role                                                   |
| ----------------------- | -------- | ------------------------------------------------------ |
| `characterstaticoffset.dbss` | Required | Maps `character_id_low16` to byte offset and payload size |
| `languagedata_en.loc`   | Optional | Resolves display names for `character_id`              |

Related but not required:

| File                                                   | Role |
| ------------------------------------------------------ | ---- |
| `hardcorerandomspawncharacterstaticstatusmanager.bss`  | Small `PABR` data file that references character IDs, including `62223` ("Wandering Merchant"); layout not yet decoded |
| `playercharacterstatic.bss`                            | Small related BSS entry; extraction currently reports a size mismatch in observed PAZ data |
| `fuelinsertcharacterstaticstatus.bss`                  | Small related BSS entry; extraction currently reports a size mismatch in observed PAZ data |

All multi-byte integer values observed in the DBSS payload are little-endian unless noted otherwise.

---

## File Layout

| Offset  | Type | Field         | Notes                                      |
| ------- | ---- | ------------- | ------------------------------------------ |
| `+0x00` | u32  | record_count  | Number of records; observed `24017`        |
| `+0x04` | ...  | record_stream | Repeated inline ID + variable-length payload chunks |

The stream is not fixed-width. Use `characterstaticoffset.dbss` to slice records.

---

## Record Structure

### Stream Entry

Each logical record occupies `2 + payload_size` bytes in the main stream.

| Offset  | Type | Field              | Notes |
| ------- | ---- | ------------------ | ----- |
| `+0x00` | u16  | character_id_low16 | Matches the offset-table `character_id_low16`; unique across observed records |
| `+0x02` | ...  | payload            | Starts at the offset listed in `characterstaticoffset.dbss`; byte count is `payload_size` |

Offset-table `data_offset` values point to the payload, not to the inline `character_id_low16`. In observed data, the two bytes immediately before every `data_offset` equal the row's `character_id_low16`.

### Payload Prefix

| Offset  | Type  | Field       | Notes |
| ------- | ----- | ----------- | ----- |
| `+0x00` | u32   | unknown_00  | Observed examples include `0` and `257`; likely status/flag data |
| `+0x04` | u32   | unknown_04  | Observed examples include `256` and `65792`; likely status/flag data |
| `+0x08` | u32   | unknown_08  | Observed examples include `21` and `5141` |
| `+0x0C` | u32   | unknown_0c  | Observed `0` in sampled records |
| `+0x10` | utf16be_z | script | Null-terminated UTF-16BE string; often empty or `getknowledge(<id>);` |
| after string | u8[8] | zero_padding | Eight zero bytes observed after the string terminator |
| after padding | ... | numeric_block | Variable-size numeric attribute block |

String byte order is UTF-16BE in observed data. This is unusual for this project because most BDO binary strings and all documented DBSS numeric values are little-endian.

### Numeric Block

The numeric block begins with the character ID again.

| Relative Offset | Type | Field             | Notes |
| --------------- | ---- | ----------------- | ----- |
| `+0x00`         | u32  | character_id_low16 | Matches stream ID and offset-table ID; high 16 bits are `0` in observed rows |
| `+0x04`         | u32  | unknown_04        | Common observed values include `1`, `2`, `7`, and `8` |
| `+0x08`         | u32  | unknown_08        | Usually `0`; `65535` appears in some rows |
| `+0x0C`         | u32  | unknown_0c        | Usually `0`; high-bit flag values appear in some rows |
| `+0x10` onward  | ...  | attributes        | Mixed u32/f32-like fields; many common constants and zero regions |

Observed `payload_size` ranges from `478` to `1055` bytes. The size variation is mostly driven by `script` length and by trailing attribute data whose semantic partitioning is not yet confirmed.

---

## Script Values

Observed action/script prefixes:

| Script Pattern          | Observed Count | Notes |
| ----------------------- | -------------- | ----- |
| empty string            | `18109`        | Most records |
| `getknowledge(<id>);`   | `5602`         | Links character interaction to a knowledge ID |
| other/control-like text | `306`          | Short non-printable or one-character strings; semantic role unresolved |

The `getknowledge` argument appears to be a knowledge-related ID, but this doc does not yet prove the exact foreign-key target for every value.

---

## `characterstaticoffset.dbss`

Provides lookup rows for `characterstatic.dbss`.

### Header (8 bytes)

| Offset  | Type  | Field | Notes |
| ------- | ----- | ----- | ----- |
| `+0x00` | u8[4] | magic | ASCII `PABR` |
| `+0x04` | u32   | count | Number of rows; observed `24017`, matching `characterstatic.dbss` |

### Index Row (10 bytes, repeated `count` times)

| Offset  | Type | Field              | Notes |
| ------- | ---- | ------------------ | ----- |
| `+0x00` | u16  | character_id_low16 | Matches the two inline ID bytes immediately before `data_offset` |
| `+0x02` | u32  | data_offset        | Absolute byte offset into `characterstatic.dbss` payload data |
| `+0x06` | u32  | payload_size       | Payload byte count, excluding the two inline ID bytes |

### Trailer (12 bytes)

| Offset  | Type | Value | Notes |
| ------- | ---- | ----- | ----- |
| `+0x00` | u32  | `0`   | Sentinel-like value |
| `+0x04` | u32  | varies | Observed `240178`; equals the end offset of the offset-table rows |
| `+0x08` | u32  | `0`   | Sentinel-like value |

Rows sorted by `data_offset` cover the whole main file from `+0x04` through EOF when the two inline ID bytes before each payload are included.

---

## Suggested UI Layout

| Column       | Type | Notes |
| ------------ | ---- | ----- |
| Character ID | num  | `character_id_low16`; right-aligned |
| Name         | text | LOC lookup `str_type=6`, `str_id1=character_id`; prefer English, fallback to ID |
| Script       | text | Decoded UTF-16BE script string |
| Knowledge ID | num | Extract from `getknowledge(<id>);` when present |
| Payload Size | num | Useful for debugging variable layouts |
| Unknown Type | num | `numeric_block +0x04`; common grouping value |

---

## Notes

- Observed files contain `24017` records.
- Offset rows are sorted by descending character ID in early data but should be treated as an index, not as a sorted table guarantee.
- `character_id_low16` values are unique in observed data; no high-16 namespace was required to disambiguate this file.
- LOC lookup confirms sample IDs: `47759` is "Edania Merchant", `16640` is "Dev Plant210", and `62223` is "Wandering Merchant".
- `characterstaticoffset.dbss` uses the same `PABR` 10-byte row pattern as `characterspawntypeoffset.dbss`, but its `data_offset` points after an inline u16 ID.

---

## Open Questions

### Numeric Attribute Semantics

The numeric block clearly contains many stable fields and constants, but its sub-structure is not confirmed. Additional cross-references, a client symbol name list, or in-game examples are needed before naming fields beyond raw offsets.

### Script Foreign Keys

`getknowledge(<id>);` strongly suggests a knowledge reward link. The exact target table and whether every argument resolves through `knowledgelearning.dbss`, `mentalcard.dbss`, or another knowledge table remains unconfirmed.

### Related BSS Files

`hardcorerandomspawncharacterstaticstatusmanager.bss`, `playercharacterstatic.bss`, and `fuelinsertcharacterstaticstatus.bss` are related by name, but they are not required to parse `characterstatic.dbss`. Their layouts should be documented separately if needed.
