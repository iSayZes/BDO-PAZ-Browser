# `blizzardregioninfo.bss` Format

## Purpose

Lists the snow regions that the client ties to blizzards: every row names one `regioninfo.bss` region of the Mountain of Eternal Winter (territory 9) or Ulukita (territory 11) and carries two integers and a float whose meaning is not confirmed.

Example:

```text
key=1  -> region 1126 Mountain of Eternal Winter  (400000, 800000, 3.0)
key=11 -> region 1123 Bronte's Bolt                (50000, 120000, 1.0)
key=17 -> region 1382 Velandir                     (500000, 800000, 3.0)
```

The file is small (21 rows in client 3458) and has no strings. The client Lua never mentions it or a blizzard, so the layout below is my own reading of the file.

## Companion Files

| File                  | Required | Role                                                  |
| --------------------- | -------- | ----------------------------------------------------- |
| `languagedata_en.loc` | Optional | Region names (LOC type 17, keyed by `region_key`)     |

All multi-byte values are little-endian unless noted otherwise.

## File Layout

| Offset  | Type    | Field              | Notes                                                    |
| ------- | ------- | ------------------ | -------------------------------------------------------- |
| `+0x00` | char[4] | magic              | `PABR` (ASCII)                                           |
| `+0x04` | u32     | record_count       | Observed `21`                                            |
| `+0x08` | row[]   | records            | `record_count` rows of 26 bytes, byte-packed             |
| varies  | u32     | string_count       | Always `0`: the PABR string table is present but empty   |
| EOF-8   | u32     | string_table_start | Absolute offset of `string_count`; equals `8 + 26 × count` |
| EOF-4   | u32     | zero_trailer       | Always `0`                                               |

The file is `8 + 26 × 21 + 12 = 566` bytes. The parser rejects a file whose rows do not end exactly at `string_table_start`.

## Record Structure

### Row (26 bytes, repeated `record_count` times)

| Offset  | Type | Field      | Notes                                                                                           |
| ------- | ---- | ---------- | ----------------------------------------------------------------------------------------------- |
| `+0x00` | u32  | key        | Unique, ascending, with gaps (`1`, `2`, `6` to `24`)                                            |
| `+0x04` | u16  | region_key | `regioninfo.bss` region key; LOC type 17 names it. Every row resolves                           |
| `+0x06` | u32  | unknown_06 | `50000` to `500000` in steps that pair with `unknown_0a`; always below it                       |
| `+0x0A` | u32  | unknown_0a | `120000` to `800000`                                                                            |
| `+0x0E` | f32  | unknown_0e | `1.0`, `2.0` or `3.0`                                                                           |
| `+0x12` | u32  | unknown_12 | Always `0`                                                                                      |
| `+0x16` | u32  | unknown_16 | Always `0`                                                                                      |

`unknown_06`, `unknown_0a` and `unknown_0e` come in a few fixed sets per area (client 3458):

| unknown_06 | unknown_0a | unknown_0e | Regions                                                                      |
| ---------- | ---------- | ---------- | ---------------------------------------------------------------------------- |
| `400000`   | `800000`   | `3.0`      | 1126 Mountain of Eternal Winter                                              |
| `250000`   | `500000`   | `2.0`      | 1175 Mountain of Eternal Winter; all Ulukita rows except Velandir            |
| `200000`   | `400000`   | `3.0`      | 1146, 1163 Mountain of Eternal Winter                                        |
| `100000`   | `250000`   | `2.0`      | Jade Starlight Forest (1127, 1147, 1164), Snowstorm Guard Post (1125, 1145)  |
| `50000`    | `120000`   | `1.0`      | Bronte's Bolt (1123, 1143, 1160)                                             |
| `500000`   | `800000`   | `3.0`      | 1382 Velandir                                                                |

## Suggested UI Layout

| Column     | Type | Notes                                         |
| ---------- | ---- | --------------------------------------------- |
| Key        | num  | `key`                                         |
| Region Key | num  | `region_key`                                  |
| Region     | text | LOC type 17 name of `region_key`, else a dash |

The `unknown_*` fields stay on the record for search and CSV but out of the table.

## Notes

- A region name can appear on several rows: LOC gives the same name to several region keys (1126, 1146, 1163 and 1175 are all Mountain of Eternal Winter).
- The two zero u32 values at `+0x12` and `+0x16` are kept as `unknown_12` and `unknown_16` because a zero field cannot be told apart from an unused one.
- `edaniaregioninfo.bss` is the other small region-variant table. It is not the same layout (9-byte rows keyed by an Edania region value, no region key), so the two files have separate parsers.

## Open Questions

### Gaps in key

The keys skip `3`, `4` and `5`. Those rows may have been removed in an earlier patch; the client does not show whether the key is read anywhere.

## In-Game Checks

### Blizzard Timing and Strength

Needs zone (all):

- Bronte's Bolt
- Mountain of Eternal Winter

`unknown_06` and `unknown_0a` are two integers per row where the first is
always smaller than the second, in sets such as `50000` / `120000` and
`400000` / `800000`. They read like a minimum and maximum in milliseconds (50
s to 2 min, 6.7 to 13.3 min), but neither the client Lua nor LOC mentions a
blizzard timer. `unknown_0e` is `1.0`, `2.0` or `3.0`, lowest at Bronte's Bolt
and highest in the Mountain of Eternal Winter core (region 1126) and
Velandir; nothing in the client names it.

Stand at Bronte's Bolt and time several blizzards and the clear spells
between them. Lengths between 50 s and 2 min match the `50000` / `120000`
pair, which makes the pair a duration range; a match in one phase only
(blizzard or clear) says which phase it times. Then compare a blizzard in
the Mountain of Eternal Winter core (`3.0`) with one at Bronte's Bolt
(`1.0`): a visibly stronger blizzard, or a larger slow or damage effect,
makes `unknown_0e` a strength level.
