# `npcgiftetc.bss` Format

## Purpose

Defines a tiny global configuration block for the NPC gift/confession system. The file is stored as one fixed-size `PABR` block and has no row count or companion offset table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

The file is exactly 32 bytes in the observed client data. Unlike DBSS records, it does not start with a record count; the first four bytes are the ASCII magic `PABR`.

| Offset  | Type    | Field      | Observed   | Notes                                  |
| ------- | ------- | ---------- | ---------- | -------------------------------------- |
| `+0x00` | char[4] | magic      | `PABR`     | Fixed ASCII file signature             |
| `+0x04` | u16     | unknown_04 | 5          | Global gift-system value               |
| `+0x06` | u16     | unknown_06 | 5          | Global gift-system value               |
| `+0x08` | u32     | unknown_08 | 1000       | Global gift-system value               |
| `+0x0C` | u32     | unknown_0c | 50000000   | Global gift-system value               |
| `+0x10` | u32     | unknown_10 | 0          | Observed zero                          |
| `+0x14` | u32     | unknown_14 | 0          | Observed zero                          |
| `+0x18` | u32     | unknown_18 | 20         | Global gift-system value               |
| `+0x1C` | u32     | unknown_1c | 0          | Observed zero                          |

## Notes

- `npcgiftetc.bss` is self-contained; no offset companion has been observed.
- The block uses the same `PABR` magic seen in several compact BSS lookup/config files, but this file contains scalar config values rather than a repeated table.
- Current evidence only confirms field boundaries and raw values. Field names remain neutral because no local code, LOC text, or companion record confirms gameplay semantics. Earlier versions of this doc called `unknown_04`, `unknown_06`, `unknown_08`, `unknown_0c` and `unknown_18` `config_a` to `config_e`.
- The file is byte-identical in the pre-2026-09-27 fixture and the 2026-09-27 client.

## Open Questions

### Config Field Semantics

The gameplay meanings of `unknown_04`, `unknown_06`, `unknown_08`, `unknown_0c` and `unknown_18` are not confirmed. Plausible roles include gift limits, thresholds, cooldowns, or cost/value settings, but the file itself provides only raw numeric values.
