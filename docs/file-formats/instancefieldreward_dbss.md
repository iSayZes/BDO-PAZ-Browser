# `instancefieldreward.dbss` Format

## Purpose

The rewards of an instance dungeon: per dungeon number a skill to learn,
five reward item groups (`itemmaingroup.bss` keys, one per grade), three
push item slots and a list of related regions. On client 3474 the file has
2 rows, dungeons `199` and `291`, both with the item groups `56001` to
`56005`; `291` lists the regions Moretti Plantation (`62`), Lynch Farm
Ruins (`63`) and Glish Swamp (`37`). Companion
`instancefieldrewardoffset.dbss` lists where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | -------------------------------- | ----- | ------------------ | --------- |
| 2      | 3474 and later | 3474    | `instancefieldreward.dbss`       | 154   | 6 Push Item, 2 Row | 12        |
| 2      | 3474 and later | 3474    | `instancefieldrewardoffset.dbss` | 24    | 2 Offset Row       | 10        |
| 1      | 1784           | 1784    | `instancefieldreward.dbss`       | 134   | 6 Push Item, 2 Row | 12        |
| 1      | 1784           | 1784    | `instancefieldrewardoffset.dbss` | 24    | 2 Offset Row       | 10        |

| Layout | File                             | Known         | Unknown      |
| ------ | -------------------------------- | ------------- | ------------ |
| 2      | `instancefieldreward.dbss`       | 82 B (53.2%)  | 72 B (46.8%) |
| 2      | `instancefieldrewardoffset.dbss` | 24 B (100.0%) | 0 B (0.0%)   |
| 1      | `instancefieldreward.dbss`       | 62 B (46.3%)  | 72 B (53.7%) |
| 1      | `instancefieldrewardoffset.dbss` | 24 B (100.0%) | 0 B (0.0%)   |

<!-- versions:end -->

## Companion Files

| File                             | Required | Role                                                                     |
| -------------------------------- | -------- | ------------------------------------------------------------------------ |
| `instancefieldrewardoffset.dbss` | Optional | `instance_dungeon_no -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`            | Optional | Region names (LOC type 17)                                               |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 36 bytes + push items and regions)

| Offset                 | Type                        | Field                   | Notes                                                       |
| ---------------------- | --------------------------- | ----------------------- | ----------------------------------------------------------- |
| `+0x00`                | u16                         | instance_dungeon_no     | Row key                                                     |
| `+0x02`                | u16                         | instance_dungeon_no_dup | Equal to `instance_dungeon_no`; the offset file points here |
| `+0x04`                | u32                         | learn_skill             | `0` (no skill) on both rows of clients 1784 and 3474         |
| `+0x08`                | u32[5]                      | item_groups             | `itemmaingroup.bss` keys, the sheet's `Grade1` to `Grade5`   |
| `+0x1C`                | u32                         | push_item_count         | `3` on both rows                                            |
| `+0x20`                | Push Item[push_item_count]  | push_items              | See Push Item                                               |
| `push_items+0x00`      | u32                         | related_region_count    | Number of regions                                           |
| `push_items+0x04`      | u16[related_region_count]   | related_regions         | `regioninfo.bss` region keys, the sheet's `RegionNo`        |

### Push Item (12 bytes)

| Offset  | Type | Field      | Notes                                       |
| ------- | ---- | ---------- | ------------------------------------------- |
| `+0x00` | u32  | unknown_00 | `0` in every slot of clients 1784 and 3474  |
| `+0x04` | i64  | unknown_04 | `0` in every slot of clients 1784 and 3474  |

### `instancefieldrewardoffset.dbss`

Bare offset table into `instancefieldreward.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                        |
| ------- | ----------------- | ----- | -------------------------------------------- |
| `+0x00` | u32               | count | Equals the `instancefieldreward.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                               |

### Offset Row (10 bytes)

| Offset  | Type | Field               | Notes                                                         |
| ------- | ---- | ------------------- | ------------------------------------------------------------- |
| `+0x00` | u16  | instance_dungeon_no | Key of the row it points at                                   |
| `+0x02` | u32  | data_offset         | Row start + 2, at `instance_dungeon_no_dup`                   |
| `+0x06` | u32  | data_size           | The row without its leading `instance_dungeon_no`             |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. On clients
1784 and 3474 every index row points at the row with its key.

## Layout 1

Client 1784 stores the five item groups as u16.

### Row (variable: 26 bytes + push items and regions)

| Offset            | Type                       | Field                   | Notes |
| ----------------- | -------------------------- | ----------------------- | ----- |
| `+0x00`           | u16                        | instance_dungeon_no     |       |
| `+0x02`           | u16                        | instance_dungeon_no_dup |       |
| `+0x04`           | u32                        | learn_skill             |       |
| `+0x08`           | u16[5]                     | item_groups             |       |
| `+0x12`           | u32                        | push_item_count         |       |
| `+0x16`           | Push Item[push_item_count] | push_items              |       |
| `push_items+0x00` | u32                        | related_region_count    |       |
| `push_items+0x04` | u16[related_region_count]  | related_regions         |       |

## Field Names

The 2016 client's debug symbols have `gc::InstanceFieldRewardStaticStatus`
as `_fieldNo` (short), `_itemGroupList` (5 u16 keys), resolved pointers, a
`_pushItemStaticList` of 3 `gc::ItemStaticInformation`, `_learnSkillKey`
and `_relatedRegion` (a vector of u16 region keys). The
`Instance_Reward` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `InstanceDundeonNo` (sic), `LearnSkill`, `RegionNo`,
`PushItem1` to `PushItem3` and `Grade1` to `Grade5`. Its 2 rows match the
client 1784 file on both keys: `LearnSkill` and the push items are empty
(`0`), `Grade1` to `Grade5` are `56001` to `56005`, and `RegionNo` of `291`
is `62, 63, 37`. The u32 before the item groups is `LearnSkill` by the
2016 member list; the file moves it ahead of the groups.

## Notes

- `199` and `291` are not keys of `instancefield.dbss`,
  `instancefieldmapinfo.bss` or `fieldinfo.bss` on client 3474.
- The push item slots hold 12 bytes each, the size of an item key and an
  item count; with every slot `0` the two parts cannot be told apart, so
  they stay `unknown_00` and `unknown_04`.

## Open Questions

### What the Dungeon Number Keys

`InstanceDundeonNo` `199` and `291` match no key of the instance field,
instance field map or field tables. Which content the two reward rows
belong to is open.
