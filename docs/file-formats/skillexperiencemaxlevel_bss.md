# `skillexperiencemaxlevel.bss` Format

## Purpose

Max level of a skill point EXP table. `skillexperiencemaxlevel.bss` holds the top level of [skillexperience](skillexperience_dbss.md) (combat skill points) and `guildskillexperiencemaxlevel.bss` the top level of [guildskillexperience](guildskillexperience_dbss.md) (guild points). Both files share this layout and one handler class. On client 3464 they hold `2000` and `1000`, the last row of each EXP table.

Example:

```text
skillexperiencemaxlevel.bss       Max Level 2000
guildskillexperiencemaxlevel.bss  Max Level 1000
```

All multi-byte values are little-endian.

## File Layout

`PABR` magic, a bare u16 array with no count, then the 12-byte PABR trailer. 18 bytes on client 3464 (one value).

| Offset  | Type    | Field     | Notes                               |
| ------- | ------- | --------- | ----------------------------------- |
| `+0x00` | char[4] | magic     | `PABR` (ASCII)                      |
| `+0x04` | u16[]   | max_level | One value on client 3464            |
| varies  | trailer | trailer   | 12 bytes                            |

The array length is not stored; the parser takes it from the trailer's `end_of_data`: `(end_of_data - 4) / 2` values.

### Trailer (12 bytes)

| Offset  | Type | Field       | Observed | Notes                                        |
| ------- | ---- | ----------- | -------- | -------------------------------------------- |
| `+0x00` | u32  | unknown_00  | `0`      |                                              |
| `+0x04` | u32  | end_of_data | `6`      | Byte offset right after the last `max_level` |
| `+0x08` | u32  | unknown_08  | `0`      |                                              |

The same trailer closes [fitnessmaxlevel](fitnessmaxlevel_bss.md), which stores u32 values instead.

## Notes

- `end_of_data` is `6` in both files, so the value is a u16, not the u32 that the first 8 bytes suggest (`d0 07 00 00`): the next two zero bytes start the trailer.
- The life skill point table [productexperience](productexperience_dbss.md) has no max level file.
