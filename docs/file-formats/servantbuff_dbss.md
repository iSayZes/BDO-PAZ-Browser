# `servantbuff.dbss` Format

## Purpose

Horse interaction (Horse Communion) actions: one record per interaction with
an optional class condition, the player's action, the horse's action and the
skill it uses. [servantinteraction.dbss](servantinteraction_dbss.md) lists
which of these each servant offers. On client 3474 the file has 4 records:
keys 1 to 3 are Horse Communion 1 to 3 (skills 220 to 222), key 4 is the
Tamer's version (`checkClass(16)`, skill 15526 `말과교감_금수랑전용`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes | Records      | Row bytes                |
| ------ | -------------- | ------- | ------------------------ | ----- | ------------ | ------------------------ |
| 2      | 3474 and later | 3474    | `servantbuff.dbss`       | 384   | 4 Record     | 88 to 116, 95 on average |
| 2      | 3474 and later | 3474    | `servantbuffoffset.dbss` | 52    | 4 Offset Row | 12                       |
| 1      | 1784           | 1784    | `servantbuff.dbss`       | 256   | 3 Record     | 84                       |
| 1      | 1784           | 1784    | `servantbuffoffset.dbss` | 34    | 3 Offset Row | 10                       |

| Layout | File                     | Known          | Unknown    |
| ------ | ------------------------ | -------------- | ---------- |
| 2      | `servantbuff.dbss`       | 384 B (100.0%) | 0 B (0.0%) |
| 2      | `servantbuffoffset.dbss` | 52 B (100.0%)  | 0 B (0.0%) |
| 1      | `servantbuff.dbss`       | 256 B (100.0%) | 0 B (0.0%) |
| 1      | `servantbuffoffset.dbss` | 34 B (100.0%)  | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                          |
| ------------------------ | -------- | --------------------------------------------- |
| `servantbuffoffset.dbss` | Optional | Index: key to the record's offset and size    |
| `languagedata_en.loc`    | Optional | `skill_no` names (LOC type 10); without a row, the Korean `skilltype.dbss` name |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                  |
| ------- | ------------- | ------- | -------------------------------------- |
| `+0x00` | u32           | count   | 4 on client 3474                       |
| `+0x04` | Record[count] | records | Back to back, variable size, up to EOF |

### Record (variable: 42 bytes + condition and action names)

| Offset                       | Type  | Field               | Notes |
| ---------------------------- | ----- | ------------------- | ----- |
| `+0x00`                      | u32   | key                 | 4 down to 1 on client 3474 |
| `+0x04`                      | u32   | key_dup             | Equals `key` on every record |
| `+0x08`                      | str16 | condition           | Empty except `checkClass(16)` (Tamer) on key 4 |
| `condition+0x00`             | str8  | action_name         | `VEHICLE_INTERACTION_HORSE_1` to `_4` |
| `action_name+0x00`           | u32   | action_hash         | Hash of `action_name` ([Action Hashes](#action-hashes)) |
| `action_name+0x04`           | str8  | servant_action_name | `HORSE_INTERACTION_1` to `_3`; key 4 uses `_3` |
| `servant_action_name+0x00`   | u32   | servant_action_hash | Hash of `servant_action_name`; equal on keys 3 and 4 |
| `servant_action_name+0x04`   | u16   | skill_no            | `skill.dbss` skill number: 220, 221, 222, 15526 |

### `servantbuffoffset.dbss`

| Offset  | Type              | Field   | Notes                          |
| ------- | ----------------- | ------- | ------------------------------ |
| `+0x00` | u32               | count   | Equals the main file's count   |
| `+0x04` | Offset Row[count] | entries | `count` entries of 12 bytes    |

### Offset Row (12 bytes)

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u32  | key    | The record's `key`                                       |
| `+0x04` | u32  | offset | Where the record's `key_dup` starts, 4 bytes into the record |
| `+0x08` | u32  | size   | Record size minus 4                                      |

## Layout 1

Client 1784 stores both keys and the index key as u16 and has 3 records
(keys 3 to 1, no condition).

### Record (variable: 38 bytes + condition and action names)

| Offset                       | Type  | Field               | Notes |
| ---------------------------- | ----- | ------------------- | ----- |
| `+0x00`                      | u16   | key                 | |
| `+0x02`                      | u16   | key_dup             | |
| `+0x04`                      | str16 | condition           | Empty on every record |
| `condition+0x00`             | str8  | action_name         | |
| `action_name+0x00`           | u32   | action_hash         | |
| `action_name+0x04`           | str8  | servant_action_name | |
| `servant_action_name+0x00`   | u32   | servant_action_hash | |
| `servant_action_name+0x04`   | u16   | skill_no            | |

### Offset Row (10 bytes)

| Offset  | Type | Field  | Notes                                                    |
| ------- | ---- | ------ | -------------------------------------------------------- |
| `+0x00` | u16  | key    | |
| `+0x02` | u32  | offset | Where the record's `key_dup` starts, 2 bytes into the record |
| `+0x06` | u32  | size   | Record size minus 2                                      |

## Field Names

The record follows the 2016 `gc::ServantBuffStaticStatus` member for member:
`_key`, `_conditionString`, `_actionName`, `_actionHashKey`,
`_servantActionName`, `_servantActionHashKey`, `_skillNo`. The
`ServantBuff_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 (`Index`, `UseCondition`, `ActionName`, `SkillNo`,
`ServantActionName`) matches all 3 records of clients 1784 and 3474 by
value in every column.

## Action Hashes

`action_hash` and `servant_action_hash` are the client's lookup3
`hashlittle` with seed `0xC5EDE` over the ASCII bytes of the name before
them, as in `manufacture.bss` (`ascii_key_hash` in
`_common/string_hash.py`); all 4 records of client 3474 match.

## Notes

- No `servantinteraction.dbss` record lists key 4 on client 3474; every
  record lists 1, 2 and 3. How the Tamer's version is offered is not in
  either file.
