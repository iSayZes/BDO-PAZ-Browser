# `npcgiftetc.bss` Format

## Purpose

Defines a tiny global configuration block for the NPC gift/confession system. The file is stored as one fixed-size `PABR` block and has no row count or companion offset table.

Example:

```text
PABR config: first limits = 5 / 5, value thresholds = 1000 / 50000000 / 20
```

## Graph

### Tags

- file format
- bss
- npc
- gift
- amity
- config

### Connections

- [npcgift.dbss](npcgift_dbss.md) - NPC gift item table and confession dialogue records that use this file as an optional global config companion

---

## File Layout

All multi-byte values are little-endian.

The file is exactly 32 bytes in the observed client data. Unlike DBSS records, it does not start with a record count; the first four bytes are the ASCII magic `PABR`.

| Offset  | Type    | Field     | Observed   | Notes                                  |
| ------- | ------- | --------- | ---------- | -------------------------------------- |
| `+0x00` | char[4] | magic     | `PABR`     | Fixed ASCII file signature             |
| `+0x04` | u16     | config_a  | 5          | Global gift-system value               |
| `+0x06` | u16     | config_b  | 5          | Global gift-system value               |
| `+0x08` | u32     | config_c  | 1000       | Global gift-system value               |
| `+0x0C` | u32     | config_d  | 50000000   | Global gift-system value               |
| `+0x10` | u32     | reserved0 | 0          | Observed zero                          |
| `+0x14` | u32     | reserved1 | 0          | Observed zero                          |
| `+0x18` | u32     | config_e  | 20         | Global gift-system value               |
| `+0x1C` | u32     | reserved2 | 0          | Observed zero                          |

---

## Suggested UI Layout

| Column | Type | Notes                                      |
| ------ | ---- | ------------------------------------------ |
| Field  | text | `config_a` through `config_e`, `reserved*` |
| Value  | num  | Raw decoded integer value                  |
| Notes  | text | Observed role or unresolved status         |

---

## Notes

- `npcgiftetc.bss` is self-contained; no offset companion has been observed.
- The block uses the same `PABR` magic seen in several compact BSS lookup/config files, but this file contains scalar config values rather than a repeated table.
- Current evidence only confirms field boundaries and raw values. Field names remain neutral because no local code, LOC text, or companion record confirms gameplay semantics.

---

## Open Questions

### Config Field Semantics

The gameplay meanings of `config_a` through `config_e` are not confirmed. Plausible roles include gift limits, thresholds, cooldowns, or cost/value settings, but the file itself provides only raw numeric values.
