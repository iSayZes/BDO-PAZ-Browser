# `employeespawninfo.dbss` Format

## Purpose

Hire data of the sailors that wait in Velia, Port Epheria and Iliya Island (the client calls sailors "employees"). One row per sailor character `59053` to `59072`: its sailor ID in `employeestaticstatus.bss`, the `employeespawnposition.dbss` spots it can appear on, the item a hire costs, and the line the sailor says when it agrees to be hired or turns the player down. Companion `employeespawninfooffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes | Records                      | Row bytes |
| ------ | -------------- | ------- | ------------------------------ | ----- | ---------------------------- | --------- |
| 1      | 1485 and later | 3474    | `employeespawninfo.dbss`       | 3,702 | 20 Hire Block, 20 Sailor Row | 44        |
| 1      | 1485 and later | 3474    | `employeespawninfooffset.dbss` | 204   | 20 Offset Row                | 10        |

| Layout | File                           | Known           | Unknown       |
| ------ | ------------------------------ | --------------- | ------------- |
| 1      | `employeespawninfo.dbss`       | 3,062 B (82.7%) | 640 B (17.3%) |
| 1      | `employeespawninfooffset.dbss` | 204 B (100.0%)  | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   |
| ------ | -------- |
| 3474   | Layout 1 |
| 3251   | Layout 1 |
| 3002   | Layout 1 |
| 2519   | Layout 1 |
| 2107   | Layout 1 |
| 1784   | Layout 1 |
| 1485   | Layout 1 |
| 1230   | No file  |
| 794    | No file  |

<!-- versions:end -->

## Companion Files

| File                               | Required | Role                                                                     |
| ---------------------------------- | -------- | ------------------------------------------------------------------------ |
| `employeespawninfooffset.dbss`     | Required | `character_key -> (offset, size)` of every row                           |
| `employeespawnposition.dbss`       | Optional | Region of each spawn position, for the Towns column                       |
| `employeespawnpositionoffset.dbss` | Optional | Offset table of `employeespawnposition.dbss`                              |
| `languagedata_en.loc`              | Optional | Sailor name and title (type 6), accept and refuse lines (type 70), item name (type 0), region names (type 17) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type              | Field | Notes                                                       |
| ------- | ----------------- | ----- | ----------------------------------------------------------- |
| `+0x00` | u32               | count | Number of rows (observed: 20)                               |
| `+0x04` | Sailor Row[count] | rows  | `count` variable-length rows, read through the offset table |

The rows follow each other with no gap and end at the end of the file (3,702 bytes on client 3458).

### Sailor Row (variable: 74 bytes + spawn keys and text)

| Offset                     | Type             | Field                        | Notes                                                                           |
| -------------------------- | ---------------- | ---------------------------- | ------------------------------------------------------------------------------- |
| `+0x00`                    | u16              | character_key                | Row key; the sailor character, `59053` to `59072`                               |
| `+0x02`                    | u32              | employee_key                 | Sailor ID in `employeestaticstatus.bss` (`1` to `20`, the same character there) |
| `+0x06`                    | u32              | spawn_count                  | Number of spawn positions, `1` or `2`                                           |
| `+0x0A`                    | u32[spawn_count] | spawn_position_keys          | Keys of `employeespawnposition.dbss` rows                                       |
| `spawn_position_keys+0x00` | Hire Block       | hire                         | See Hire Block                                                                  |
| `spawn_position_keys+0x2C` | str16            | accept_text_kr               | Korean line when the sailor agrees to be hired; u64 length in UTF-16 units      |
| `accept_text_kr+0x00`      | str16            | refuse_text_kr               | Korean line when the sailor turns the player down                               |
| `refuse_text_kr+0x00`      | u32              | unknown_after_refuse_text_kr | Always `0`; the row ends after it                                               |

The inline text holds real line breaks (`0x0A`), not the `\n` escape of `buff.dbss` and `skill.dbss`.

Earlier versions of this doc called `unknown_after_refuse_text_kr` `terminator`.

### Hire Block (44 bytes)

Offsets count from the end of `spawn_position_keys`. Every row of client 3458 holds the same 44 bytes.

| Offset  | Type | Field           | Notes                                                            |
| ------- | ---- | --------------- | ---------------------------------------------------------------- |
| `+0x00` | u32  | unknown_00      | Always `0`                                                       |
| `+0x04` | u32  | unknown_04      | Always `0`                                                       |
| `+0x08` | u32  | unknown_08      | Always `0`                                                       |
| `+0x0C` | u32  | unknown_0c      | Always `0`                                                       |
| `+0x10` | u32  | respawn_time_s  | Always `3600`; seconds, the one-hour sailor respawn time in game |
| `+0x14` | u32  | unknown_14      | Always `0`                                                       |
| `+0x18` | u32  | unknown_18      | Always `1000000`; see Open Questions                             |
| `+0x1C` | u32  | hire_item_key   | Always `752030`, Sailor Contract Certificate (LOC type 0)        |
| `+0x20` | u64  | hire_item_count | Always `1`                                                       |
| `+0x28` | u32  | unknown_28      | Always `1000000`; see Open Questions                             |

The item text of `752030` reads "A certificate required for hiring a sailor", and the grumpygreen.cricket sailor guide states one certificate per hired sailor, which matches `hire_item_count` `1`. Item counts are 64-bit in the client (`getNeedItemCount_s64` in `panel_dialog_employee_hireitem_all_1.luac`); the upper half of `hire_item_count` is `0` on every row, so a u32 count and a zero u32 would read the same.

### `employeespawninfooffset.dbss`

Bare offset table into `employeespawninfo.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                             |
| ------- | ----------------- | ----- | ------------------------------------------------- |
| `+0x00` | u32               | count | Number of offset rows; equals the main file count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                    |

