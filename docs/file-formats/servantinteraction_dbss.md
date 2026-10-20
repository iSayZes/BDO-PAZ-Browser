# `servantinteraction.dbss` Format

## Purpose

Which horse interactions (Horse Communion) each servant offers: one record
per servant character with a cooldown and a list of
[servantbuff.dbss](servantbuff_dbss.md) keys. On client 3474 the file has
311 records, and every one holds cooldown 1,200,000 and the buff keys 1, 2
and 3.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                            | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------------- | ----- | -------------- | --------- |
| 2      | 3474 and later | 3474    | `servantinteraction.dbss`       | 9,956 | 311 Record     | 32        |
| 2      | 3474 and later | 3474    | `servantinteractionoffset.dbss` | 3,114 | 311 Offset Row | 10        |
| 1      | 1784           | 1784    | `servantinteraction.dbss`       | 6,634 | 255 Record     | 26        |
| 1      | 1784           | 1784    | `servantinteractionoffset.dbss` | 2,554 | 255 Offset Row | 10        |

| Layout | File                            | Known            | Unknown    |
| ------ | ------------------------------- | ---------------- | ---------- |
| 2      | `servantinteraction.dbss`       | 9,956 B (100.0%) | 0 B (0.0%) |
| 2      | `servantinteractionoffset.dbss` | 3,114 B (100.0%) | 0 B (0.0%) |
| 1      | `servantinteraction.dbss`       | 6,634 B (100.0%) | 0 B (0.0%) |
| 1      | `servantinteractionoffset.dbss` | 2,554 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                            | Required | Role                                                  |
| ------------------------------- | -------- | ----------------------------------------------------- |
| `servantinteractionoffset.dbss` | Optional | Index: character ID to the record's offset and size   |
| `servantbuff.dbss`              | Optional | The interactions `buff_keys` point at                 |
| `characterstaticoffset.dbss`    | Optional | Every `characterstatic.dbss` key, so a `character_id` without a row shows as plain text instead of a link |
| `languagedata_en.loc`           | Optional | Servant names (LOC type 6, `str_id1` = `character_id`) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | 311 on client 3474                     |
| `+0x04` | Record[count] | records | Back to back, variable size, up to EOF |

### Record (variable: 20 bytes + buff keys)

| Offset  | Type             | Field            | Notes |
| ------- | ---------------- | ---------------- | ----- |
| `+0x00` | u16              | character_id     | Servant character, as in `servant.bss` |
| `+0x02` | u16              | character_id_dup | Equals `character_id` on every record |
| `+0x04` | u64              | cool_time        | Milliseconds ([Notes](#notes)); 1,200,000 (20 minutes) on every record (client 3474) |
| `+0x0C` | u64              | buff_count       | 3 on every record (client 3474) |
| `+0x14` | u32[buff_count]  | buff_keys        | `servantbuff.dbss` keys; 1, 2, 3 on every record (client 3474) |

### `servantinteractionoffset.dbss`

| Offset  | Type              | Field   | Notes                          |
| ------- | ----------------- | ------- | ------------------------------ |
| `+0x00` | u32               | count   | Equals the main file's count   |
| `+0x04` | Offset Row[count] | entries | `count` entries of 10 bytes; not in file order |

### Offset Row (10 bytes)

| Offset  | Type | Field        | Notes                                                        |
| ------- | ---- | ------------ | ------------------------------------------------------------ |
| `+0x00` | u16  | character_id | The record's `character_id`                                  |
| `+0x02` | u32  | offset       | Where the record's `character_id_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size         | Record size minus 2                                          |

## Layout 1

Client 1784 stores the buff keys as u16, as `servantbuff.dbss` does its keys
there; it has 255 records.

### Record (variable: 20 bytes + buff keys)

| Offset  | Type             | Field            | Notes |
| ------- | ---------------- | ---------------- | ----- |
| `+0x00` | u16              | character_id     | |
| `+0x02` | u16              | character_id_dup | |
| `+0x04` | u64              | cool_time        | |
| `+0x0C` | u64              | buff_count       | |
| `+0x14` | u16[buff_count]  | buff_keys        | |

## Field Names

The names follow the `ServantInteraction_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 (`CharacterKey`, `BuffList`,
`CoolTime`): all 255 records of client 1784 and the 258 client 3474 records
in the sheet match in every column. The 2016
`gc::ServantInteractionStaticStatus` holds `_key`, `_buffKeyList` and
`_coolTime`; the file stores the cooldown before the list.

## Notes

- `cool_time` is in milliseconds: the interaction panel
  (`panel_interaction.luac`) shows the remaining Horse Communion cooldown
  from `vehicleWrapper:getSympatheticCoolTime()` through
  `convertStringFromMillisecondtime`.
- On client 3474, 20 records name a character that is not in
  [servant.bss](servant_bss.md): 9033, 9884 to 9886, 9900, 9986, 31518,
  31534, 31535, 31537, 31538, 31540 to 31543, 31546, 31547, 31561, 31593
  and 35129. All but 9033, 9986 and 35129 have no `characterstatic.dbss`
  row either.
