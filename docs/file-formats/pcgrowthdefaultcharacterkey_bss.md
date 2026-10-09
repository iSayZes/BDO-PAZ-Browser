# `pcgrowthdefaultcharacterkey.bss` Format

## Purpose

An 18-byte PABR file holding one u16 character key, `47` on client 3464. It sits next to [pcgrowth](pcgrowth_dbss.md) and [pcgrowthsimply](pcgrowthsimply_bss.md). No browser handler reads it.

All multi-byte values are little-endian.

## File Layout

| Offset  | Type    | Field              | Notes               |
| ------- | ------- | ------------------ | ------------------- |
| `+0x00` | char[4] | magic              | `PABR`              |
| `+0x04` | u16     | character_key      | `47` on client 3464 |
| `+0x06` | u32     | string count       | `0`                 |
| `+0x0A` | u32     | string_table_start | `6`                 |
| `+0x0E` | u32     | zero               | `0`                 |

The string table starts at `+0x06`, so the rows end after the single u16.

## Notes

- `47` is the character key of class type 46 (`PYFW5`, LOC type 6 `PYFW5`) in `pcgrowth.dbss`, and also the row count of `pcgrowth.dbss`, `pcgrowthoffset.dbss` and `pcgrowthsimply.bss`.

## Open Questions

### Character Key or Class Count

The stored `47` is both the character key of the last class slot and the class count. A client where the class count changes would show which one the file tracks.