### Offset Row (10 bytes)

| Offset  | Type | Field         | Notes                                            |
| ------- | ---- | ------------- | ------------------------------------------------ |
| `+0x00` | u16  | character_key | Key of the row it points at                      |
| `+0x02` | u32  | data_offset   | Absolute byte offset in `employeespawninfo.dbss` |
| `+0x06` | u32  | data_size     | Row size in bytes, `136` to `236`                |

The rows are in file order, which is not key order (59061, 59053, 59055, 59064, ...). The parser reads the main file through these rows, checks that every row holds the key of the offset row that points at it, and checks that the row ends exactly at `data_offset + data_size`.

## Localization

| Text            | LOC key                                                  |
| --------------- | -------------------------------------------------------- |
| Name            | type 6, `str_id1` = `character_key`, `str_id4` 0 (`Sailor`) |
| Title           | type 6, `str_id1` = `character_key`, `str_id4` 1 (`<Ambitious>`) |
| Accept line     | type 70, `str_id1` = `character_key`, `str_id4` 0         |
| Refuse line     | type 70, `str_id1` = `character_key`, `str_id4` 1         |
| Hire item       | type 0, `str_id1` = `hire_item_key`                       |
| Town            | type 17, `str_id1` = `region_key` of the spawn position   |

LOC type 70 holds exactly these 40 lines on client 3458, `str_id4` 0 and 1 for each of the 20 characters. The English line matches the inline Korean one (59053: "I will get rid of all the prejudice you have on Goblins." for "고블린에 대한 편견을 다 없애드리지요."). The handler shows the LOC text and falls back to the inline Korean. Without LOC the Name and Title columns show the Korean `characterstatic.dbss` name and title (`59053` `선원 <욕심 있는>`).

## Notes

- `employee_key` is the sailor ID of `employeestaticstatus.bss`: all 20 rows match its level 1 row for the same character (`1` = `59053` to `20` = `59072`). Sailors `21` to `23` of that table (`59101`, `59227`, `59228`) and the First Mates have no row here; they are not hired in a port town.
- The spawn positions of each sailor agree with the location chart of the grumpygreen.cricket sailor guide for 19 of 20 sailors (Ambitious: Velia and Port Epheria; Born in the Sea: Iliya Island; Quick-Witted: Velia and Iliya Island). The guide lists Tenacious (`59062`, positions `2` and `42`) in Velia only.
- Every row has one or two spawn positions, and every two-position row names two different towns.
- The `employeespawnposition.dbss` handler reads this file as an optional companion for its Sailors column (see [employeespawnposition](employeespawnposition_dbss.md)).

## Open Questions

### unknown_18 and unknown_28

Both store `1000000`, which is the client's 100% for rates stored out of 1,000,000. Either could be a hire success chance or a spawn chance. A row with another value after a patch would tell them apart.

### unknown_00 to unknown_0c and unknown_14

These five u32 values are `0` on every row. The first could be the count of an empty list rather than a fixed field; a row with a non-zero value would show which.
