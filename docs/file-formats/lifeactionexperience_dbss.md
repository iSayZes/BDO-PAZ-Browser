# `lifeactionexperience.dbss` Format

## Purpose

Life skill EXP per item: each row names an item and up to two life skills
with an EXP amount each. On clients 1784 and 3474 every EXP amount is `0`
and every first life skill is `0` (Gathering), so the file holds a list of
items and no working EXP. `lifeactionexperienceoffset.dbss` is the
item-keyed index into it.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes  | Records          | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ------ | ---------------- | --------- |
| 1      | 1784 and later | 3474    | `lifeactionexperience.dbss`       | 79,356 | 3,052 Row        | 26        |
| 1      | 1784 and later | 3474    | `lifeactionexperienceoffset.dbss` | 36,628 | 3,052 Offset Row | 12        |

| Layout | File                              | Known             | Unknown    |
| ------ | --------------------------------- | ----------------- | ---------- |
| 1      | `lifeactionexperience.dbss`       | 79,356 B (100.0%) | 0 B (0.0%) |
| 1      | `lifeactionexperienceoffset.dbss` | 36,628 B (100.0%) | 0 B (0.0%) |

<!-- versions:end -->

## Companion Files

| File                              | Required | Role                                                     |
| --------------------------------- | -------- | -------------------------------------------------------- |
| `lifeactionexperienceoffset.dbss` | Optional | `item_key -> (data_offset, data_size)` index; the rows are fixed size and can be walked without it |
| `languagedata_en.loc`             | Optional | Item name for `item_key` (`str_type=0`, `str_id1=item_key`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes                                      |
| ------- | ---------- | ----- | ------------------------------------------ |
| `+0x00` | u32        | count | Number of rows; `3,052` on client 3474     |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (26 bytes)

| Offset  | Type   | Field             | Notes                                                              |
| ------- | ------ | ----------------- | ------------------------------------------------------------------ |
| `+0x00` | u32    | item_key          | Item, packed as `enchant_level << 24 \| item_id`; unique per row, the index key |
| `+0x04` | u32    | item_key_dup      | Equal to `item_key` in every row; the index's `data_offset` points here |
| `+0x08` | u8[2]  | life_action_types | Life skill per slot, see [Life Skills](lifeexp_dbss.md#life-skills); `15` (`Type_Count`) is an empty slot |
| `+0x0A` | i64[2] | experiences       | EXP per slot; `0` in every slot (clients 1784 and 3474)            |

Every `item_key` has a zero top byte (enhancement level 0) on both clients.
The rows are not sorted by key.

### `lifeactionexperienceoffset.dbss`

| Offset  | Type              | Field | Notes                                          |
| ------- | ----------------- | ----- | ---------------------------------------------- |
| `+0x00` | u32               | count | Equals the `lifeactionexperience.dbss` count   |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row           |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                     |
| ------- | ---- | ----------- | ----------------------------------------- |
| `+0x00` | u32  | item_key    | Row key                                   |
| `+0x04` | u32  | data_offset | Row start + 4, at `item_key_dup`          |
| `+0x08` | u32  | data_size   | Row size - 4: `22`                        |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key.

## Field Names

The row is the 2016 `gc::LifeActionExperienceStaticStatus` after the index
key: `_itemKey` (a `gc::ItemEnchantKey`), `_type`
(`pa::Array<gc::LifeExperienceType,2>`) and `_experience`
(`pa::Array<__int64,2>`). The 2016 `gc::LifeExperienceType` ends at
`Type_Count = 9`; the client 3474 Lua's `CppEnums.LifeExperienceType` ends at
`Type_Count = 15`, the empty slot value on both clients.

The values match the `LifeActionEXP_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784 by `ItemKey`. An empty sheet cell in the
second slot is type `15` with EXP `0`.

| Field             | Column                                 | Same value (client 1784) | Same value (client 3474) |
| ----------------- | -------------------------------------- | ------------------------ | ------------------------ |
| item_key          | `ItemKey`                              | 1,817 of 1,817 rows      | 1,836 of 3,052 rows      |
| life_action_types | `LifeActionType0`, `LifeActionType1`   | 1,817 of 1,817           | 1,835 of 1,836           |
| experiences       | `Exp0`, `Exp1`                         | 1,817 of 1,817           | 1,836 of 1,836           |

The sheet has 1,858 rows. Client 1784 lacks 41 of them (`9069`, `9339` to
`9379` with gaps, `9640` and `9641`); client 3474 lacks 22 (`5201` Fruit of
Crimson Flame to `5217` with gaps, and seven keys from `9347` to `9377`). The one row that differs on client 3474 is `4999` Black Gem
Fragment, which gained a second Gathering slot after client 1784. The client
3474 file adds 1,216 keys the sheet lacks, up to `890074` Endless Ocean
Draught.

## Notes

- On client 3474, 141 rows fill both slots with Gathering (`0`, `0`) and
  2,911 fill the first slot only. The two-slot rows include processed
  materials (`4078` Melted Vanadium Shard, `4098` Melted Magnetite Shard),
  `4476` Red Coral, `5006` Spirit's Leaf and `5401` Sunrise Herb. The
  one-slot rows include items no life skill gives, such as `292` Flare of
  the Ancients and `518` HP Potion (Medium).
- No client Lua file names the table or reads it, and the client 1784 sheet
  holds `0` in every `Exp` cell too.
- [bdo-data-extractor](https://github.com/iDevelopThings/bdo-data-extractor)
  lists this file with `actionexp.dbss` as "offset-indexed action award
  tables" whose record payloads "do not follow the ordinary decoded
  DBSS/PABR forms". The row is a plain fixed-size struct with a u32 count before it.

## Open Questions

### What The Life Skill Slots Select

Every row holds `0` EXP, so the file awards nothing on clients 1784 and
3474. Why 141 items carry a second Gathering slot, and what the item list
selects when the EXP is zero, has no reader in the client Lua to show.
